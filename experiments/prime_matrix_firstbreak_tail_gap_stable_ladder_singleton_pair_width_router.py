#!/usr/bin/env python3
"""生成 stable ladder singleton/pair 的低纤维与长宽度二分证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_singleton_pair_width_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap"

IMPORT = "StableActualLadderSingletonOrPairPeriodImportedLedger"
SINGLETON_LOW_FIBER = "StableLadderSingletonSurplusLowFiberQuotaLedger"
PAIR_WIDTH = "StableLadderSameCellPairSupportWidthDichotomyLedger"
SHORT_PAIR_KILL = "StableLadderShortSupportPairExclusionLedger"
LONG_PAIR = "StableLadderLongWidthSameCellPeriodPairRegistrationLedger"
NO_ANON = "NoAnonymousSingletonOrPairPeriodExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterSingletonPairWidthLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON_LOW_FIBER} AND {PAIR_WIDTH} AND {SHORT_PAIR_KILL} "
    f"AND {LONG_PAIR} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 singleton/pair 硬点替换成低纤维/长宽度二分。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造低纤维与长宽度判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderSingletonOrPairPeriodImported",
            imported,
            False,
            "上一层把正过载改写为 singleton surplus atom 或同 cell period-pair。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderSingletonSurplusLowFiberQuotaClosed",
            True,
            True,
            "若 M_s=1 且 M_s-L/q_j>=eta>0，则 L<q_j；singleton 只能在低 pivot 纤维中存活。",
            SINGLETON_LOW_FIBER,
        ),
        row(
            "StableLadderSameCellPairSupportWidthDichotomyClosed",
            True,
            True,
            "若同 cell pair 存在，则 n2-n1=tW>=W；因此任一承载支撑直径 H 必满足 H>=W。",
            PAIR_WIDTH,
        ),
        row(
            "StableLadderShortSupportPairExcluded",
            True,
            True,
            "在 H<W 的短支撑分支，同 cell period-pair 不可能存在。",
            SHORT_PAIR_KILL,
        ),
        row(
            "StableLadderLongWidthSameCellPeriodPairRegistered",
            True,
            False,
            "H>=W 的剩余 pair 分支登记为长宽度 same-cell period-pair PDEC/cap。",
            LONG_PAIR,
        ),
        row(
            "NoAnonymousSingletonOrPairPeriodExit",
            True,
            True,
            "singleton/pair 出口被改写为低纤维 singleton 或长宽度 period-pair，不再匿名。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterSingletonPairWidth",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "LowFiberSingletonOrLongWidthPairStillOpen",
            False,
            False,
            "仍未证明低纤维 singleton 全局可求和，也未排斥长宽度 same-cell period-pair。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭低纤维 singleton、长宽度 period-pair 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 singleton/pair 宽度路由证书。"""
    previous = load_json(PREVIOUS_CERT)
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "singleton/pair 出口可继续压缩：若 singleton 分支 M_s=1 仍有正过载，"
        "则 1-L/q_j>0，故固定 pivot 纤维大小 L<q_j；若 pair 分支存在，"
        "同 cell 周期差给出 n2-n1=tW>=W，所以承载支撑直径 H>=W。"
        "因此短支撑 H<W 排斥 pair，剩余只是不匿名的低纤维 singleton 或长宽度 period-pair。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_singleton_pair_width_router",
        "status": "singleton_pair_split_to_low_fiber_or_long_width_pair_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "singleton_pair_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "singleton_low_fiber_quota_closed": True,
        "pair_support_width_dichotomy_closed": True,
        "short_support_pair_excluded": True,
        "long_width_pair_registered": True,
        "anonymous_singleton_or_pair_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "low_fiber_singleton_summability_proved": False,
        "long_width_pair_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "width_formulas": {
            "singleton_positive_surplus": "M_s=1 and M_s-L/q_j>=eta>0 => L<q_j",
            "singleton_integer_quota": "L in Z_{>=0} => L<=q_j-1",
            "same_cell_period": "n2-n1=tW, t in Z_{>=1}, W=lcm_i(q_i)",
            "support_diameter": "H>=n2-n1>=W whenever a same-cell pair is present",
            "short_support_exclusion": "H<W => no same-cell period-pair",
            "long_width_remaining": "H>=W is a named long-width same-cell period-pair PDEC/cap",
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
        "# Prime Matrix stable-ladder singleton/pair width 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"singleton_pair_imported={fmt_bool(cert['singleton_pair_imported'])}",
        f"singleton_low_fiber_quota_closed={fmt_bool(cert['singleton_low_fiber_quota_closed'])}",
        f"pair_support_width_dichotomy_closed={fmt_bool(cert['pair_support_width_dichotomy_closed'])}",
        f"short_support_pair_excluded={fmt_bool(cert['short_support_pair_excluded'])}",
        f"long_width_pair_registered={fmt_bool(cert['long_width_pair_registered'])}",
        f"anonymous_singleton_or_pair_removed={fmt_bool(cert['anonymous_singleton_or_pair_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"low_fiber_singleton_summability_proved={fmt_bool(cert['low_fiber_singleton_summability_proved'])}",
        f"long_width_pair_pdec_cap_proved={fmt_bool(cert['long_width_pair_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. singleton 的低纤维强制",
        "",
        "上一层 singleton 分支满足：",
        "",
        "```text",
        "M_s=1,",
        "M_s-L/q_j>=eta>0.",
        "```",
        "",
        "因此：",
        "",
        "```text",
        "1-L/q_j>0, hence L<q_j.",
        "```",
        "",
        "所以 singleton surplus atom 不能出现在 `L>=q_j` 的高纤维中；它只能作为低 pivot 纤维事件继续登记。",
        "",
        "## 2. pair 的长宽度强制",
        "",
        "同 cell pair 分支给出：",
        "",
        "```text",
        "n2-n1=tW, t>=1, W=lcm_i(q_i).",
        "```",
        "",
        "若承载支撑直径为 `H`，则：",
        "",
        "```text",
        "H>=n2-n1>=W.",
        "```",
        "",
        "因此 `H<W` 的短支撑分支直接排斥同 cell period-pair；只有 `H>=W` 的长宽度分支仍需 PDEC/cap。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 singleton/pair 匿名出口变成低纤维 singleton 或长宽度 same-cell period-pair，外加 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明低纤维 singleton surplus atom 全局可求和。",
            "- 本证书没有证明长宽度 same-cell period-pair PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 singleton/pair 出口改写为低纤维/长宽度二分。",
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
