#!/usr/bin/env python3
"""生成 stable ladder residue-count PDEC 的正余数过载证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_positive_surplus_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap"

IMPORT = "StableActualLadderResidueCountPDECImportedLedger"
SIGNED = "StableLadderResidueDeviationSignDichotomyLedger"
ZERO_SUM = "StableLadderResidueDeviationZeroSumTransferLedger"
SURPLUS = "StableLadderPositiveResidueSurplusLocalizationLedger"
THRESHOLD = "StableLadderPositiveResidueSurplusThresholdLedger"
NO_ANON = "NoAnonymousSignedResidueImbalanceExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPositiveSurplusLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {SIGNED} AND {ZERO_SUM} AND {SURPLUS} "
    f"AND {THRESHOLD} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
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
    """把旧活动基中的 residue-count 硬点替换成正过载分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造正余数过载 PDEC 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderResidueCountPDECImported",
            imported,
            False,
            "上一层把 primitive fiber 角色相关改写为固定纤维内单余数类绝对计数偏差。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderResidueDeviationSignDichotomyClosed",
            True,
            True,
            "若 |D_r|>=delta，则要么 D_r>=delta，要么 D_r<=-delta。",
            SIGNED,
        ),
        row(
            "StableLadderResidueDeviationZeroSumTransferClosed",
            True,
            True,
            "当 D_r<=-delta 时，由 sum_s D_s=0 得 sum_{s!=r}D_s>=delta。",
            ZERO_SUM,
        ),
        row(
            "StableLadderPositiveResidueSurplusLocalizationClosed",
            True,
            True,
            "由鸽巢原理，若其他 q_j-1 个余数类总盈余至少 delta，则某个余数类正偏差至少 delta/(q_j-1)。",
            SURPLUS,
        ),
        row(
            "StableLadderPositiveResidueSurplusThresholdClosed",
            True,
            True,
            "取 delta=E/(N-1)，得到某个余数类满足 M_s-L/q_j>=E/((N-1)(q_j-1))。",
            THRESHOLD,
        ),
        row(
            "NoAnonymousSignedResidueImbalanceExit",
            True,
            True,
            "绝对计数偏差出口被改写成正向余数过载出口，亏损分支由零和转移到盈余分支。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPositiveSurplus",
            True,
            False,
            "非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "StableActualLadderPositiveResidueSurplusPDECCapStillOpen",
            False,
            False,
            "仍未证明所有固定纤维余数类正过载都低于阈值，也未证明 sparse scale-ladder SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需给出 positive residue-surplus PDEC cap，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable ladder positive-surplus PDEC 证书。"""
    previous = load_json(PREVIOUS_CERT)
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "residue-count 绝对偏差可由零和偏差向量转成正余数过载。"
        "若某个 D_r=M_r-L/q_j 满足 |D_r|>=delta，则正分支直接给出 D_r>=delta；"
        "负分支 D_r<=-delta 时，其他余数类总盈余至少 delta，故某个余数类正偏差至少 delta/(q_j-1)。"
        "代入 delta=E_a(S)/(N-1)，得到正过载阈值 E_a(S)/((N-1)(q_j-1))。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_positive_surplus_pdec_router",
        "status": "residue_count_imbalance_reduced_to_positive_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "residue_count_pdec_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "sign_dichotomy_closed": True,
        "zero_sum_transfer_closed": True,
        "positive_surplus_localization_closed": True,
        "positive_surplus_threshold_closed": True,
        "anonymous_signed_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "positive_surplus_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "positive_surplus_formulas": {
            "deviation": "D_r=M_r-L/q_j, sum_r D_r=0",
            "absolute_threshold": "|D_r|>=delta, delta=E_a(S)/(N-1)",
            "positive_branch": "D_r>=delta => positive surplus with threshold delta",
            "negative_branch": "D_r<=-delta => sum_{s!=r} D_s>=delta",
            "pigeonhole": "exists s!=r with D_s>=delta/(q_j-1)",
            "surplus_threshold": "exists s with M_s-L/q_j>=E_a(S)/((N-1)(q_j-1))",
            "new_failure": "positive residue-surplus PDEC cap or sparse scale-ladder SAE summability",
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
        "# Prime Matrix stable-ladder positive-surplus PDEC 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"residue_count_pdec_imported={fmt_bool(cert['residue_count_pdec_imported'])}",
        f"sign_dichotomy_closed={fmt_bool(cert['sign_dichotomy_closed'])}",
        f"zero_sum_transfer_closed={fmt_bool(cert['zero_sum_transfer_closed'])}",
        f"positive_surplus_localization_closed={fmt_bool(cert['positive_surplus_localization_closed'])}",
        f"positive_surplus_threshold_closed={fmt_bool(cert['positive_surplus_threshold_closed'])}",
        f"anonymous_signed_imbalance_removed={fmt_bool(cert['anonymous_signed_imbalance_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"positive_surplus_pdec_cap_proved={fmt_bool(cert['positive_surplus_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 偏差符号二分",
        "",
        "沿用上一层固定纤维内的偏差向量：",
        "",
        "```text",
        "D_r=M_r-L/q_j,",
        "sum_r D_r=0.",
        "```",
        "",
        "上一层给出某个余数 `r` 的绝对偏差阈值：",
        "",
        "```text",
        "|D_r|>=delta,",
        "delta=E_a(S)/(N-1).",
        "```",
        "",
        "若 `D_r>=delta`，则已经得到正余数过载。",
        "",
        "## 2. 亏损到盈余的零和转移",
        "",
        "若 `D_r<=-delta`，则：",
        "",
        "```text",
        "sum_{s!=r}D_s=-D_r>=delta.",
        "```",
        "",
        "共有 `q_j-1` 个其他余数类，因此鸽巢原理给出某个 `s!=r` 满足：",
        "",
        "```text",
        "D_s>=delta/(q_j-1).",
        "```",
        "",
        "代入 `delta=E_a(S)/(N-1)` 得到统一正过载阈值：",
        "",
        "```text",
        "M_s-L/q_j>=E_a(S)/((N-1)(q_j-1)).",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从有符号 residue-count 偏差变成 positive residue-surplus PDEC cap，或 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书没有证明 positive residue-surplus PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把有符号余数计数偏差改写为正余数过载输入。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 7. 依赖哈希",
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
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
