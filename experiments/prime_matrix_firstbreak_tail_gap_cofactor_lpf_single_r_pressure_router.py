#!/usr/bin/env python3
"""生成 cofactor-LPF dyadic pressure 的 single-r pressure 证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_single_r_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json",
]

PREVIOUS_TARGET = "DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC"
CARDINALITY = "ActivePrimeCardinalityFromProductLedger"
SMALL_Z = "SmallZFiniteAtomBoundaryLedger"
SINGLE_R = "SingleCofactorPrimePressureLocalizationLedger"
ELL_PARTITION = "FixedRSourceEllPartitionLedger"
PAIR_CELL = "FixedREllRoughMCRTCellLedger"
PAIR_PRODUCT = "FixedPairProductWidthColumnCRTExitLedger"
SMALL_PRODUCT = "SingleRSmallProductPressurePDEC"
NEW_TARGET = "SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC"

REDUCED_TARGET = (
    f"{CARDINALITY} AND {SMALL_Z} AND {SINGLE_R} AND {ELL_PARTITION} "
    f"AND {PAIR_CELL} AND {PAIR_PRODUCT} AND {SMALL_PRODUCT} AND {NEW_TARGET}"
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
    """把旧活动基中的 dyadic pressure 硬点替换为 single-r 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 single-r pressure 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "DyadicPressureImported",
            imported,
            False,
            "上一层把 cofactor-LPF 覆盖债务压成 dyadic r 层过载或 small-product ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "ActiveCardinalityClosed",
            True,
            True,
            "在 dyadic 层 Z<r<=2Z 且 Z>=2 中，若活动乘积 M_Z<=W_C，则活动素因子个数 a_Z 受 K_Z=floor(log W_C/log Z) 控制。",
            CARDINALITY,
        ),
        row(
            "SmallZBoundaryClosed",
            True,
            True,
            "Z<2 的最低 cofactor prime 层只含有限小素因子，单独登记为有限原子边界。",
            SMALL_Z,
        ),
        row(
            "SingleRPressureClosed",
            True,
            True,
            "若 E_Z>U_Z 且 a_Z<=K_Z，则某个活动 r 满足 E_r>U_Z/K_Z。",
            SINGLE_R,
        ),
        row(
            "FixedREllPartitionClosed",
            True,
            True,
            "固定 r 后，E_r=sum_{ell in Y, ell>r}E_{r<-ell}；若 E_r 超预算，则至少一个 ell 源层超预算。",
            ELL_PARTITION,
        ),
        row(
            "FixedPairMCRTCellClosed",
            True,
            True,
            "固定 r 与 ell 后，q=ell*r*m，m 位于显式短区间且 gcd(m,W_<r)=1。",
            PAIR_CELL,
        ),
        row(
            "FixedPairProductWidthClosed",
            True,
            True,
            "固定 pair 的相位字若需要多个 residual primes，则其 product-width 超过 m 支撑时进入 ColumnCRT/PDEC。",
            PAIR_PRODUCT,
        ),
        row(
            "SingleRSmallProductStillOpen",
            False,
            False,
            "仍未排除单个 r 或固定 pair 的高压力；本步只把 small-product 层压力压到 single-r/fixed-pair 单元。",
            SMALL_PRODUCT,
        ),
        row(
            "DyadicPressureReduced",
            True,
            False,
            "DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC 被压成 active cardinality、single-r pressure、fixed-pair rough-m CRT 与 product-width 出口。",
            REDUCED_TARGET,
        ),
        row(
            "SingleRPressureExcluded",
            False,
            False,
            "本步没有证明 single-r/fixed-pair pressure 不可能。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 single-r/fixed-pair rough-m pressure 或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 single-r pressure 分解证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "dyadic r 层过载在 small-product 分支中不能继续保持为层总量。"
        "若活动乘积不超过 cell 支撑宽度，活动素因子个数受到对数界控制；"
        "总层压力超标时，必须有单个 r 承担超过平均阈值的压力。"
        "固定 r 后再按源 ell 分区，最终得到固定 (r,ell) 的 rough-m CRT 单元。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_cofactor_lpf_single_r_pressure_router",
        "status": "dyadic_cofactor_lpf_pressure_reduced_to_single_r_fixed_pair_pressure_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "dyadic_pressure_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "active_prime_cardinality_closed": True,
        "small_z_finite_atom_boundary_closed": True,
        "single_r_pressure_localization_closed": True,
        "fixed_r_source_ell_partition_closed": True,
        "fixed_r_ell_rough_m_crt_cell_closed": True,
        "fixed_pair_product_width_closed": True,
        "single_r_pressure_excluded": False,
        "row_column_unconditional_closed": False,
        "single_r_formulas": {
            "active_layer": "R_Z(C)={r: Z<r<=2Z, E_r(C)>0}",
            "active_product": "M_Z=prod_{r in R_Z(C)}r",
            "cardinality_bound": "for Z>=2, M_Z<=W_C and r>Z => |R_Z(C)|<=K_Z=floor(log W_C/log Z)",
            "small_z_boundary": "Z<2 is a finite small-prime atom boundary",
            "single_r_pigeonhole": "E_Z(C)>U_Z and |R_Z(C)|<=K_Z => exists r with E_r(C)>U_Z/K_Z",
            "fixed_r_partition": "E_r(C)=sum_{ell in Y, ell>r}E_{r<-ell}(C)",
            "ell_pigeonhole": "E_r>V_r and sum_ell V_{r,ell}<=V_r => exists ell with E_{r<-ell}>V_{r,ell}",
            "fixed_pair_cell": "q=ell*r*m, m_min=ceil(n_min/r), m_max=floor(n_max/r), gcd(m,W_<r)=1",
            "fixed_pair_weight": "alpha_{ell,r*m}=j*u(ell*r*m)",
            "new_failure": "single-r/fixed-pair rough-m pressure or fixed-pair ColumnCRT/PDEC",
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
        "# Prime Matrix cofactor-LPF single-r pressure 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"dyadic_pressure_imported={fmt_bool(cert['dyadic_pressure_imported'])}",
        f"active_prime_cardinality_closed={fmt_bool(cert['active_prime_cardinality_closed'])}",
        "small_z_finite_atom_boundary_closed=true",
        f"single_r_pressure_localization_closed={fmt_bool(cert['single_r_pressure_localization_closed'])}",
        f"fixed_r_source_ell_partition_closed={fmt_bool(cert['fixed_r_source_ell_partition_closed'])}",
        f"fixed_r_ell_rough_m_crt_cell_closed={fmt_bool(cert['fixed_r_ell_rough_m_crt_cell_closed'])}",
        f"fixed_pair_product_width_closed={fmt_bool(cert['fixed_pair_product_width_closed'])}",
        f"single_r_pressure_excluded={fmt_bool(cert['single_r_pressure_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. small-product 给出活动个数界",
        "",
        "在 dyadic 层 `Z<r<=2Z` 中，活动集合为",
        "",
        "```text",
        "R_Z(C)={r: Z<r<=2Z, E_r(C)>0}.",
        "```",
        "",
        "`Z<2` 的最低层作为有限小素因子原子边界单独登记。以下取 `Z>=2`。若仍处于 small-product 分支",
        "",
        "```text",
        "M_Z=prod_{r in R_Z(C)}r <= W_C=width(C),",
        "```",
        "",
        "而每个活动 `r>Z`，则",
        "",
        "```text",
        "|R_Z(C)| <= K_Z=floor(log W_C/log Z).",
        "```",
        "",
        "这把 small-product 分支转成活动素因子个数有限的压力问题。",
        "",
        "## 2. single-r 压力定位",
        "",
        "若 dyadic 层超预算",
        "",
        "```text",
        "E_Z(C)>U_Z,",
        "```",
        "",
        "且 `|R_Z(C)|<=K_Z`，则必有某个活动素因子",
        "",
        "```text",
        "E_r(C)>U_Z/K_Z.",
        "```",
        "",
        "因此反例不能只停留在 dyadic 总层，必须落到单个 `r`。",
        "",
        "## 3. 固定 r 到固定 (r,ell)",
        "",
        "固定 `r` 后按源 `ell` 分区：",
        "",
        "```text",
        "E_r(C)=sum_{ell in Y, ell>r}E_{r<-ell}(C).",
        "```",
        "",
        "若单个 `r` 仍超预算，则同样存在固定 `ell` 源层超预算。该 pair 的单元为",
        "",
        "```text",
        "q=ell*r*m,",
        "m_min=ceil(n_min/r),",
        "m_max=floor(n_max/r),",
        "gcd(m,W_<r)=1.",
        "```",
        "",
        "权重为",
        "",
        "```text",
        "alpha_{ell,r*m}=j*u(ell*r*m).",
        "```",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {CARDINALITY}",
        f"  AND {SMALL_Z}",
        f"  AND {SINGLE_R}",
        f"  AND {ELL_PARTITION}",
        f"  AND {PAIR_CELL}",
        f"  AND {PAIR_PRODUCT}",
        f"  AND {SMALL_PRODUCT}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "剩余变成 single-r/fixed-pair rough-m pressure，或 fixed-pair ColumnCRT/PDEC。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 single-r/fixed-pair pressure 不可能。",
            "- 本证书只把 small-product dyadic 压力压成单个 `r` 与固定 `(r,ell)` 单元。",
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
