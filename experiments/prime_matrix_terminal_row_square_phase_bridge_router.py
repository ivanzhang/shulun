#!/usr/bin/env python3
"""把终端行 reduced atom 存在性接到平方相位 Jacobsthal/PDEC 前沿。

用法示例：
  python3 experiments/prime_matrix_terminal_row_square_phase_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json

输出：
  data/prime-matrix-terminal-row-square-phase-bridge-ledger.json
  docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json
  docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

OUT_LEDGER = DATA / "prime-matrix-terminal-row-square-phase-bridge-ledger.json"
OUT_JSON = DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.md"

TERMINAL_ATOM = DOCS / "prime-matrix-terminal-row-crt-atom-router.json"
SQUARE_PM = DOCS / "prime-matrix-prime-square-pm-layered-wheel-alignment-router.json"
SPECIAL_JAC = DOCS / "prime-matrix-square-phase-jacobsthal-special-phase-router.json"
LOCAL_PCRT = DOCS / "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json"
PAGE_SPARSE = DOCS / "prime-matrix-beta-gap-page-sparsity-router.json"

SOURCE_FILES = [
    TERMINAL_ATOM,
    SQUARE_PM,
    SPECIAL_JAC,
    LOCAL_PCRT,
    PAGE_SPARSE,
    DOCS / "claim-status-table.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    PAPER,
]

PREVIOUS_TARGET = "TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer"
NEXT_TARGET = "SquarePhaseSpecialPhaseLongBlockPDECExclusion"
ALT_TARGET = "TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound"
AP_TARGET = "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    primes: list[int] = []
    for value in range(2, n + 1):
        composite = False
        for prime in primes:
            if prime * prime > value:
                break
            if value % prime == 0:
                composite = True
                break
        if not composite:
            primes.append(value)
    return primes


def next_prime_after(n: int) -> int:
    """返回 n 后的下一个素数。"""
    value = n + 1
    while True:
        if all(value % p for p in range(2, int(value ** 0.5) + 1)):
            return value
        value += 1


def covered_by_low_primes(value: int, low_primes: list[int]) -> bool:
    """判断 value 是否被 low_primes 中某个素数整除。"""
    return any(value % p == 0 for p in low_primes)


def sample_square_phase(P: int) -> dict[str, Any]:
    """给出 P 的 plus/minus 终端幸存 r。"""
    low_primes = [p for p in primes_upto(P) if p < P]
    modulus = prod(low_primes)
    plus_survivors: list[dict[str, int]] = []
    minus_survivors: list[dict[str, int]] = []
    plus_covered: list[int] = []
    minus_covered: list[int] = []
    for r in range(1, P):
        plus_n = P * P + r
        minus_n = P * P - r
        if covered_by_low_primes(plus_n, low_primes):
            plus_covered.append(r)
        else:
            plus_survivors.append({"r": r, "n": plus_n, "phase_start": (P * P + 1) % modulus})
        if covered_by_low_primes(minus_n, low_primes):
            minus_covered.append(r)
        else:
            minus_survivors.append({"r": r, "n": minus_n, "phase_start": (P * P - (P - 1)) % modulus})
    p_next = next_prime_after(P)
    return {
        "P": P,
        "low_primes": low_primes,
        "M_below_P": modulus,
        "p_next": p_next,
        "sqrt_gate_upper": p_next * p_next,
        "plus_window": [P * P + 1, P * P + P - 1],
        "minus_window": [P * P - (P - 1), P * P - 1],
        "plus_survivors": plus_survivors,
        "minus_survivors": minus_survivors,
        "plus_full_cover": len(plus_survivors) == 0,
        "minus_full_cover": len(minus_survivors) == 0,
        "plus_full_cover_implies_long_block_start": (P * P + 1) % modulus,
        "minus_full_cover_implies_long_block_start": (P * P - (P - 1)) % modulus,
        "block_length": P - 1,
    }


def rows() -> list[dict[str, Any]]:
    """构造判定表。"""
    return [
        {
            "gate": "TerminalReducedAtomEquivalentToSquarePhaseSurvivor",
            "closed": True,
            "proved": True,
            "meaning": "末行 P^2-r 与下一行 P^2+r 的 reduced atom 存在性等价于 plus/minus 平方相位幸存 r。",
            "remaining": "none for equivalence",
        },
        {
            "gate": "ReducedAtomForcesPrimeBySqrtGate",
            "closed": True,
            "proved": True,
            "meaning": "1<=r<P 时 P^2±r 均小于下一素数平方；若避开所有 q<P，则为素数。",
            "remaining": "none for atom-to-prime",
        },
        {
            "gate": "TerminalFullCoverImpliesSpecialLongBlock",
            "closed": True,
            "proved": True,
            "meaning": "若 plus 或 minus 终端窗口被 q<P 全覆盖，则 P^2 特殊相位启动长度 P-1 的 primorial 覆盖块。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "UniformJacobsthalBoundSuffices",
            "closed": True,
            "proved": False,
            "meaning": "若全周期最大覆盖块长度总小于 P-1 则可闭合，但既有 Jacobsthal 数据显示该强路线已失败。",
            "remaining": "rejected route; use special phase instead",
        },
        {
            "gate": "GlobalSpecialPhaseAvoidanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明 P^2 特殊相位不落入长覆盖块深处，或把命中登记为 PDEC/SAE/ColumnCRT。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosed",
            "closed": False,
            "proved": False,
            "meaning": "本步是接口合流，不是全局无条件闭合。",
            "remaining": f"{NEXT_TARGET} OR {AP_TARGET}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    terminal = load_json(TERMINAL_ATOM)
    square_pm = load_json(SQUARE_PM)
    special = load_json(SPECIAL_JAC)
    samples = [sample_square_phase(5), sample_square_phase(7)]
    return {
        "certificate_type": "prime_matrix_terminal_row_square_phase_bridge_router",
        "status": "terminal_row_localization_routed_to_square_phase_special_jacobsthal_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "alternative_attack_target": ALT_TARGET,
        "ap_zero_packet_fallback": AP_TARGET,
        "imported_terminal_atom_status": terminal.get("status"),
        "imported_square_phase_status": square_pm.get("status"),
        "imported_special_jacobsthal_status": special.get("status"),
        "special_phase_period_bound_failure_count": special.get("period_bound_failure_count"),
        "special_phase_plus_full_cover_count": special.get("plus_full_cover_count"),
        "special_phase_minus_full_cover_count": special.get("minus_full_cover_count"),
        "samples": samples,
        "rows": rows(),
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": (
            "(SquarePhaseSpecialPhaseLongBlockPDECExclusion OR "
            "TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound OR "
            "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier OR "
            "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR "
            "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR "
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND "
            "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND "
            "ExplicitModelGapAndFiniteDPRCLedger AND "
            "RatePreservationLedger_FOR_moving_atom_packet AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "plain_conclusion": (
            "终端行 reduced atom 存在性已经无损并入平方锚 `P^2±r` 特殊相位问题。"
            "末行缺失等价于 minus 窗口 `P^2-(1..P-1)` 被 `q<P` 全覆盖；下一行缺失等价于 plus 窗口 "
            "`P^2+(1..P-1)` 被 `q<P` 全覆盖。任何一侧全覆盖都会使 `P^2` 在 `M_<P` 周期中启动"
            "长度 `P-1` 的低筛覆盖块。普通全周期 Jacobsthal 短块上界已被既有数据否定，"
            "所以最新可攻点不是全周期最大块，而是 `P^2` 特殊相位避让长块，或把该相位命中登记并排斥为 "
            "PDEC/SAE/ColumnCRT。"
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix 终端行到平方相位 Jacobsthal 桥",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_target={result['previous_target']}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"alternative_attack_target={result['alternative_attack_target']}",
        f"ap_zero_packet_fallback={result['ap_zero_packet_fallback']}",
        f"special_phase_period_bound_failure_count={result['special_phase_period_bound_failure_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价公式",
        "",
        "对 `1<=r<P`：",
        "",
        "```text",
        "plus survivor  <=> gcd(P^2+r, M_<P)=1",
        "minus survivor <=> gcd(P^2-r, M_<P)=1",
        "plus full cover  <=> r=-P^2 mod q 的禁类覆盖 r=1..P-1",
        "minus full cover <=> r= P^2 mod q 的禁类覆盖 r=1..P-1",
        "```",
        "",
        "若 plus 或 minus full cover 成立，则从对应平方相位开始出现长度 `P-1` 的 primorial 覆盖块。",
        "",
        "## 2. P=5,7 样本桥接",
        "",
    ]
    for sample in result["samples"]:
        lines += [
            f"### P={sample['P']}",
            "",
            "```text",
            f"M_below_P={sample['M_below_P']}",
            f"plus_window={sample['plus_window']}",
            f"minus_window={sample['minus_window']}",
            f"plus_survivors={sample['plus_survivors']}",
            f"minus_survivors={sample['minus_survivors']}",
            f"plus_full_cover_implies_long_block_start={sample['plus_full_cover_implies_long_block_start']}",
            f"minus_full_cover_implies_long_block_start={sample['minus_full_cover_implies_long_block_start']}",
            "```",
            "",
        ]

    lines += [
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{table_cell(row['gate'])}` | `{fmt_bool(row['closed'])}` | "
            f"`{fmt_bool(row['proved'])}` | {table_cell(row['meaning'])} | "
            f"{table_cell(row['remaining'])} |"
        )

    lines += [
        "",
        "## 4. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明特殊相位避让、PDEC/SAE/ColumnCRT 排斥、点态 AP 零点包界或行/列命题无条件闭合；它只完成接口合流。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "alternative_attack_target": result["alternative_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
