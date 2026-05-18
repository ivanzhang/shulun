#!/usr/bin/env python3
"""生成 stable ladder positive-surplus 的整数占位二分证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_occupancy_dichotomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap"

IMPORT = "StableActualLadderPositiveResidueSurplusImportedLedger"
INTEGER = "StableLadderOverloadedCellIntegerOccupancyLedger"
DICHOTOMY = "StableLadderPositiveSurplusSingletonOrPairDichotomyLedger"
SINGLETON = "StableLadderSingletonSurplusAtomRegistrationLedger"
PAIR = "StableLadderSameCellPairCongruenceLedger"
PERIOD = "StableLadderSameCellPairPeriodMultipleLedger"
NO_ANON = "NoAnonymousPositiveResidueSurplusExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterOccupancyDichotomyLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {INTEGER} AND {DICHOTOMY} AND {SINGLETON} "
    f"AND {PAIR} AND {PERIOD} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 positive-surplus 硬点替换成整数占位二分。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造整数占位二分判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderPositiveResidueSurplusImported",
            imported,
            False,
            "上一层把有符号余数计数偏差统一转成固定纤维内的正余数过载。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderOverloadedCellIntegerOccupancyClosed",
            True,
            True,
            "过载余数类的占位数 M_s 是非负整数，且 M_s-L/q_j>=eta>0 强制 M_s>=1。",
            INTEGER,
        ),
        row(
            "StableLadderPositiveSurplusSingletonOrPairDichotomyClosed",
            True,
            True,
            "整数占位满足 M_s=1 或 M_s>=2；两者穷尽所有正过载可能。",
            DICHOTOMY,
        ),
        row(
            "StableLadderSingletonSurplusAtomRegistered",
            True,
            False,
            "M_s=1 分支登记为 singleton surplus atom；本步不证明其全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderSameCellPairCongruenceClosed",
            True,
            True,
            "M_s>=2 分支给出同一完整 stable-ladder cell 中两点 n1<n2。",
            PAIR,
        ),
        row(
            "StableLadderSameCellPairPeriodMultipleClosed",
            True,
            True,
            "同一完整 cell 中两点满足 n2-n1 被 W=lcm(q_i) 整除；若有短宽度上界 H<W，可立即排斥该 pair。",
            PERIOD,
        ),
        row(
            "NoAnonymousPositiveResidueSurplusExit",
            True,
            True,
            "正余数过载出口被改写成 singleton atom 或同 cell period-pair 出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterOccupancyDichotomy",
            True,
            False,
            "非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "StableActualLadderSingletonSurplusOrCellPairPeriodPDECCapStillOpen",
            False,
            False,
            "仍未证明 singleton surplus atom 全局可求和，也未排斥同 cell period-pair/PDEC。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需给出 singleton/cell-pair cap，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable ladder occupancy dichotomy 证书。"""
    previous = load_json(PREVIOUS_CERT)
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "positive residue-surplus 可转成完整 stable-ladder cell 的整数占位二分。"
        "设过载余数类占位 M_s 满足 M_s-L/q_j>=eta>0，则 M_s>=1。"
        "若 M_s=1，登记为 singleton surplus atom；若 M_s>=2，则同一完整 cell 内存在两点，"
        "它们在所有 ladder 坐标上同余，因此差值被 W=lcm_i(q_i) 整除。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_occupancy_dichotomy_router",
        "status": "positive_surplus_reduced_to_singleton_or_same_cell_pair_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "positive_surplus_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "integer_occupancy_closed": True,
        "singleton_or_pair_dichotomy_closed": True,
        "singleton_surplus_atom_registered": True,
        "same_cell_pair_congruence_closed": True,
        "same_cell_pair_period_multiple_closed": True,
        "anonymous_positive_surplus_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "singleton_surplus_sae_summability_proved": False,
        "same_cell_pair_period_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "occupancy_formulas": {
            "positive_surplus": "M_s-L/q_j>=eta, eta=E_a(S)/((N-1)(q_j-1))",
            "integer_floor": "M_s in Z_{\u003e=0} and eta>0 => M_s>=1",
            "dichotomy": "M_s=1 OR M_s>=2",
            "singleton_branch": "M_s=1 is a singleton surplus atom",
            "pair_branch": "M_s>=2 => exists n1<n2 in the same full stable-ladder cell",
            "period_modulus": "W=lcm_i(q_i)",
            "same_cell_period": "n2-n1 is a nonzero multiple of W",
            "short_width_exclusion": "if ambient support width H<W, same-cell pair is impossible",
            "new_failure": "singleton surplus SAE or same-cell period-pair PDEC cap",
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
        "# Prime Matrix stable-ladder occupancy-dichotomy 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"positive_surplus_imported={fmt_bool(cert['positive_surplus_imported'])}",
        f"integer_occupancy_closed={fmt_bool(cert['integer_occupancy_closed'])}",
        f"singleton_or_pair_dichotomy_closed={fmt_bool(cert['singleton_or_pair_dichotomy_closed'])}",
        f"singleton_surplus_atom_registered={fmt_bool(cert['singleton_surplus_atom_registered'])}",
        f"same_cell_pair_congruence_closed={fmt_bool(cert['same_cell_pair_congruence_closed'])}",
        f"same_cell_pair_period_multiple_closed={fmt_bool(cert['same_cell_pair_period_multiple_closed'])}",
        f"anonymous_positive_surplus_removed={fmt_bool(cert['anonymous_positive_surplus_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"singleton_surplus_sae_summability_proved={fmt_bool(cert['singleton_surplus_sae_summability_proved'])}",
        f"same_cell_pair_period_pdec_cap_proved={fmt_bool(cert['same_cell_pair_period_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 整数占位",
        "",
        "上一层给出固定补坐标纤维和 pivot 余数类中的正过载：",
        "",
        "```text",
        "M_s-L/q_j>=eta,",
        "eta=E_a(S)/((N-1)(q_j-1))>0.",
        "```",
        "",
        "由于 `M_s` 是非负整数，故必有：",
        "",
        "```text",
        "M_s>=1.",
        "```",
        "",
        "## 2. singleton/pair 二分",
        "",
        "整数占位只有两个出口：",
        "",
        "```text",
        "M_s=1  OR  M_s>=2.",
        "```",
        "",
        "`M_s=1` 登记为 singleton surplus atom；本步不证明其全局求和。",
        "",
        "若 `M_s>=2`，则同一完整 stable-ladder cell 中有两个不同点 `n1<n2`。",
        "",
        "## 3. 同 cell 周期差约束",
        "",
        "同一完整 cell 表示两点在所有 stable ladder 坐标上同余。令：",
        "",
        "```text",
        "W=lcm_i(q_i).",
        "```",
        "",
        "则：",
        "",
        "```text",
        "n2-n1 is a nonzero multiple of W.",
        "```",
        "",
        "因此若某个上游支撑宽度界 `H<W` 已可用，则 pair 分支立即被排斥；否则它成为显式 same-cell period-pair PDEC/cap 输入。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 positive residue-surplus PDEC cap 变成 singleton surplus atom 或 same-cell period-pair cap，外加 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 singleton surplus atom 全局可求和。",
            "- 本证书没有证明 same-cell period-pair PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把正余数过载改写为整数占位的 singleton/pair 二分。",
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
