#!/usr/bin/env python3
"""生成 self-mirror tail gap 的筛缺陷路由证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_sieved_defect_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-sieved-defect-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-sieved-defect-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-sieved-defect-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json",
]

PREVIOUS_TARGET = "SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC"
NONPRIME_DEFECT = "PrimeTailNonprimeDefectExactLedger"
ROUGH_IDENTITY = "SqrtRoughPrimeTailIdentityLedger"
PARITY_DEFECT = "EndpointParityNonprimeDefectLowerBoundLedger"
SIEVED_MARGIN = "SievedTailGapMarginFunctionalLedger"
SIEVED_CRITERION = "SievedPositiveGapCriterionLedger"
ROUGH_PDEC = "WeightedRoughTailCRTDefectOrNamedReturnPDEC"
NEW_TARGET = "SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC"

REDUCED_TARGET = (
    f"{NONPRIME_DEFECT} AND {ROUGH_IDENTITY} AND {PARITY_DEFECT} "
    f"AND {SIEVED_MARGIN} AND {SIEVED_CRITERION} AND {ROUGH_PDEC} AND {NEW_TARGET}"
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
    """把旧活动基中的 self-mirror 硬点替换为筛缺陷分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造筛缺陷路由判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "SelfMirrorImported",
            imported,
            False,
            "上一层把 deep-late 剩余压成自镜像 collar，或 quotient core 层/命名 return 吃掉 margin。",
            PREVIOUS_TARGET,
        ),
        row(
            "NonprimeDefectExactClosed",
            True,
            True,
            "对 w(q)=min(L,q-H)ceil((P-1)/q)，有 C_tail=C_all-D_np，其中 D_np 为 H<q<P 的非素数权重总和。",
            NONPRIME_DEFECT,
        ),
        row(
            "SqrtRoughIdentityClosed",
            True,
            True,
            "取 z=floor(sqrt(P-1))、W_z=prod_{ell<=z}ell。q>z 且 q<P 时，gcd(q,W_z)=1 当且仅当 q 为素数。",
            ROUGH_IDENTITY,
        ),
        row(
            "EndpointParityDefectClosed",
            True,
            True,
            "在 self-mirror 分支 L<=D 且 P>3 时，q=P-1 是非素数端点并给出权重 L；任意 q>2 的偶数 regular saturated 槽也给出二重非素数缺陷。",
            PARITY_DEFECT,
        ),
        row(
            "SievedMarginFunctionalClosed",
            True,
            True,
            "late gap 可精确改写为 G=L(L-D)+min(L,y-1)-X_core+D_np-R_named；self-mirror 时 min(L,y-1)=L。",
            SIEVED_MARGIN,
        ),
        row(
            "SievedPositiveCriterionClosed",
            True,
            True,
            "若 L(L-D)+min(L,y-1)-X_core+D_np>R_named，则正 gap 已成立。",
            SIEVED_CRITERION,
        ),
        row(
            "WeightedRoughCRTDefectStillOpen",
            False,
            False,
            "若正 gap 仍失败，则 sqrt-rough 加权 tail 必须几乎吃满整数包络；这才是新的 CRT 全局缺陷/PDEC 接口。",
            ROUGH_PDEC,
        ),
        row(
            "SelfMirrorReduced",
            True,
            False,
            "SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC 被压成素/非素数缺陷恒等式、sqrt-rough 精确素数身份、端点/奇偶 CRT 缺陷、筛后 margin 与 weighted rough PDEC。",
            REDUCED_TARGET,
        ),
        row(
            "SelfMirrorSievedGapProved",
            False,
            False,
            "本步没有证明 D_np 总能超过 X_core 与 R_named 的消耗，只把失败形态变成加权 rough CRT 支撑过密。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 weighted rough tail 的 CRT 过密、并行的 source-rank/strict 前沿和外部谱/模型输入。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造筛缺陷证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "self-mirror/collar 剩余被推进到真实素数 tail 与整数 tail 的精确差额。"
        "令 w(q)=min(L,q-H)ceil((P-1)/q)。整数包络 C_all 与真实 prime tail 的差额正是非素数权重 "
        "D_np，因此 G=G_int+D_np-R_named。取 z=floor(sqrt(P-1)) 后，q>z 的 z-rough 整数与素数等价，"
        "所以失败不再是抽象整数容量问题，而是加权 sqrt-rough CRT 支撑在 tail 窗口内过密，或命名 return 吃掉筛缺陷。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_sieved_defect_router",
        "status": "self_mirror_reduced_to_exact_sieved_tail_gap_or_weighted_rough_crt_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "self_mirror_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "nonprime_defect_exact_closed": True,
        "sqrt_rough_prime_tail_identity_closed": True,
        "endpoint_parity_defect_lower_bound_closed": True,
        "sieved_margin_functional_closed": True,
        "sieved_positive_gap_criterion_closed": True,
        "weighted_rough_crt_defect_excluded": False,
        "self_mirror_sieved_gap_proved": False,
        "row_column_unconditional_closed": False,
        "sieved_defect_formulas": {
            "tail_weight": "w(q)=min(L,q-H)ceil((P-1)/q)",
            "integer_tail": "C_all=sum_{H<q<P} w(q)",
            "prime_tail": "C_tail=sum_{H<q<P, q prime} w(q)",
        "nonprime_defect": "D_np=sum_{H<q<P, q not prime} w(q)=C_all-C_tail",
            "sqrt_cutoff": "z=floor(sqrt(P-1)), W_z=prod_{ell prime, ell<=z} ell",
            "sqrt_rough_identity": "C_tail=sum_{H<q<=z, q prime}w(q)+sum_{z<q<P, gcd(q,W_z)=1}w(q)",
            "late_sieved_gap": "G=L(L-D)+min(L,y-1)-X_core+D_np-R_named",
            "self_mirror_gap": "L<=D => G=L(L-D)+L-X_core+D_np-R_named",
            "positive_branch": "L(L-D)+min(L,y-1)-X_core+D_np>R_named => G>0",
            "failure_branch": "G<=0 => weighted sqrt-rough tail plus R_named saturates the integer envelope",
            "parity_endpoint_defect": "P>3 and L<=D => endpoint q=P-1 contributes D_np>=L",
            "endpoint_plus_regular_even_defect": "D_np>=L+2L*#{even q: max(m+1,H+L,4)<=q<=P-2}",
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
        "# Prime Matrix self-mirror tail gap 筛缺陷证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"self_mirror_imported={fmt_bool(cert['self_mirror_imported'])}",
        f"nonprime_defect_exact_closed={fmt_bool(cert['nonprime_defect_exact_closed'])}",
        f"sqrt_rough_prime_tail_identity_closed={fmt_bool(cert['sqrt_rough_prime_tail_identity_closed'])}",
        f"endpoint_parity_defect_lower_bound_closed={fmt_bool(cert['endpoint_parity_defect_lower_bound_closed'])}",
        f"sieved_margin_functional_closed={fmt_bool(cert['sieved_margin_functional_closed'])}",
        f"sieved_positive_gap_criterion_closed={fmt_bool(cert['sieved_positive_gap_criterion_closed'])}",
        f"weighted_rough_crt_defect_excluded={fmt_bool(cert['weighted_rough_crt_defect_excluded'])}",
        f"self_mirror_sieved_gap_proved={fmt_bool(cert['self_mirror_sieved_gap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. prime tail 与非素数缺陷",
        "",
        "令",
        "",
        "```text",
        "w(q)=min(L,q-H)ceil((P-1)/q),  H<q<P.",
        "```",
        "",
        "则",
        "",
        "```text",
        "C_all=sum_{H<q<P}w(q),",
        "C_tail=sum_{H<q<P, q prime}w(q),",
        "D_np=sum_{H<q<P, q not prime}w(q).",
        "```",
        "",
        "因此有精确恒等式",
        "",
        "```text",
        "C_tail=C_all-D_np.",
        "```",
        "",
        "这一步把整数包络中的虚假容量全部登记为真实的非素数筛缺陷。",
        "",
        "## 2. sqrt-rough 精确身份",
        "",
        "取",
        "",
        "```text",
        "z=floor(sqrt(P-1)),",
        "W_z=prod_{ell prime, ell<=z} ell.",
        "```",
        "",
        "若 `z<q<P`，则",
        "",
        "```text",
        "q prime  <=>  gcd(q,W_z)=1.",
        "```",
        "",
        "所以",
        "",
        "```text",
        "C_tail = sum_{H<q<=z, q prime}w(q)",
        "       + sum_{z<q<P, gcd(q,W_z)=1}w(q).",
        "```",
        "",
        "这把剩余硬点改成 weighted rough CRT 支撑问题。",
        "",
        "## 3. 筛后 margin",
        "",
        "由上一层 late collar 公式",
        "",
        "```text",
        "G_int=L(L-D)+min(L,y-1)-X_core.",
        "```",
        "",
        "加入非素数缺陷后得到真实 gap：",
        "",
        "```text",
        "G=G_int+D_np-R_named",
        " =L(L-D)+min(L,y-1)-X_core+D_np-R_named.",
        "```",
        "",
        "在 self-mirror 分支 `L<=D` 中，`min(L,y-1)=L`，因此",
        "",
        "```text",
        "G=L(L-D)+L-X_core+D_np-R_named.",
        "```",
        "",
        "若",
        "",
        "```text",
        "L(L-D)+min(L,y-1)-X_core+D_np>R_named,",
        "```",
        "",
        "则正 gap 已成立。",
        "",
        "## 4. 端点与奇偶 CRT 非素数缺陷",
        "",
        "在 `P>3` 且 `L<=D` 时，端点 `q=P-1` 是非素数并贡献权重 `L`。此外 regular saturated 区间内的偶数槽给出显式下界：",
        "",
        "```text",
        "D_np >= L + 2L*#{even q: max(m+1,H+L,4)<=q<=P-2}.",
        "```",
        "",
        "这是最小的 mod 2 CRT 缺陷；更高素模量的缺陷由 `W_z` 的 rough 支撑继续承载。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        f"{PREVIOUS_TARGET}",
        f"  -> {NONPRIME_DEFECT}",
        f"  AND {ROUGH_IDENTITY}",
        f"  AND {PARITY_DEFECT}",
        f"  AND {SIEVED_MARGIN}",
        f"  AND {SIEVED_CRITERION}",
        f"  AND {ROUGH_PDEC}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "若失败仍存在，则不是整数 tail 可饱和，而是 sqrt-rough 加权支撑过密或 `R_named` 吃掉筛缺陷。",
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
            "- 本证书没有证明 `D_np` 总能超过 `X_core` 与 `R_named` 的消耗。",
            "- 本证书把失败形态压成 weighted sqrt-rough CRT 支撑过密或命名 return 质量过大。",
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
