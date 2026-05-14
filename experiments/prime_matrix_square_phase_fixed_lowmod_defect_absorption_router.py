#!/usr/bin/env python3
"""生成 square-phase 固定低模亏损吸收路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_fixed_lowmod_defect_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.json

输出：
  docs/monograph/prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.json
  docs/monograph/prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.md"

CG = 0.48
MARGIN_C = 0.010
SAMPLE_D = [5, 7, 11, 13, 17, 19, 23, 29, 31]

MOVING_DEFECT = "MovingCutoffNegativeSquarePhaseDefectOrTailSievePDEC"
PHASE_DEFECT = "NegativeSquarePhaseCoveringDefectOrQuadraticCharacterPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json",
    "prime-matrix-square-phase-ldg-mertens-product-margin-router.json",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
]


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    primes: list[int] = []
    for value in range(2, n + 1):
        for prime in primes:
            if prime * prime > value:
                break
            if value % prime == 0:
                break
        else:
            primes.append(value)
            continue
        if any(value % prime == 0 for prime in primes if prime * prime <= value):
            continue
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return primes


def prime_list_upto(n: int) -> list[int]:
    """简单筛法返回素数。"""
    flags = [True] * (n + 1)
    if n >= 0:
        flags[0] = False
    if n >= 1:
        flags[1] = False
    for value in range(2, int(n**0.5) + 1):
        if not flags[value]:
            continue
        for multiple in range(value * value, n + 1, value):
            flags[multiple] = False
    return [idx for idx, is_prime in enumerate(flags) if is_prime]


def primorial_and_phi(d: int) -> tuple[int, int, list[int]]:
    """计算 q<=d 的 primorial 与 Euler phi。"""
    primes = prime_list_upto(d)
    modulus = 1
    phi = 1
    for prime in primes:
        modulus *= prime
        phi *= prime - 1
    return modulus, phi, primes


def threshold_for_fixed_modulus(modulus: int, margin_c: float) -> int:
    """粗略求 M <= margin_c * P/logP 的起始 P。"""
    p = max(3, int(modulus / max(margin_c, 1e-12)))
    while margin_c * p / math.log(p) < modulus:
        p *= 2
    lo = max(3, p // 2)
    hi = p
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if margin_c * mid / math.log(mid) >= modulus:
            hi = mid
        else:
            lo = mid
    return hi


def sample_rows() -> list[dict[str, Any]]:
    """列出固定低模吸收阈值。"""
    rows = []
    for d in SAMPLE_D:
        modulus, phi, primes = primorial_and_phi(d)
        threshold = threshold_for_fixed_modulus(modulus, MARGIN_C)
        rows.append(
            {
                "d": d,
                "primes": primes,
                "modulus": modulus,
                "phi": phi,
                "density": phi / modulus,
                "abs_error_bound": modulus,
                "threshold_for_margin_c": threshold,
            }
        )
    return rows


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_fixed_lowmod_defect_absorption_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FixedLowModPrefixExactCRTCountingClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定 D 时，避开 q<=D 的负平方相位列数等于完整 CRT 周期计数加 O(M_D)。",
            "remaining": "none",
        },
        {
            "gate": "FixedLowModPersistentDefectAbsorbed",
            "closed": True,
            "proved": True,
            "meaning": "对任何固定 D，O(M_D) 误差最终小于任意 cP/logP 级亏损；低范围只能进有限 SAE。",
            "remaining": "finite threshold for chosen D",
        },
        {
            "gate": "MovingCutoffDefectIsNecessary",
            "closed": True,
            "proved": False,
            "meaning": "若 LDG 亏损无限持续，不能归咎于固定低模周期；必须在 D 随 P 增长的 moving cutoff 或尾筛层发生。",
            "remaining": MOVING_DEFECT,
        },
        {
            "gate": "NegativeSquarePhaseDefectExcluded",
            "closed": False,
            "proved": False,
            "meaning": "moving cutoff 负平方相位亏损尚未排斥。",
            "remaining": MOVING_DEFECT,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未排除 LDG moving defect 与 RFP reciprocal-floor defect。",
            "remaining": "moving LDG defect + RFP defect",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造固定低模吸收证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_fixed_lowmod_defect_absorption_router",
        "status": "fixed_lowmod_prefix_defect_absorbed_moving_cutoff_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "fixed_lowmod_prefix_exact_crt_counting_closed": True,
        "fixed_lowmod_persistent_defect_absorbed": True,
        "moving_cutoff_defect_is_necessary": True,
        "negative_square_phase_defect_excluded": False,
        "row_column_unconditional_closed": False,
        "margin_c_used_for_threshold_table": MARGIN_C,
        "sample_rows": sample_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": MOVING_DEFECT,
        "plain_conclusion": (
            "固定低模前缀不能是 LDG 持续亏损的终端来源。"
            "对任意固定 cutoff D，设 M_D=prod_{q<=D}q，则避开全部 `-P^2 mod q` 的列数"
            "是 `floor((P-1)/M_D)phi(M_D)+O(M_D)`，因此固定前缀偏差为 O(M_D)。"
            "任何 `P/logP` 级持续亏损最终都必须来自随 P 增长的 moving cutoff 或尾筛层，"
            "而不是某个固定 CRT 周期。该 moving defect 尚未排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase 固定低模亏损吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_lowmod_prefix_exact_crt_counting_closed={fmt_bool(result['fixed_lowmod_prefix_exact_crt_counting_closed'])}",
        f"fixed_lowmod_persistent_defect_absorbed={fmt_bool(result['fixed_lowmod_persistent_defect_absorbed'])}",
        f"moving_cutoff_defect_is_necessary={fmt_bool(result['moving_cutoff_defect_is_necessary'])}",
        f"negative_square_phase_defect_excluded={fmt_bool(result['negative_square_phase_defect_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定低模精确计数",
        "",
        "固定 `D`，记",
        "",
        "```text",
        "M_D = prod_{q<=D} q,",
        "H_D(P) = #{1<=k<P: k != -P^2 mod q for every q<=D}.",
        "```",
        "",
        "每个完整 `M_D` 周期内恰有 `phi(M_D)` 个允许列，故",
        "",
        "```text",
        "H_D(P)=floor((P-1)/M_D) phi(M_D)+E_D(P), |E_D(P)|<=M_D.",
        "```",
        "",
        "这说明固定低模只产生有界周期误差；若出现 `P/logP` 级持续亏损，必然不是固定周期相位可解释的。",
        "",
        "## 2. 样本阈值",
        "",
        f"下表用保守余量尺度 `{MARGIN_C} P/logP` 比较固定周期误差 `M_D`。",
        "",
        "| D | primes<=D | M_D | phi(M_D)/M_D | error bound | threshold for M_D<=cP/logP |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in result["sample_rows"]:
        lines.append(
            f"| {item['d']} | `{item['primes']}` | {item['modulus']} | "
            f"{item['density']:.12f} | {item['abs_error_bound']} | "
            f"{item['threshold_for_margin_c']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            f"- 主攻 `{MOVING_DEFECT}`：证明随 `P` 增长的负平方相位 moving cutoff 亏损不可能持续，或把它登记为可排斥 PDEC/SAE。",
            "- 固定低模分支已经不是无限尾段硬点；低范围阈值以下只能作为有限 SAE 处理。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "fixed_lowmod_persistent_defect_absorbed": result["fixed_lowmod_persistent_defect_absorbed"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
