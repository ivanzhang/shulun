#!/usr/bin/env python3
"""生成 LPF 删除债务的 dyadic cofactor interval 分解证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_lpf_dyadic_cofactor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json",
]

PREVIOUS_TARGET = "LPFDeletionDebtOrRoughPrefixOverdensityPDEC"
DYADIC_LAYER = "DyadicLPFDeletionLayerPartitionLedger"
LOCALIZATION = "DyadicDebtLocalizationForAnyBudgetVectorLedger"
WEIGHT_SPLIT = "RampSaturatedTailWeightSplitLedger"
QUOTIENT_CELL = "QuotientLayerCofactorIntervalLedger"
COFACTOR_ENDPOINT = "CofactorIntervalEndpointFormulaLedger"
ROUGH_INTERVAL = "RoughCofactorIntervalCRTSupportLedger"
CELL_DEBT = "DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC"
NEW_TARGET = "DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC"

REDUCED_TARGET = (
    f"{DYADIC_LAYER} AND {LOCALIZATION} AND {WEIGHT_SPLIT} "
    f"AND {QUOTIENT_CELL} AND {COFACTOR_ENDPOINT} "
    f"AND {ROUGH_INTERVAL} AND {CELL_DEBT} AND {NEW_TARGET}"
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
    """把旧活动基中的 LPF debt 硬点替换为 dyadic cofactor 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 dyadic cofactor 分解判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "LPFDebtImported",
            imported,
            False,
            "上一层把 weighted rough over-density 压成互不重叠的 LPF 删除债务。",
            PREVIOUS_TARGET,
        ),
        row(
            "DyadicLayerPartitionClosed",
            True,
            True,
            "把 ell 按 Y<ell<=2Y 分层，B_tot=sum_Y B_Y，且层之间互不重叠。",
            DYADIC_LAYER,
        ),
        row(
            "DebtLocalizationClosed",
            True,
            True,
            "若 sum_Y B_Y<=T 而任意候选预算 sum_Y A_Y>T，则至少一层满足 B_Y<A_Y。",
            LOCALIZATION,
        ),
        row(
            "RampSaturatedWeightSplitClosed",
            True,
            True,
            "w(q)=min(L,q-H)ceil((P-1)/q) 精确拆成 H<q<H+L 的 ramp 层与 q>=H+L 的 saturated 层。",
            WEIGHT_SPLIT,
        ),
        row(
            "QuotientCellClosed",
            True,
            True,
            "再按 j=ceil((P-1)/q) 分层；固定 ell、j 后 q=ell*n 把支撑变成一个显式 cofactor 区间。",
            QUOTIENT_CELL,
        ),
        row(
            "CofactorEndpointFormulaClosed",
            True,
            True,
            "令 A=P-1；Q_j 给出 q_min=floor(A/j)+1、q_max=A(j=1) 或 floor(A/(j-1))，再与 tail/ramp/sat 边界相交并除以 ell。",
            COFACTOR_ENDPOINT,
        ),
        row(
            "RoughCofactorIntervalClosed",
            True,
            True,
            "每个 cofactor 区间还带 gcd(n,W_<ell)=1；因此局部债务是短区间 rough-cofactor CRT 支撑问题。",
            ROUGH_INTERVAL,
        ),
        row(
            "CofactorIntervalDebtStillOpen",
            False,
            False,
            "仍未证明每个 dyadic/quotient/cofactor interval 的 rough 支撑给出足够删除质量，或失败必为 ColumnCRT/PDEC。",
            CELL_DEBT,
        ),
        row(
            "LPFDebtReduced",
            True,
            False,
            "LPFDeletionDebtOrRoughPrefixOverdensityPDEC 被压成 dyadic LPF 层、预算定位、权重层、quotient cell、rough cofactor interval 与局部债务。",
            REDUCED_TARGET,
        ),
        row(
            "DyadicCofactorDebtExcluded",
            False,
            False,
            "本步没有排斥 dyadic rough cofactor interval debt，只把它写成更小的局部 CRT 支撑问题。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 dyadic rough cofactor interval debt，或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 dyadic cofactor 分解证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "LPF 删除债务被继续拆成 dyadic 最小素因子层、权重层和 quotient cofactor 区间。"
        "每个 B_ell 先按 ell 的 dyadic 层 B_Y 汇总；若总删除量不足，则相对于任意候选预算向量 "
        "A_Y，至少有一个 dyadic 层短缺。层内再按 ramp/saturated 权重和 j=ceil((P-1)/q) 分块。"
        "固定 ell 与 j 后，q=ell*n 把问题变成带 gcd(n,W_<ell)=1 的短 cofactor 区间 CRT 支撑。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_lpf_dyadic_cofactor_router",
        "status": "lpf_deletion_debt_reduced_to_dyadic_rough_cofactor_interval_debt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "lpf_debt_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "dyadic_layer_partition_closed": True,
        "debt_localization_closed": True,
        "ramp_saturated_weight_split_closed": True,
        "quotient_layer_cofactor_interval_closed": True,
        "rough_cofactor_interval_crt_support_closed": True,
        "cofactor_interval_endpoint_formula_closed": True,
        "dyadic_rough_cofactor_interval_debt_excluded": False,
        "row_column_unconditional_closed": False,
        "dyadic_cofactor_formulas": {
            "B_ell": "B_ell=sum_{z<q<P, ell=lpf(q)}w(q)",
            "dyadic_layer": "B_Y=sum_{Y<ell<=2Y, ell prime}B_ell",
            "total_deletion": "B_tot=sum_Y B_Y",
            "budget_localization": "B_tot<=T<sum_Y A_Y => exists Y with B_Y<A_Y",
            "tail_weight": "w(q)=u(q)v(q), u(q)=min(L,q-H), v(q)=ceil((P-1)/q)",
            "ramp_region": "H<q<H+L => u(q)=q-H",
            "saturated_region": "q>=H+L => u(q)=L",
            "quotient_layer": "Q_j={q: ceil((P-1)/q)=j}",
            "quotient_q_endpoints": "A=P-1; q_j_min=floor(A/j)+1; q_j_max=A if j=1 else floor(A/(j-1))",
            "ramp_q_endpoints": "q_min=max(z+1,H+1,q_j_min), q_max=min(P-1,H+L-1,q_j_max)",
            "saturated_q_endpoints": "q_min=max(z+1,H+L,q_j_min), q_max=min(P-1,q_j_max)",
            "cofactor_integer_endpoints": "n_min=ceil(q_min/ell), n_max=floor(q_max/ell); empty iff n_min>n_max",
            "cofactor_cell": "q=ell*n, n in I_{ell,j,sigma}, gcd(n,W_<ell)=1",
            "cell_sum": "B_{Y,sigma,j}=sum_{Y<ell<=2Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} u(ell n) j",
            "layer_reassembly": "B_Y=sum_{sigma in {ramp,sat}} sum_j B_{Y,sigma,j}",
            "new_failure": "some B_{Y,sigma,j} below its local budget or named return/ColumnCRT",
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
        "# Prime Matrix LPF 删除债务 dyadic cofactor 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lpf_debt_imported={fmt_bool(cert['lpf_debt_imported'])}",
        f"dyadic_layer_partition_closed={fmt_bool(cert['dyadic_layer_partition_closed'])}",
        f"debt_localization_closed={fmt_bool(cert['debt_localization_closed'])}",
        f"ramp_saturated_weight_split_closed={fmt_bool(cert['ramp_saturated_weight_split_closed'])}",
        f"quotient_layer_cofactor_interval_closed={fmt_bool(cert['quotient_layer_cofactor_interval_closed'])}",
        f"cofactor_interval_endpoint_formula_closed={fmt_bool(cert['cofactor_interval_endpoint_formula_closed'])}",
        f"rough_cofactor_interval_crt_support_closed={fmt_bool(cert['rough_cofactor_interval_crt_support_closed'])}",
        f"dyadic_rough_cofactor_interval_debt_excluded={fmt_bool(cert['dyadic_rough_cofactor_interval_debt_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. dyadic LPF 层",
        "",
        "从上一层",
        "",
        "```text",
        "B_ell=sum_{z<q<P, ell=lpf(q)}w(q)",
        "```",
        "",
        "按 dyadic `ell` 层定义",
        "",
        "```text",
        "B_Y=sum_{Y<ell<=2Y, ell prime}B_ell,",
        "B_tot=sum_Y B_Y.",
        "```",
        "",
        "若 `B_tot<=T`，而某个候选预算向量满足 `sum_Y A_Y>T`，则必存在",
        "",
        "```text",
        "B_Y<A_Y.",
        "```",
        "",
        "这把总债务定位到至少一个 dyadic LPF 层。",
        "",
        "## 2. 权重层",
        "",
        "写",
        "",
        "```text",
        "w(q)=u(q)v(q),",
        "u(q)=min(L,q-H),",
        "v(q)=ceil((P-1)/q).",
        "```",
        "",
        "于是",
        "",
        "```text",
        "H<q<H+L  =>  u(q)=q-H,",
        "q>=H+L   =>  u(q)=L.",
        "```",
        "",
        "这给出 ramp 与 saturated 两个互不重叠的权重区域。",
        "",
        "## 3. quotient cofactor 区间",
        "",
        "再按",
        "",
        "```text",
        "Q_j={q: ceil((P-1)/q)=j}",
        "```",
        "",
        "分层。固定 `ell` 与 `j`，写 `q=ell*n`，则 `Q_j` 与 ramp/saturated 条件一起给出一个显式整数区间",
        "",
        "```text",
        "n in I_{ell,j,sigma}.",
        "```",
        "",
        "端点可直接写出。令 `A=P-1`，则",
        "",
        "```text",
        "q_j_min=floor(A/j)+1,",
        "q_j_max=A                     if j=1,",
        "q_j_max=floor(A/(j-1))        if j>=2.",
        "```",
        "",
        "对 ramp 层：",
        "",
        "```text",
        "q_min=max(z+1,H+1,q_j_min),",
        "q_max=min(P-1,H+L-1,q_j_max).",
        "```",
        "",
        "对 saturated 层：",
        "",
        "```text",
        "q_min=max(z+1,H+L,q_j_min),",
        "q_max=min(P-1,q_j_max).",
        "```",
        "",
        "于是固定 `ell` 后",
        "",
        "```text",
        "n_min=ceil(q_min/ell),",
        "n_max=floor(q_max/ell),",
        "I_{ell,j,sigma}=[n_min,n_max]∩Z.",
        "```",
        "",
        "同时 LPF 条件保留为",
        "",
        "```text",
        "gcd(n,W_<ell)=1.",
        "```",
        "",
        "因此局部单元为",
        "",
        "```text",
        "B_{Y,sigma,j}=",
        "sum_{Y<ell<=2Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} u(ell*n)j.",
        "```",
        "",
        "并且精确重组：",
        "",
        "```text",
        "B_Y=sum_{sigma in {ramp,sat}} sum_j B_{Y,sigma,j}.",
        "```",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {DYADIC_LAYER}",
        f"  AND {LOCALIZATION}",
        f"  AND {WEIGHT_SPLIT}",
        f"  AND {QUOTIENT_CELL}",
        f"  AND {COFACTOR_ENDPOINT}",
        f"  AND {ROUGH_INTERVAL}",
        f"  AND {CELL_DEBT}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "剩余不再是全局 LPF 总债务，而是 dyadic/quotient/cofactor interval 的局部 rough CRT 支撑债务。",
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
            "- 本证书没有证明 dyadic rough cofactor interval debt 不可能。",
            "- 本证书只把 LPF 删除债务定位到更小的局部 CRT 单元。",
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
