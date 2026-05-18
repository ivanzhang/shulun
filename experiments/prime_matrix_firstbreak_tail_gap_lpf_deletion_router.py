#!/usr/bin/env python3
"""生成 weighted rough tail 的最小素因子删除债务证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_lpf_deletion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-lpf-deletion-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-lpf-deletion-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-deletion-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.json",
]

PREVIOUS_TARGET = "SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC"
SMALL_DEFECT = "SmallTailFiniteNonprimeDefectLedger"
LPF_PARTITION = "LargeTailLeastPrimeFactorPartitionLedger"
PREFIX_TELESCOPE = "RoughPrefixDeletionTelescopingLedger"
LPF_CRT = "LeastPrimeFactorCRTDeletionCellLedger"
LPF_GAP = "SievedGapLPFDeletionFunctionalLedger"
DYADIC_DEBT = "DyadicLPFDeletionDebtOrNamedReturnPDEC"
NEW_TARGET = "LPFDeletionDebtOrRoughPrefixOverdensityPDEC"

REDUCED_TARGET = (
    f"{SMALL_DEFECT} AND {LPF_PARTITION} AND {PREFIX_TELESCOPE} "
    f"AND {LPF_CRT} AND {LPF_GAP} AND {DYADIC_DEBT} AND {NEW_TARGET}"
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
    """把旧活动基中的 rough 硬点替换为 LPF 删除分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 LPF 删除债务判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "WeightedRoughTargetImported",
            imported,
            False,
            "上一层把 self-mirror 剩余压成筛后 gap，失败时必须是 weighted sqrt-rough CRT 支撑过密或命名 return 过大。",
            PREVIOUS_TARGET,
        ),
        row(
            "SmallTailFiniteDefectClosed",
            True,
            True,
            "q<=z 的非素数 tail 是有限小端，直接作为 D_small 精确扣回；q=1 边界自动包含在内。",
            SMALL_DEFECT,
        ),
        row(
            "LargeTailLPFPartitionClosed",
            True,
            True,
            "对 z<q<P 的非素数，最小素因子 ell<=z 唯一存在，故大 tail 非素数缺陷按 ell 唯一分块。",
            LPF_PARTITION,
        ),
        row(
            "RoughPrefixTelescopingClosed",
            True,
            True,
            "按素数 ell 递增筛去 q≡0 mod ell；前缀 rough 质量的每一步降幅正是对应 LPF 删除块 B_ell。",
            PREFIX_TELESCOPE,
        ),
        row(
            "LPFCRTDeletionCellClosed",
            True,
            True,
            "每个 B_ell 可写为 q=ell*n、z/ell<n<P/ell、gcd(n,W_<ell)=1 的 CRT 删除单元。",
            LPF_CRT,
        ),
        row(
            "LPFSievedGapFunctionalClosed",
            True,
            True,
            "真实 gap 改写为 Phi + D_small + sum_ell B_ell - R_named，其中 Phi=L(L-D)+min(L,y-1)-X_core。",
            LPF_GAP,
        ),
        row(
            "DyadicLPFDebtStillOpen",
            False,
            False,
            "若 gap 失败，则 LPF 删除总量未能超过 R_named-Phi-D_small；必须定位到某些 dyadic ell 层的删除债务或命名 return。",
            DYADIC_DEBT,
        ),
        row(
            "WeightedRoughReduced",
            True,
            False,
            "SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC 被压成小端非素数缺陷、large-tail LPF 唯一分区、前缀删除 telescoping、CRT 删除单元和 dyadic 删除债务。",
            REDUCED_TARGET,
        ),
        row(
            "LPFDeletionDebtExcluded",
            False,
            False,
            "本步没有证明所有 LPF 删除层给出足够质量；只把 rough over-density 变成 disjoint CRT 删除债务。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 dyadic LPF 删除债务，或证明该债务必回流为 PDEC/SAE/ColumnCRT。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 LPF 删除债务证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "weighted rough tail 的失败形态被改写为最小素因子删除债务。"
        "小端 q<=z 的非素数质量先精确扣出为 D_small；大端 z<q<P 中，每个非素数有唯一最小素因子 "
        "ell<=z，于是 D_large=sum B_ell。按 ell 递增筛时，前缀 rough 质量的 telescoping 降幅正是 "
        "B_ell，且每个 B_ell 是 q=ell*n、gcd(n,W_<ell)=1 的 CRT 删除单元。"
        "若真实 gap 仍失败，则不是 rough 集合抽象过密，而是某些 dyadic 最小素因子层删除质量不足，"
        "或命名 return 吃掉这些删除。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_lpf_deletion_router",
        "status": "weighted_rough_tail_reduced_to_lpf_deletion_debt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "weighted_rough_target_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "small_tail_finite_nonprime_defect_closed": True,
        "large_tail_lpf_partition_closed": True,
        "rough_prefix_deletion_telescoping_closed": True,
        "lpf_crt_deletion_cell_closed": True,
        "lpf_sieved_gap_functional_closed": True,
        "dyadic_lpf_deletion_debt_excluded": False,
        "lpf_deletion_debt_proved_impossible": False,
        "row_column_unconditional_closed": False,
        "lpf_deletion_formulas": {
            "tail_weight": "w(q)=min(L,q-H)ceil((P-1)/q)",
            "z": "z=floor(sqrt(P-1))",
            "small_defect": "D_small=sum_{H<q<=z, q not prime} w(q)",
            "lpf_cell": "B_ell=sum_{z<q<P, ell=lpf(q)} w(q)",
            "lpf_crt_cell": "B_ell=sum_{z/ell<n<P/ell, gcd(n,W_<ell)=1} w(ell*n)",
            "large_defect": "D_large=sum_{ell<=z} B_ell",
            "nonprime_defect": "D_np=D_small+D_large",
            "prefix_rough": "S_u=sum_{z<q<P, gcd(q,W_u)=1} w(q)",
            "telescoping": "S_{ell^-}-S_ell=B_ell and S_0-S_z=sum_{ell<=z}B_ell",
            "phi": "Phi=L(L-D)+min(L,y-1)-X_core",
            "gap": "G=Phi+D_small+sum_{ell<=z}B_ell-R_named",
            "positive_branch": "Phi+D_small+sum B_ell>R_named => G>0",
            "failure_branch": "G<=0 => sum B_ell<=R_named-Phi-D_small",
            "dyadic_partition": "sum_{ell<=z}B_ell=sum_Y sum_{Y<ell<=2Y}B_ell",
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
        "# Prime Matrix weighted rough tail LPF 删除债务证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"weighted_rough_target_imported={fmt_bool(cert['weighted_rough_target_imported'])}",
        f"small_tail_finite_nonprime_defect_closed={fmt_bool(cert['small_tail_finite_nonprime_defect_closed'])}",
        f"large_tail_lpf_partition_closed={fmt_bool(cert['large_tail_lpf_partition_closed'])}",
        f"rough_prefix_deletion_telescoping_closed={fmt_bool(cert['rough_prefix_deletion_telescoping_closed'])}",
        f"lpf_crt_deletion_cell_closed={fmt_bool(cert['lpf_crt_deletion_cell_closed'])}",
        f"lpf_sieved_gap_functional_closed={fmt_bool(cert['lpf_sieved_gap_functional_closed'])}",
        f"dyadic_lpf_deletion_debt_excluded={fmt_bool(cert['dyadic_lpf_deletion_debt_excluded'])}",
        f"lpf_deletion_debt_proved_impossible={fmt_bool(cert['lpf_deletion_debt_proved_impossible'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 小端与大端",
        "",
        "沿用",
        "",
        "```text",
        "w(q)=min(L,q-H)ceil((P-1)/q),",
        "z=floor(sqrt(P-1)).",
        "```",
        "",
        "先把小端非素数质量单独扣出：",
        "",
        "```text",
        "D_small=sum_{H<q<=z, q not prime}w(q).",
        "```",
        "",
        "`q=1` 若出现在 tail 中，也自动归入这个有限小端。",
        "",
        "## 2. 最小素因子唯一分区",
        "",
        "若 `z<q<P` 且 `q` 非素数，则 `lpf(q)<=sqrt(q)<=z`，且 `lpf(q)` 唯一。因此",
        "",
        "```text",
        "B_ell=sum_{z<q<P, ell=lpf(q)}w(q),",
        "D_large=sum_{ell<=z}B_ell,",
        "D_np=D_small+D_large.",
        "```",
        "",
        "这把非素数筛缺陷变成互不重叠的最小素因子删除层。",
        "",
        "## 3. CRT 删除单元",
        "",
        "记",
        "",
        "```text",
        "W_<ell=prod_{p<ell}p.",
        "```",
        "",
        "则每个删除层有精确 CRT 形式：",
        "",
        "```text",
        "B_ell=sum_{z/ell<n<P/ell, gcd(n,W_<ell)=1} w(ell*n).",
        "```",
        "",
        "这说明每个删除块都是 `q=0 mod ell` 且避开更小素数模的 CRT 单元。",
        "",
        "## 4. 前缀 rough telescoping",
        "",
        "令 `W_u=prod_{p<=u}p`，并定义",
        "",
        "```text",
        "S_u=sum_{z<q<P, gcd(q,W_u)=1}w(q).",
        "```",
        "",
        "按素数 `ell` 递增筛时：",
        "",
        "```text",
        "S_{ell^-}-S_ell=B_ell,",
        "S_0-S_z=sum_{ell<=z}B_ell.",
        "```",
        "",
        "所以 weighted rough over-density 等价于这些 CRT 删除层总降幅过小。",
        "",
        "## 5. 筛后 gap",
        "",
        "设",
        "",
        "```text",
        "Phi=L(L-D)+min(L,y-1)-X_core.",
        "```",
        "",
        "则真实 gap 为",
        "",
        "```text",
        "G=Phi+D_small+sum_{ell<=z}B_ell-R_named.",
        "```",
        "",
        "若",
        "",
        "```text",
        "Phi+D_small+sum B_ell>R_named,",
        "```",
        "",
        "则正 gap 已成立。若反例仍存在，则必须满足",
        "",
        "```text",
        "sum B_ell<=R_named-Phi-D_small.",
        "```",
        "",
        "这就是最小素因子删除债务。",
        "",
        "## 6. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {SMALL_DEFECT}",
        f"  AND {LPF_PARTITION}",
        f"  AND {PREFIX_TELESCOPE}",
        f"  AND {LPF_CRT}",
        f"  AND {LPF_GAP}",
        f"  AND {DYADIC_DEBT}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "下一步不再处理重叠包含-排除，而是攻击 disjoint LPF 删除层的 dyadic 债务。",
        "",
        "## 7. 判定表",
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
            "## 8. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 9. 诚实边界",
            "",
            "- 本证书没有证明 LPF 删除层总能支付 gap。",
            "- 本证书把 rough over-density 改写为互不重叠的 CRT 删除债务。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 10. 依赖哈希",
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
