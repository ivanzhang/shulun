#!/usr/bin/env python3
"""生成 cofactor-LPF 覆盖债务的 dyadic pressure/product-width 证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_dyadic_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json",
]

PREVIOUS_TARGET = "CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC"
EXCESS_THRESHOLD = "CofactorCoverExcessThresholdLedger"
ACTIVE_PRODUCT = "ActiveCofactorPrimeProductDichotomyLedger"
DYADIC_R_PARTITION = "DyadicCofactorPrimePressurePartitionLedger"
OVERFULL_LOCALIZATION = "OverfullDyadicRLayerLocalizationLedger"
M_INTERVAL = "FixedRToMIntervalEndpointLedger"
R_LAYER_CRT = "RLayerRoughMCRTSupportLedger"
SMALL_PRODUCT = "SmallProductActiveCoverConcentrationPDEC"
NEW_TARGET = "DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC"

REDUCED_TARGET = (
    f"{EXCESS_THRESHOLD} AND {ACTIVE_PRODUCT} AND {DYADIC_R_PARTITION} "
    f"AND {OVERFULL_LOCALIZATION} AND {M_INTERVAL} AND {R_LAYER_CRT} "
    f"AND {SMALL_PRODUCT} AND {NEW_TARGET}"
)


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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 cofactor-LPF cover 硬点替换为 dyadic pressure 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 dyadic pressure/product-width 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "CofactorLPFCoverDebtImported",
            imported,
            False,
            "上一层把 rough 支撑不足改写为 cofactor 最小素因子覆盖过量或 product-width ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "ExcessThresholdClosed",
            True,
            True,
            "对 cell C，令 H_C=F_C-A_C；局部反例要求 E_C>H_C。",
            EXCESS_THRESHOLD,
        ),
        row(
            "ActivePrimeProductDichotomyClosed",
            True,
            True,
            "活动 cofactor primes R_C 的乘积 M_C=prod R_C；若 M_C 超过支撑宽度，则进入 product-width ColumnCRT/PDEC，否则进入 small-product concentration。",
            ACTIVE_PRODUCT,
        ),
        row(
            "DyadicRPartitionClosed",
            True,
            True,
            "按 Z<r<=2Z 分解 E_C=sum_Z E_Z，同时 M_C=prod_Z M_Z。",
            DYADIC_R_PARTITION,
        ),
        row(
            "OverfullLocalizationClosed",
            True,
            True,
            "若 E_C>H_C 且候选允许预算 sum_Z U_Z<=H_C，则至少一个 dyadic r 层满足 E_Z>U_Z。",
            OVERFULL_LOCALIZATION,
        ),
        row(
            "FixedRMEndpointClosed",
            True,
            True,
            "固定 r 后，n=r*m 给出 m_min=ceil(n_min/r)、m_max=floor(n_max/r) 的显式短区间。",
            M_INTERVAL,
        ),
        row(
            "RLayerCRTClosed",
            True,
            True,
            "固定 r 层保留 gcd(m,W_<r)=1，成为更低阶 rough-m CRT 支撑。",
            R_LAYER_CRT,
        ),
        row(
            "SmallProductConcentrationStillOpen",
            False,
            False,
            "仍未排除 active product 小于支撑宽度时的局部高覆盖集中。",
            SMALL_PRODUCT,
        ),
        row(
            "CofactorCoverDebtReduced",
            True,
            False,
            "CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC 被压成 excess threshold、active product 二分、dyadic r 压力层与 small-product 出口。",
            REDUCED_TARGET,
        ),
        row(
            "DyadicPressureExcluded",
            False,
            False,
            "本步没有证明 dyadic r 层过载不可能。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 dyadic cofactor-LPF pressure 或 small-product ColumnCRT/PDEC。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 dyadic pressure/product-width 分解证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "cofactor-LPF 覆盖债务被继续拆成局部 excess threshold、活动素因子 product-width 二分、"
        "dyadic r 层压力定位和固定 r 的 rough-m CRT 支撑。若活动素因子乘积大于 cell 支撑宽度，"
        "只能作为 product-width ColumnCRT/PDEC 复现；若乘积不大，则反例必须集中在 small-product "
        "active cover，且至少一个 dyadic r 层超过其候选预算。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_cofactor_lpf_dyadic_pressure_router",
        "status": "cofactor_lpf_cover_debt_reduced_to_dyadic_pressure_or_small_product_columncrt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "cofactor_lpf_cover_debt_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "excess_threshold_closed": True,
        "active_prime_product_dichotomy_closed": True,
        "dyadic_r_partition_closed": True,
        "overfull_localization_closed": True,
        "fixed_r_m_endpoint_closed": True,
        "r_layer_crt_closed": True,
        "small_product_concentration_excluded": False,
        "dyadic_pressure_excluded": False,
        "row_column_unconditional_closed": False,
        "dyadic_pressure_formulas": {
            "excess_threshold": "H_C=F_C-A_C; local debt requires E_C>H_C",
            "active_set": "R_C={r prime: E_r(C)>0}",
            "active_product": "M_C=prod_{r in R_C}r",
            "product_width_branch": "M_C>width(C) => product-width ColumnCRT/PDEC or finite atom",
            "small_product_branch": "M_C<=width(C) => small-product active cover concentration",
            "dyadic_r_layer": "E_Z(C)=sum_{Z<r<=2Z}E_r(C)",
            "r_layer_product": "M_Z=prod_{Z<r<=2Z, E_r(C)>0}r; M_C=prod_Z M_Z",
            "overfull_pigeonhole": "E_C>H_C and sum_Z U_Z<=H_C => exists Z with E_Z(C)>U_Z",
            "fixed_r_endpoint": "n in [n_min,n_max], n=r*m => m_min=ceil(n_min/r), m_max=floor(n_max/r)",
            "fixed_r_crt": "E_r(C)=sum_{m_min<=m<=m_max, gcd(m,W_<r)=1} alpha_{ell,r*m}",
            "new_failure": "dyadic r-layer overpressure or small-product ColumnCRT/PDEC",
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
        "# Prime Matrix cofactor-LPF dyadic pressure 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"cofactor_lpf_cover_debt_imported={fmt_bool(cert['cofactor_lpf_cover_debt_imported'])}",
        f"excess_threshold_closed={fmt_bool(cert['excess_threshold_closed'])}",
        f"active_prime_product_dichotomy_closed={fmt_bool(cert['active_prime_product_dichotomy_closed'])}",
        f"dyadic_r_partition_closed={fmt_bool(cert['dyadic_r_partition_closed'])}",
        f"overfull_localization_closed={fmt_bool(cert['overfull_localization_closed'])}",
        f"fixed_r_m_endpoint_closed={fmt_bool(cert['fixed_r_m_endpoint_closed'])}",
        f"r_layer_crt_closed={fmt_bool(cert['r_layer_crt_closed'])}",
        f"small_product_concentration_excluded={fmt_bool(cert['small_product_concentration_excluded'])}",
        f"dyadic_pressure_excluded={fmt_bool(cert['dyadic_pressure_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. excess threshold",
        "",
        "上一层给出 `B_C<A_C <=> E_C>F_C-A_C`。本层记",
        "",
        "```text",
        "H_C=F_C-A_C.",
        "```",
        "",
        "因此局部反例要求",
        "",
        "```text",
        "E_C>H_C.",
        "```",
        "",
        "这把支撑不足变成明确的覆盖过量阈值。",
        "",
        "## 2. active product 二分",
        "",
        "令",
        "",
        "```text",
        "R_C={r prime: E_r(C)>0},",
        "M_C=prod_{r in R_C}r.",
        "```",
        "",
        "若 `M_C>width(C)`，同一覆盖相位字的复现周期超过 cell 支撑宽度，必须进入 product-width ColumnCRT/PDEC 或有限原子出口。",
        "若 `M_C<=width(C)`，则所有高覆盖被迫集中在 small-product active set 上。",
        "",
        "## 3. dyadic r 层压力",
        "",
        "按 `Z<r<=2Z` 分解：",
        "",
        "```text",
        "E_C=sum_Z E_Z(C),",
        "M_C=prod_Z M_Z.",
        "```",
        "",
        "若候选允许预算 `U_Z` 满足",
        "",
        "```text",
        "sum_Z U_Z<=H_C",
        "```",
        "",
        "而反例要求 `E_C>H_C`，则存在某个 dyadic 层",
        "",
        "```text",
        "E_Z(C)>U_Z.",
        "```",
        "",
        "这把局部 over-cover 压到一个 dyadic `r` 层。",
        "",
        "## 4. 固定 r 的 lower CRT 单元",
        "",
        "固定 `r` 后，上一层的 cofactor 区间 `n_min<=n<=n_max` 给出",
        "",
        "```text",
        "n=r*m,",
        "m_min=ceil(n_min/r),",
        "m_max=floor(n_max/r).",
        "```",
        "",
        "并保留",
        "",
        "```text",
        "gcd(m,W_<r)=1.",
        "```",
        "",
        "所以过载层变成更低阶 rough-m CRT 支撑问题，而不是原命题的短区间素数存在性。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {EXCESS_THRESHOLD}",
        f"  AND {ACTIVE_PRODUCT}",
        f"  AND {DYADIC_R_PARTITION}",
        f"  AND {OVERFULL_LOCALIZATION}",
        f"  AND {M_INTERVAL}",
        f"  AND {R_LAYER_CRT}",
        f"  AND {SMALL_PRODUCT}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "剩余变成 dyadic r 层过载，或 small-product active cover 的 ColumnCRT/PDEC。",
        "",
        "## 6. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
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
            "- 本证书没有证明 dyadic r 层过载不可能。",
            "- 本证书没有证明 small-product active cover concentration 不可能。",
            "- 本证书只把 cofactor-LPF 覆盖债务压成 product-width 二分和 dyadic r 层压力。",
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
    """生成 JSON、ledger 和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
