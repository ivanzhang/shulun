#!/usr/bin/env python3
"""生成 square-phase 近全粗骨架 prime-void 二分证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_nearfull_rough_primevoid_dichotomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json

输出：
  docs/monograph/prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json
  docs/monograph/prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-nearfull-rough-primevoid-dichotomy-router.md"

LDG = "LDG-Lower"
RFP = "RFP-Upper"
NEAR_FULL = "PostSquareNearFullRoughSkeletonLowerBound"
LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
RFP_DEFECT = "ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE"
PRIME_INPUT = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"

CG = 0.48
CB = 1.50
P0 = 23

SOURCE_FILES = [
    "prime-matrix-square-phase-dimension-gap-attack-router.json",
    "prime-matrix-square-phase-ldg-lower-direct-attack-router.json",
    "prime-matrix-square-phase-rfp-upper-direct-attack-router.json",
    "prime-matrix-square-phase-ldg-beta-level-barrier-router.json",
    "prime-matrix-diagonal-postsquare-tail-cofactor-identity.md",
    "prime-matrix-diagonal-postsquare-tail-collision-vanishing.md",
    "prime-matrix-diagonal-postsquare-primepair-dimension-gap.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_nearfull_rough_primevoid_dichotomy_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def constant_rows() -> list[dict[str, Any]]:
    """给出常数二分读数。"""
    rows = []
    for p in [23, 101, 1009, 10007, 1000003]:
        log_p = math.log(p)
        rows.append(
            {
                "p": p,
                "log_p": log_p,
                "cb_over_cg": CB / CG,
                "dimension_gap_constant_positive": log_p > CB / CG,
                "rfp_excess_factor_if_prime_void_and_ldg_holds": CG * log_p / CB,
            }
        )
    return rows


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "NearFullRoughExactDecomposition",
            True,
            True,
            "由一尾互补因子恒等式与多尾碰撞消失，P>=23 时 G(P)=PrimeWindow(P)+B(P)。",
            "none",
        ),
        row(
            "PrimeVoidForcesGEqualsB",
            True,
            True,
            "若平方后前半窗无素数，则低筛骨架全由三曲线素对覆盖，故 G(P)=B(P)。",
            "none",
        ),
        row(
            "LDGAndRFPImplyPrime",
            True,
            True,
            f"若 G(P)>={CG}P/logP 且 B(P)<={CB}P/log^2P，logP>{CB/CG:.3f} 时得到 G>B。",
            f"{LDG} AND {RFP}",
        ),
        row(
            "PrimeVoidDefectDichotomy",
            True,
            True,
            "对 P>=23 的反例，必发生 LDG 亏损或 RFP 过密；二者不能同时保持正常。",
            f"{LOW_DEFECT} OR {RFP_DEFECT}",
        ),
        row(
            "NearFullRoughLowerIndependentClosure",
            False,
            False,
            "近全阈值粗骨架下界不是比短区间素数更弱的独立易证对象；反例态下它等价于要求 B(P) 达到一维尺度。",
            f"{NEAR_FULL} OR {LOW_DEFECT}",
        ),
        row(
            "DirectUnconditionalContradictionFound",
            False,
            False,
            "本步给出严格二分和路线校准，尚未排除两个命名缺陷出口。",
            f"exclude {LOW_DEFECT} AND {RFP_DEFECT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到全局无条件闭合。",
            f"{PRIME_INPUT} OR ({LOW_DEFECT} excluded AND {RFP_DEFECT} excluded)",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 prime-void 二分证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_nearfull_rough_primevoid_dichotomy_router",
        "status": "nearfull_rough_exact_primevoid_defect_dichotomy_closed_defect_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "nearfull_rough_exact_decomposition_closed": True,
        "prime_void_forces_g_equals_b": True,
        "ldg_and_rfp_imply_prime_closed": True,
        "prime_void_defect_dichotomy_closed": True,
        "nearfull_rough_lower_independent_closure_proved": False,
        "low_skeleton_defect_excluded": False,
        "reciprocal_floor_primepair_excess_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "constants": {
            "c_g": CG,
            "c_b": CB,
            "c_b_over_c_g": CB / CG,
            "p0": P0,
            "log_p0": math.log(P0),
            "log_p0_exceeds_c_b_over_c_g": math.log(P0) > CB / CG,
        },
        "constant_rows": constant_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": "PrimeVoidDefectExclusion: LowSkeletonDeficitPDECOrSAE OR ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE",
        "plain_conclusion": (
            "本步把 `PostSquareNearFullRoughSkeletonLowerBound` 的真实地位校准清楚："
            "在 `P>=23` 的平方端点，低筛骨架精确等于端点素数集合与三曲线素对覆盖集合的无交并。"
            "因此若假设反例，即 `(P^2,P^2+P)` 无素数，则必有 `G(P)=B(P)`。"
            "常数账本 `c_G=0.48,C_B=1.50` 下，`log(23)>C_B/c_G`，"
            "所以反例不能同时满足 LDG 正常下界与 RFP 正常上界；它必须暴露为"
            "`LowSkeletonDeficit/PDEC/SAE` 或 `ReciprocalFloorPrimePairExcess/TailAnchor/PDEC/SAE`。"
            "这不是最终闭合，因为两个缺陷出口尚未排除；但它切断了把近全 rough 下界当作普通 beta-sieve 余项的误接路线。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    constants = result["constants"]
    lines = [
        "# Prime Matrix square-phase 近全粗骨架 prime-void 二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"nearfull_rough_exact_decomposition_closed={fmt_bool(result['nearfull_rough_exact_decomposition_closed'])}",
        f"prime_void_forces_g_equals_b={fmt_bool(result['prime_void_forces_g_equals_b'])}",
        f"prime_void_defect_dichotomy_closed={fmt_bool(result['prime_void_defect_dichotomy_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确分解",
        "",
        "令 `y=floor(P/e)`，",
        "",
        "```text",
        "G(P)=#{1<=r<P: P^-(P^2+r)>y}",
        "B(P)=#{y<ell<P<m: ell,m prime, P^2<ell*m<P^2+P}",
        "A(P)=#{1<=r<P: P^2+r prime}",
        "```",
        "",
        "对 `P>=23`，已有一尾互补因子恒等式和多尾碰撞消失给出无交分解：",
        "",
        "```text",
        "G(P)=A(P)+B(P).",
        "```",
        "",
        "因此反例 `A(P)=0` 强制 `G(P)=B(P)`。这就是当前反例链与真实结构链的最短接口。",
        "",
        "## 2. 常数二分",
        "",
        f"- `c_G={constants['c_g']}`。",
        f"- `C_B={constants['c_b']}`。",
        f"- `C_B/c_G={constants['c_b_over_c_g']:.6f}`。",
        f"- `log(23)={constants['log_p0']:.6f}`，已经超过 `C_B/c_G`。",
        "",
        "| P | log P | C_B/c_G | logP>C_B/c_G | 反例且LDG正常时的RFP超额因子 |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["constant_rows"]:
        lines.append(
            f"| {item['p']} | {item['log_p']:.6f} | {item['cb_over_cg']:.6f} | "
            f"`{fmt_bool(item['dimension_gap_constant_positive'])}` | "
            f"{item['rfp_excess_factor_if_prime_void_and_ldg_holds']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 反例二分",
            "",
            "若 `P>=23` 且 `A(P)=0`，则 `G(P)=B(P)`。于是：",
            "",
            "```text",
            "若 G(P) >= 0.48 P/logP，",
            "则 B(P) >= 0.48 P/logP",
            "      = (0.48 logP) P/log^2P",
            "      > 1.50 P/log^2P.",
            "```",
            "",
            "所以反例必须落入下面二选一：",
            "",
            "```text",
            "G(P) < 0.48 P/logP        -> LowSkeletonDeficit/PDEC/SAE",
            "B(P) > 1.50 P/log^2P      -> ReciprocalFloorPrimePairExcess/TailAnchor/PDEC/SAE",
            "```",
            "",
            "## 4. 判定表",
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
            "## 5. 下一步",
            "",
            "- 主攻 `LowSkeletonDeficitPDECOrSAE`：证明近全低骨架亏损会产生可排斥的端点相位缺陷，或给出低骨架全局下界。",
            "- 并行攻 `ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE`：证明三曲线素对过密会产生可排斥的尾锚/倒数相位缺陷，或给出 RFP 上界。",
            "- 不再把 `PostSquareNearFullRoughSkeletonLowerBound` 当成普通 `P^0.43` beta-sieve 输入；它已经贴近短区间素数主问题。",
            "",
            "## 6. 依赖哈希",
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
                "prime_void_defect_dichotomy_closed": result["prime_void_defect_dichotomy_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
