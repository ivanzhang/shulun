#!/usr/bin/env python3
"""生成 dyadic cofactor rough 支撑债务的 cofactor-LPF 覆盖证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_cover_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.json",
]

PREVIOUS_TARGET = "DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC"
WEIGHTED_ENVELOPE = "CofactorCellWeightedEnvelopeLedger"
SUPPORT_QUOTA = "RoughSupportQuotaCriterionLedger"
LPF_PARTITION = "CofactorLeastPrimeFactorPartitionLedger"
LPF_CRT_CELL = "CofactorLPFCRTCellLedger"
PRODUCT_WIDTH = "CofactorCoverPrimeProductWidthLedger"
LOCAL_COVER_DEBT = "LocalCofactorLPFCoverDebtOrFiniteAtomPDEC"
NEW_TARGET = "CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC"

REDUCED_TARGET = (
    f"{WEIGHTED_ENVELOPE} AND {SUPPORT_QUOTA} AND {LPF_PARTITION} "
    f"AND {LPF_CRT_CELL} AND {PRODUCT_WIDTH} AND {LOCAL_COVER_DEBT} "
    f"AND {NEW_TARGET}"
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
    """把旧活动基中的 cofactor rough debt 硬点替换为 cofactor-LPF 覆盖分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 cofactor-LPF 覆盖分解判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "DyadicCofactorDebtImported",
            imported,
            False,
            "上一层把 LPF 删除债务定位到 dyadic/quotient/cofactor interval 的 rough 支撑债务。",
            PREVIOUS_TARGET,
        ),
        row(
            "WeightedEnvelopeClosed",
            True,
            True,
            "对每个 cofactor cell 写出全整数权重包络 F_C、rough 支撑质量 B_C 与被小因子删除质量 E_C=F_C-B_C。",
            WEIGHTED_ENVELOPE,
        ),
        row(
            "SupportQuotaCriterionClosed",
            True,
            True,
            "若目标预算为 A_C，则 B_C<A_C 等价于 E_C>F_C-A_C；局部支撑债务变成 cofactor 小因子过覆盖。",
            SUPPORT_QUOTA,
        ),
        row(
            "CofactorLPFPartitionClosed",
            True,
            True,
            "对 gcd(n,W_<ell)>1 的 cofactor，按 r=lpf(n)<ell 作互不重叠分区。",
            LPF_PARTITION,
        ),
        row(
            "CofactorLPFCRTCellClosed",
            True,
            True,
            "每个 r 层写成 n=r*m 且 gcd(m,W_<r)=1 的短区间 CRT 单元。",
            LPF_CRT_CELL,
        ),
        row(
            "ProductWidthDichotomyClosed",
            True,
            True,
            "若一个局部覆盖族使用 distinct primes R，则其完整相位字周期为 M_R=prod R；M_R 超过支撑宽度时只能作为有限原子或 ColumnCRT/PDEC 复现。",
            PRODUCT_WIDTH,
        ),
        row(
            "LocalCoverDebtStillOpen",
            False,
            False,
            "仍未排除 cofactor-LPF 过覆盖本身；本步只把 rough 支撑不足改写为更低素因子的显式覆盖债务。",
            LOCAL_COVER_DEBT,
        ),
        row(
            "CofactorRoughDebtReduced",
            True,
            False,
            "DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC 被压成局部权重包络、quota、cofactor-LPF 分区、CRT cell 与 product-width 出口。",
            REDUCED_TARGET,
        ),
        row(
            "ProductWidthColumnCRTExcluded",
            False,
            False,
            "本步没有证明 product-width/ColumnCRT 出口不可能。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 cofactor-LPF 覆盖债务或证明其必回流为有限原子、ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 cofactor-LPF 覆盖分解证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "dyadic rough cofactor interval 的不足不再只作为支撑下界黑箱保留。"
        "对每个 cell 先写全整数权重包络 F_C 与 rough 支撑 B_C；若 B_C 低于预算 A_C，"
        "则被小 cofactor 因子删除的 E_C=F_C-B_C 必超过 F_C-A_C。"
        "再按 cofactor 的最小素因子 r=lpf(n)<ell 分区，得到 disjoint 的短区间 CRT 覆盖债务。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_cofactor_lpf_cover_router",
        "status": "dyadic_rough_cofactor_debt_reduced_to_local_cofactor_lpf_cover_debt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "dyadic_cofactor_debt_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "weighted_envelope_closed": True,
        "support_quota_criterion_closed": True,
        "cofactor_lpf_partition_closed": True,
        "cofactor_lpf_crt_cell_closed": True,
        "product_width_dichotomy_closed": True,
        "local_cofactor_lpf_cover_debt_excluded": False,
        "row_column_unconditional_closed": False,
        "cofactor_cover_formulas": {
            "cell_weight": "alpha_{ell,n}=j*u(ell*n)",
            "integer_envelope": "F_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}} alpha_{ell,n}",
            "rough_support": "B_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} alpha_{ell,n}",
            "deleted_mass": "E_C=F_C-B_C",
            "quota_defect": "B_C<A_C <=> E_C>F_C-A_C",
            "cofactor_lpf_partition": "E_C=sum_{ell in Y} sum_{r<ell} E_{r<-ell}",
            "cofactor_lpf_cell": "E_{r<-ell}=sum_{n in I_{ell,j,sigma}, r=lpf(n)} alpha_{ell,n}",
            "crt_form": "n=r*m, gcd(m,W_<r)=1, m in ceil(I/r)..floor(I/r)",
            "participating_prime_product": "M_R=prod_{r in R_C} r",
            "product_width_exit": "M_R>width(C) forces exact replay to be finite-atom/ColumnCRT rather than local-period drift",
            "new_failure": "local cofactor-LPF cover debt or product-width ColumnCRT/PDEC",
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
        "# Prime Matrix cofactor-LPF 覆盖债务证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"dyadic_cofactor_debt_imported={fmt_bool(cert['dyadic_cofactor_debt_imported'])}",
        f"weighted_envelope_closed={fmt_bool(cert['weighted_envelope_closed'])}",
        f"support_quota_criterion_closed={fmt_bool(cert['support_quota_criterion_closed'])}",
        f"cofactor_lpf_partition_closed={fmt_bool(cert['cofactor_lpf_partition_closed'])}",
        f"cofactor_lpf_crt_cell_closed={fmt_bool(cert['cofactor_lpf_crt_cell_closed'])}",
        f"product_width_dichotomy_closed={fmt_bool(cert['product_width_dichotomy_closed'])}",
        f"local_cofactor_lpf_cover_debt_excluded={fmt_bool(cert['local_cofactor_lpf_cover_debt_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. cell 权重包络",
        "",
        "固定上一层的 dyadic/quotient/cofactor cell `C=(Y,sigma,j)`。写",
        "",
        "```text",
        "alpha_{ell,n}=j*u(ell*n).",
        "```",
        "",
        "全整数包络、rough 支撑与删除质量为",
        "",
        "```text",
        "F_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}} alpha_{ell,n},",
        "B_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} alpha_{ell,n},",
        "E_C=F_C-B_C.",
        "```",
        "",
        "若局部预算为 `A_C`，则",
        "",
        "```text",
        "B_C<A_C  <=>  E_C>F_C-A_C.",
        "```",
        "",
        "因此 rough 支撑债务等价于 cofactor 小素因子过覆盖债务。",
        "",
        "## 2. cofactor LPF 分区",
        "",
        "对被删除的 cofactor，按",
        "",
        "```text",
        "r=lpf(n)<ell",
        "```",
        "",
        "作互不重叠分区：",
        "",
        "```text",
        "E_C=sum_{ell in Y} sum_{r<ell} E_{r<-ell},",
        "E_{r<-ell}=sum_{n in I_{ell,j,sigma}, r=lpf(n)} alpha_{ell,n}.",
        "```",
        "",
        "每个层又有 CRT 形式",
        "",
        "```text",
        "n=r*m,",
        "gcd(m,W_<r)=1,",
        "ceil(n_min/r)<=m<=floor(n_max/r).",
        "```",
        "",
        "这一步只使用整数的最小素因子唯一性，不使用短区间素数存在性。",
        "",
        "## 3. product-width 出口",
        "",
        "若某个局部覆盖债务使用 distinct cofactor primes `R_C`，定义",
        "",
        "```text",
        "M_R=prod_{r in R_C}r.",
        "```",
        "",
        "完整相位字以 `M_R` 为周期。若 `M_R` 超过该 cell 的支撑宽度，则同一覆盖字不能由局部短周期漂移稳定复现；",
        "它必须登记为有限原子、ColumnCRT/PDEC，或转入更深的 moving-support 出口。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {WEIGHTED_ENVELOPE}",
        f"  AND {SUPPORT_QUOTA}",
        f"  AND {LPF_PARTITION}",
        f"  AND {LPF_CRT_CELL}",
        f"  AND {PRODUCT_WIDTH}",
        f"  AND {LOCAL_COVER_DEBT}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "剩余不再是未解析的 rough 支撑不足，而是 cofactor 最小素因子覆盖过量或 product-width ColumnCRT/PDEC。",
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
            "- 本证书没有证明 cofactor-LPF 过覆盖不可能。",
            "- 本证书只把局部 rough 支撑不足改写为更低素因子的显式 CRT 覆盖债务。",
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
