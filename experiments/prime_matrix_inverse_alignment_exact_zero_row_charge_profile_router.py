#!/usr/bin/env python3
"""生成逆元对齐零行精确解集与兄弟收费剖面证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_exact_zero_row_charge_profile_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json

输出：
  data/inverse-alignment-exact-zero-row-charge-profile-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json
  docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.md"
OUT_LEDGER = DATA / "inverse-alignment-exact-zero-row-charge-profile-ledger.json"

SOURCE_LEDGER = DATA / "inverse-alignment-covering-system-sample-ledger.json"
SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-covering-system-router.json",
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json",
    DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
    DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json",
    DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
]

SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
SIBLING_LEDGER = "CanonicalColdWindowSiblingChargingOrHotReturnLedger"
SHORT_INTERVAL = "PrimeGapBelowP2ForAllPBlocks"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_exact_zero_row_charge_profile_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    if OUT_LEDGER.exists():
        result[str(OUT_LEDGER.relative_to(ROOT))] = sha256(OUT_LEDGER)
    if SOURCE_LEDGER.exists():
        result[str(SOURCE_LEDGER.relative_to(ROOT))] = sha256(SOURCE_LEDGER)
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_upto(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
    return [i for i, ok in enumerate(sieve) if ok]


def inverse_phase(P: int, x: int, q: int) -> int:
    """计算 q 对行 x 的覆盖相位 rho_q(x)。"""
    return (-x * P) % q


def positive_residue(residue: int, q: int) -> int:
    """把模 q 相位转成 [1,q] 中的列代表。"""
    return q if residue == 0 else residue


def mu_for_phase(P: int, residue: int, q: int) -> int:
    """计算 1<=c<P 中落在给定相位的列数。"""
    first = positive_residue(residue, q)
    if first > P - 1:
        return 0
    return 1 + (P - 1 - first) // q


def covering_profile(P: int, x: int) -> dict[str, Any]:
    """计算一行的精确覆盖、容量和重叠剖面。"""
    qs = primes_upto(P - 1)
    phases = {q: inverse_phase(P, x, q) for q in qs}
    mu_by_q = {q: mu_for_phase(P, phases[q], q) for q in qs}
    covering_qs_by_c: dict[int, list[int]] = {}
    for c in range(1, P):
        hits = [q for q in qs if c % q == phases[q]]
        covering_qs_by_c[c] = hits

    uncovered = [c for c, hits in covering_qs_by_c.items() if not hits]
    multiplicities = {c: len(hits) for c, hits in covering_qs_by_c.items()}
    total_capacity = sum(mu_by_q.values())
    total_hits = sum(multiplicities.values())
    overlap_debt = sum(max(0, value - 1) for value in multiplicities.values())
    capacity_identity_ok = total_capacity == total_hits
    zero_row_identity_ok = bool(uncovered) or total_capacity == (P - 1) + overlap_debt
    first_factor_counter = Counter()
    for hits in covering_qs_by_c.values():
        if hits:
            first_factor_counter[min(hits)] += 1

    return {
        "P": P,
        "x": x,
        "zero_row": not uncovered,
        "uncovered_columns": uncovered,
        "phase_rows": [
            {
                "q": q,
                "rho_q": phases[q],
                "positive_representative": positive_residue(phases[q], q),
                "mu_q": mu_by_q[q],
            }
            for q in qs
        ],
        "total_capacity_sum_mu": total_capacity,
        "total_column_hits": total_hits,
        "overlap_debt": overlap_debt,
        "capacity_identity_ok": capacity_identity_ok,
        "zero_row_capacity_identity_ok": zero_row_identity_ok,
        "max_column_multiplicity": max(multiplicities.values()) if multiplicities else 0,
        "multiplicity_histogram": dict(sorted(Counter(multiplicities.values()).items())),
        "first_factor_histogram": dict(sorted(first_factor_counter.items())),
    }


def prefix_tau_profile(P: int, x: int, z: int) -> dict[str, Any]:
    """计算 prefix 残洞和 tau 兄弟收费剖面。"""
    qs = primes_upto(P - 1)
    phases = {q: inverse_phase(P, x, q) for q in qs}
    mu_by_q = {q: mu_for_phase(P, phases[q], q) for q in qs}
    small = [q for q in qs if q <= z]
    large = [q for q in qs if q > z]
    residual_columns: list[int] = []
    tau_by_c: dict[int, int] = {}
    for c in range(1, P):
        if any(c % q == phases[q] for q in small):
            continue
        residual_columns.append(c)
        hit = next((q for q in large if c % q == phases[q]), None)
        if hit is not None:
            tau_by_c[c] = hit

    tau_counts = Counter(tau_by_c.values())
    msharp = sum(count / mu_by_q[q] for q, count in tau_counts.items() if mu_by_q[q])
    assigned_atoms = sum(tau_counts.values())
    appeared_capacity = sum(mu_by_q[q] for q in tau_counts)
    suffix_capacity = sum(mu_by_q[q] for q in large)
    charged_slack = appeared_capacity - assigned_atoms
    unappeared_suffix_capacity = suffix_capacity - appeared_capacity
    all_labeled = len(tau_by_c) == len(residual_columns)
    assigned_le_mu = all(tau_counts[q] <= mu_by_q[q] for q in tau_counts)
    return {
        "z": z,
        "R_xz_size": len(residual_columns),
        "all_residual_columns_labeled": all_labeled,
        "tau_counts": dict(sorted(tau_counts.items())),
        "Msharp_exact": msharp,
        "assigned_atoms": assigned_atoms,
        "appeared_tau_capacity_sum_mu": appeared_capacity,
        "suffix_capacity_sum_mu": suffix_capacity,
        "charged_slack_for_appeared_tau": charged_slack,
        "unappeared_suffix_capacity": unappeared_suffix_capacity,
        "assigned_atoms_le_mu_for_each_tau": assigned_le_mu,
        "prefix_tau_charge_identity_ok": all_labeled and assigned_le_mu,
    }


def canonical_z_values(P: int) -> list[int]:
    """给出同参数和低层样本 z。"""
    candidates = {3, 5, int(P**0.43), int(math.isqrt(P))}
    return sorted(z for z in candidates if 2 <= z < P)


def build_profile_ledger() -> dict[str, Any]:
    """从既有逆元覆盖 ledger 中生成精确收费剖面。"""
    source = load_json(SOURCE_LEDGER)
    rows: list[dict[str, Any]] = []
    for item in source.get("rows", []):
        P = int(item["P"])
        x = item.get("minimal_alignment_x_in_bound")
        if x is None:
            continue
        x = int(x)
        if P > 43:
            continue
        cover = covering_profile(P, x)
        prefix_rows = [prefix_tau_profile(P, x, z) for z in canonical_z_values(P)]
        rows.append(
            {
                "P": P,
                "minimal_alignment_x": x,
                "x_over_P": x / P,
                "x_le_P": x <= P,
                "covering_profile": cover,
                "prefix_tau_profiles": prefix_rows,
            }
        )

    exact_identity_ok = all(row["covering_profile"]["capacity_identity_ok"] for row in rows)
    zero_identity_ok = all(row["covering_profile"]["zero_row_capacity_identity_ok"] for row in rows)
    tau_identity_ok = all(
        profile["prefix_tau_charge_identity_ok"]
        for row in rows
        for profile in row["prefix_tau_profiles"]
    )
    return {
        "ledger_type": "inverse_alignment_exact_zero_row_charge_profile_ledger",
        "source_ledger": str(SOURCE_LEDGER.relative_to(ROOT)),
        "diagnostic_only": True,
        "profile_rows": rows,
        "all_capacity_identities_ok": exact_identity_ok,
        "all_zero_row_capacity_identities_ok": zero_identity_ok,
        "all_prefix_tau_charge_identities_ok": tau_identity_ok,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合的恒等式和边界。"""
    return [
        {
            "name": "exact_phase_solution_set",
            "statement": "for fixed P,x, every q<P contributes one phase rho_q(x)=-xP mod q.",
            "status": "closed",
        },
        {
            "name": "capacity_hit_identity",
            "statement": "sum_{q<P} mu_q(x;P)=sum_{1<=c<P} #{q<P: c=rho_q(x) mod q}.",
            "status": "closed",
        },
        {
            "name": "zero_row_overlap_identity",
            "statement": "if x is a zero row, sum_q mu_q=(P-1)+overlap_debt(x).",
            "status": "closed",
        },
        {
            "name": "prefix_tau_sibling_identity",
            "statement": "for z<P, R_{x,z} is partitioned by tau_z(c); each tau bucket has size <= mu_tau.",
            "status": "closed",
        },
        {
            "name": "sibling_numeric_envelope",
            "statement": "a uniform parent-level bound for all exact tau/cold sibling families.",
            "status": "open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ExactZeroRowSolutionProfileClosed",
            "closed": result["exact_zero_row_solution_profile_closed"],
            "proved": result["exact_zero_row_solution_profile_closed"],
            "meaning": "具体 P 的零行行号 x 可由逆元 CRT 覆盖系统给出，并生成完整相位剖面。",
            "remaining": "uniform proof, not sample computation",
        },
        {
            "gate": "CapacityOverlapIdentityClosed",
            "closed": result["capacity_overlap_identity_closed"],
            "proved": result["capacity_overlap_identity_closed"],
            "meaning": "任何零行都必须把总覆盖容量分解为 P-1 个实际列加重叠债。",
            "remaining": "convert overlap debt into hot/fixed/PDEC returns globally",
        },
        {
            "gate": "PrefixTauSiblingChargeIdentityClosed",
            "closed": result["prefix_tau_sibling_charge_identity_closed"],
            "proved": result["prefix_tau_sibling_charge_identity_closed"],
            "meaning": "prefix residual 的 tau 兄弟桶与 mu_tau 容量完全同字段匹配。",
            "remaining": SIBLING_NUMERIC,
        },
        {
            "gate": "DirectEarlyZeroRowContradictionFound",
            "closed": False,
            "proved": False,
            "meaning": "精确解集给出强诊断，但尚未从有限样本或恒等式推出全局反例不存在。",
            "remaining": f"{SIBLING_NUMERIC} OR {SHORT_INTERVAL}",
        },
        {
            "gate": "SiblingColdCoreNumericEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需同参数证明父级兄弟预算支配所有精确 tau/cold 兄弟收费。",
            "remaining": SIBLING_NUMERIC,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未同时完成冷兄弟数值 envelope、持久 moving atom 和 DStructure/Rankin 验收。",
            "remaining": f"{SIBLING_NUMERIC} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result(ledger: dict[str, Any]) -> dict[str, Any]:
    """构造证书对象。"""
    sibling = load_json(DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json")
    exact_closed = bool(ledger["profile_rows"]) and all(
        row["covering_profile"]["zero_row"] for row in ledger["profile_rows"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_exact_zero_row_charge_profile_router",
        "status": "exact_inverse_alignment_zero_row_charge_profile_closed_sibling_numeric_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sibling_charging_ledger_imported": sibling.get(
            "canonical_cold_window_sibling_charging_ledger_closed"
        )
        is True,
        "exact_zero_row_solution_profile_closed": exact_closed,
        "capacity_overlap_identity_closed": ledger["all_capacity_identities_ok"]
        and ledger["all_zero_row_capacity_identities_ok"],
        "prefix_tau_sibling_charge_identity_closed": ledger["all_prefix_tau_charge_identities_ok"],
        "direct_unconditional_contradiction_found": False,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SIBLING_NUMERIC,
        "hardpoint_after_router": f"ExactInverseAlignmentSiblingChargeUniformEnvelope OR {SHORT_INTERVAL}",
        "next_direct_attack_target": "ExactInverseAlignmentSiblingChargeUniformEnvelope",
        "parallel_attack_targets": [
            SIBLING_NUMERIC,
            SHORT_INTERVAL,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "theorem_rows": theorem_rows(),
        "ledger": ledger,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逆元方程组现在已转成可复核的零行收费剖面：给定假设零行 x，"
            "每个小素数 q 给出唯一相位 rho_q(x)，容量 mu_q 与实际列命中数满足精确恒等式。"
            "若 x 是零行，则总容量必分解为 P-1 个被覆盖列加 overlap_debt；prefix 残洞再由 "
            "tau_z(c) 分桶，每个桶的原始容量正是同一 mu_tau。这说明许多冷兄弟窗口不能当作"
            "无来源的抽象分叉，它们必须来自同一行相位源和同一容量/重叠账本。"
            "但这一步仍只关闭了解集与收费恒等式；要形成全局矛盾，还需证明这些精确 tau/cold "
            "兄弟收费在同参数下有统一父级 envelope，或者直接证明 x<P 的最小对齐解不可能存在。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix 逆元零行精确收费剖面路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_zero_row_solution_profile_closed={fmt_bool(result['exact_zero_row_solution_profile_closed'])}",
        f"capacity_overlap_identity_closed={fmt_bool(result['capacity_overlap_identity_closed'])}",
        f"prefix_tau_sibling_charge_identity_closed={fmt_bool(result['prefix_tau_sibling_charge_identity_closed'])}",
        f"sibling_cold_core_threshold_numeric_envelope_proved={fmt_bool(result['sibling_cold_core_threshold_numeric_envelope_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 恒等式",
        "",
        "| name | statement | status |",
        "| --- | --- | --- |",
    ]
    for row in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["statement"]),
                    f"`{table_cell(row['status'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 最小零行收费样本",
            "",
            "| P | min x | x/P | sum mu | overlap debt | max multiplicity | first-factor histogram |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["ledger"]["profile_rows"]:
        profile = row["covering_profile"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["P"]),
                    str(row["minimal_alignment_x"]),
                    f"{row['x_over_P']:.3f}",
                    str(profile["total_capacity_sum_mu"]),
                    str(profile["overlap_debt"]),
                    str(profile["max_column_multiplicity"]),
                    f"`{table_cell(profile['first_factor_histogram'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. Prefix Tau 兄弟剖面",
            "",
            "| P | x | z | R_xz size | M# | tau counts | appeared capacity | charged slack |",
            "| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for row in result["ledger"]["profile_rows"]:
        for profile in row["prefix_tau_profiles"]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["P"]),
                        str(row["minimal_alignment_x"]),
                        str(profile["z"]),
                        str(profile["R_xz_size"]),
                        f"{profile['Msharp_exact']:.6f}",
                        f"`{table_cell(profile['tau_counts'])}`",
                        str(profile["appeared_tau_capacity_sum_mu"]),
                        str(profile["charged_slack_for_appeared_tau"]),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")
    lines.extend(
        [
            "",
            "审稿边界：本步不使用真实零行缺席，不声明全局 `min x>P`，也不声明行/列命题无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    ledger = build_profile_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result = build_result(ledger)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
