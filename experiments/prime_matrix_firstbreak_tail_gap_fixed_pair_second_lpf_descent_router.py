#!/usr/bin/env python3
"""生成 fixed-pair rough-m pressure 的二级 LPF 递降证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_fixed_pair_second_lpf_descent_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json",
]

PREVIOUS_TARGET = "SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC"
PAIR_IMPORT = "FixedPairPressureImportedLedger"
M_DESCENT = "FixedPairMSupportStrictDescentLedger"
M_ONE = "MEqualsOneFiniteAtomLedger"
SECOND_LPF = "SecondCofactorLeastPrimeFactorPartitionLedger"
SECOND_CRT = "SecondLPFRoughTCRTCellLedger"
SECOND_PRODUCT = "SecondLPFProductWidthColumnCRTExitLedger"
NO_CYCLE = "ResidualSupportWidthStrictDecreaseNoCycleLedger"
NEW_TARGET = "SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC"

REDUCED_TARGET = (
    f"{PAIR_IMPORT} AND {M_DESCENT} AND {M_ONE} AND {SECOND_LPF} "
    f"AND {SECOND_CRT} AND {SECOND_PRODUCT} AND {NO_CYCLE} AND {NEW_TARGET}"
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
    """把旧活动基中的 fixed-pair pressure 硬点替换为二级 LPF 递降分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造二级 LPF 递降判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "FixedPairPressureImported",
            imported,
            False,
            "上一层把 small-product dyadic 压力压到 single-r/fixed-pair rough-m pressure。",
            PREVIOUS_TARGET,
        ),
        row(
            "MSupportStrictDescentClosed",
            True,
            True,
            "固定 (r,ell) 后 q=ell*r*m；非有限分支 r>=2，二级分解后的 t 支撑宽度至多 ceil(width_m/r)，严格小于原 m 支撑或进入有限原子。",
            M_DESCENT,
        ),
        row(
            "MEqualsOneFiniteAtomClosed",
            True,
            True,
            "m=1 是固定 q=ell*r 的单点有限原子，不能支撑无限复现压力。",
            M_ONE,
        ),
        row(
            "SecondLPFPartitionClosed",
            True,
            True,
            "对 m>1 且 gcd(m,W_<r)=1，令 s=lpf(m)>=r；按 s 作互不重叠的二级 LPF 分区。",
            SECOND_LPF,
        ),
        row(
            "SecondLPFCRTCellClosed",
            True,
            True,
            "固定 s 后 m=s*t，且 gcd(t,W_<s)=1，得到更低支撑的 rough-t CRT 单元。",
            SECOND_CRT,
        ),
        row(
            "SecondProductWidthClosed",
            True,
            True,
            "活动 residual primes S 的乘积若超过 m 支撑宽度，则同一二级相位字只能作为 ColumnCRT/PDEC 或有限原子复现。",
            SECOND_PRODUCT,
        ),
        row(
            "StrictNoCycleClosed",
            True,
            True,
            "每次二级 LPF 递降都把活动支撑宽度至少除以 r>=2；无限循环只能撞到 width<=1 的有限原子。",
            NO_CYCLE,
        ),
        row(
            "SecondLPFPressureStillOpen",
            False,
            False,
            "仍未排除二级 LPF/triple rough-t pressure；本步只证明它是严格下降的固定三元单元或 ColumnCRT/PDEC。",
            NEW_TARGET,
        ),
        row(
            "FixedPairPressureReduced",
            True,
            False,
            "SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC 被压成固定 pair 导入、m 支撑严格下降、二级 LPF 分区、rough-t CRT 与 no-cycle 出口。",
            REDUCED_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥二级 LPF/triple pressure 或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造二级 LPF 递降证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "fixed-pair rough-m pressure 被继续拆成严格下降的二级 LPF 单元。"
        "在固定 (r,ell) 中，q=ell*r*m 且 gcd(m,W_<r)=1。m=1 是有限原子；"
        "m>1 时令 s=lpf(m)>=r，得到 m=s*t 与 gcd(t,W_<s)=1。"
        "由于非有限分支 r>=2，t 的支撑宽度严格小于 m 的支撑宽度，不能形成同尺度循环。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_fixed_pair_second_lpf_descent_router",
        "status": "fixed_pair_pressure_reduced_to_strict_second_lpf_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "fixed_pair_pressure_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "m_support_strict_descent_closed": True,
        "m_equals_one_finite_atom_closed": True,
        "second_lpf_partition_closed": True,
        "second_lpf_crt_cell_closed": True,
        "second_product_width_closed": True,
        "strict_no_cycle_closed": True,
        "second_lpf_pressure_excluded": False,
        "row_column_unconditional_closed": False,
        "second_lpf_formulas": {
            "fixed_pair_cell": "q=ell*r*m, m_min<=m<=m_max, gcd(m,W_<r)=1",
            "weight": "beta_m=j*u(ell*r*m)",
            "unit_atom": "m=1 gives q=ell*r finite atom",
            "second_lpf": "m>1, s=lpf(m)>=r",
            "second_partition": "E_{r<-ell}=E_{m=1}+sum_{s>=r}E_{s<-r,ell}",
            "second_crt": "m=s*t, gcd(t,W_<s)=1",
            "t_endpoints": "t_min=ceil(m_min/s), t_max=floor(m_max/s)",
            "support_descent": "width_t<=ceil(width_m/s)<=ceil(width_m/r); r>=2 gives strict descent unless width_m<=1",
            "active_second_product": "M_S=prod_{s in S} s",
            "product_width_exit": "M_S>width_m => second-level ColumnCRT/PDEC or finite atom",
            "new_failure": "second LPF/triple rough-t pressure or ColumnCRT/PDEC",
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
        "# Prime Matrix fixed-pair second-LPF descent 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"fixed_pair_pressure_imported={fmt_bool(cert['fixed_pair_pressure_imported'])}",
        f"m_support_strict_descent_closed={fmt_bool(cert['m_support_strict_descent_closed'])}",
        f"m_equals_one_finite_atom_closed={fmt_bool(cert['m_equals_one_finite_atom_closed'])}",
        f"second_lpf_partition_closed={fmt_bool(cert['second_lpf_partition_closed'])}",
        f"second_lpf_crt_cell_closed={fmt_bool(cert['second_lpf_crt_cell_closed'])}",
        f"second_product_width_closed={fmt_bool(cert['second_product_width_closed'])}",
        f"strict_no_cycle_closed={fmt_bool(cert['strict_no_cycle_closed'])}",
        f"second_lpf_pressure_excluded={fmt_bool(cert['second_lpf_pressure_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定 pair 的 m 单元",
        "",
        "上一层把压力压到固定 `(r,ell)`：",
        "",
        "```text",
        "q=ell*r*m,",
        "m_min<=m<=m_max,",
        "gcd(m,W_<r)=1,",
        "beta_m=j*u(ell*r*m).",
        "```",
        "",
        "`m=1` 只给出单点 `q=ell*r`，登记为有限原子。",
        "",
        "## 2. 二级 LPF 分区",
        "",
        "对 `m>1`，由 `gcd(m,W_<r)=1` 得",
        "",
        "```text",
        "s=lpf(m)>=r.",
        "```",
        "",
        "于是",
        "",
        "```text",
        "m=s*t,",
        "gcd(t,W_<s)=1,",
        "t_min=ceil(m_min/s),",
        "t_max=floor(m_max/s).",
        "```",
        "",
        "并有互不重叠分区：",
        "",
        "```text",
        "E_{r<-ell}=E_{m=1}+sum_{s>=r}E_{s<-r,ell}.",
        "```",
        "",
        "## 3. 严格下降 no-cycle",
        "",
        "记 `width_m=m_max-m_min+1`。固定 `s` 后：",
        "",
        "```text",
        "width_t<=ceil(width_m/s)<=ceil(width_m/r).",
        "```",
        "",
        "非有限分支已有 `r>=2`。因此若 `width_m>1`，递降后的支撑宽度严格变小；若 `width_m<=1`，直接进入有限原子。",
        "这给出非循环证书：二级 LPF 递降不能在同一支撑尺度上闭环。",
        "",
        "## 4. product-width 出口",
        "",
        "若二级活动素因子集合为 `S`，定义",
        "",
        "```text",
        "M_S=prod_{s in S}s.",
        "```",
        "",
        "若 `M_S>width_m`，二级相位字的复现周期超过原 m 支撑宽度，只能登记为 ColumnCRT/PDEC 或有限原子。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {PAIR_IMPORT}",
        f"  AND {M_DESCENT}",
        f"  AND {M_ONE}",
        f"  AND {SECOND_LPF}",
        f"  AND {SECOND_CRT}",
        f"  AND {SECOND_PRODUCT}",
        f"  AND {NO_CYCLE}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "剩余变成二级 LPF/triple rough-t pressure，或二级 product-width ColumnCRT/PDEC。",
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
            "- 本证书没有证明二级 LPF/triple pressure 不可能。",
            "- 本证书只证明 fixed-pair pressure 若继续下钻，必须严格降低支撑尺度或进入 ColumnCRT/PDEC/有限原子。",
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
