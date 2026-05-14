#!/usr/bin/env python3
"""生成素数基点能否突破 1/2 指数障碍的审查证书。

用法示例：
  python3 experiments/prime_matrix_prime_base_exponent_half_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json

输出：
  docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json
  docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.md"

FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
SQUARE_PHASE = "SquarePhaseRoughSurvivorUniformLowerBound"
NO_EXCEPTION = "PrimeSquareEndpointNoExceptionalPhaseTheorem"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"

SOURCE_FILES = [
    "prime-matrix-postsquare-first-half-finite-boundary-router.json",
    "prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json",
    "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json",
    "prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md",
    "prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_prime_base_exponent_half_barrier_router.py": sha256(Path(__file__).resolve())
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
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def scaling_rows() -> list[dict[str, Any]]:
    """列出 0.525/0.52 与 1/2 目标的尺度关系。"""
    return [
        {
            "input": "Baker-Harman-Pintz",
            "interval_for_X": "X^0.525",
            "after_X_equals_P2": "P^1.05",
            "target_length": "P",
            "sufficient": False,
        },
        {
            "input": "Li arXiv:2308.04458",
            "interval_for_X": "X^0.52",
            "after_X_equals_P2": "P^1.04",
            "target_length": "P",
            "sufficient": False,
        },
        {
            "input": "needed square-endpoint theorem",
            "interval_for_X": "X^(1/2) or better on X=P^2",
            "after_X_equals_P2": "P",
            "target_length": "P",
            "sufficient": True,
        },
    ]


def structure_rows() -> list[dict[str, str]]:
    """列出 P 为素数带来的真实结构与不足。"""
    return [
        {
            "structure": "q=P is harmless",
            "content": "0<r<P 时 P 不整除 P^2+r，因此端点自己的素因子不会覆盖窗口。",
            "effect": "消除一个平凡障碍，但不产生素数存在性下界。",
        },
        {
            "structure": "quadratic phase",
            "content": "对每个 q<P，禁类为 r==-P^2 mod q；相位属于负二次剩余轨道。",
            "effect": "给出平方相位刚性；单模密度仍是一条禁类，未自动改善筛密度。",
        },
        {
            "structure": "CRT square subvariety",
            "content": "模 primorial 的相位向量来自同一个 P^2，而不是任意 CRT 向量。",
            "effect": "这是可攻入口：若能证明 square-phase 短段不能被覆盖，即可突破。",
        },
        {
            "structure": "prime P equidistribution",
            "content": "P 在小模单位类中随 P 变化近似均匀，P^2 只落在平方类。",
            "effect": "适合做平均或异常集攻击；但本命题要每个 P，平均不足以闭合。",
        },
        {
            "structure": "parity",
            "content": "奇 P 下 P^2+r 为奇数要求 r 偶数。",
            "effect": "候选点减半，是已知局部密度的一部分，不是负面矛盾。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成最终判定表。"""
    return [
        row(
            "External0525SpecializedToPrimeSquareComputed",
            True,
            True,
            "把 X=P^2 代入外部 X^theta 短区间定理，只得到 P^(2theta) 长度。",
            "theta<=1/2 needed",
        ),
        row(
            "PrimeBaseRestrictionAutomaticallyImprovesExponent",
            False,
            False,
            "P 为素数只把端点相位限制到平方轨道；现有定理没有给出从 0.52/0.525 到 1/2 的自动降维。",
            f"{SQUARE_PHASE} OR {NO_EXCEPTION}",
        ),
        row(
            "SquarePhaseRigidityAttackTargetIdentified",
            True,
            False,
            "真正可攻点是证明负平方相位的短区间筛残洞有统一下界，或任何失败产生 PDEC/SAE 缺陷。",
            f"{SQUARE_PHASE} OR PDEC/SAE defect",
        ),
        row(
            "AlmostAllPrimeBaseWouldSuffice",
            False,
            False,
            "几乎所有 P 有素数不够；需要所有素数 P，或证明异常集不含任何素数平方端点。",
            NO_EXCEPTION,
        ),
        row(
            "FirstHalfPrimeSquareClosedByPrimeBaseRigidity",
            False,
            False,
            "当前语料和外部输入尚未把 P 为素数的结构刚性转成全局无条件素数存在性。",
            f"{FIRST_HALF} OR {NONFINAL}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    return {
        "certificate_type": "prime_matrix_prime_base_exponent_half_barrier_router",
        "status": "prime_base_square_phase_rigidity_identified_but_half_exponent_not_closed",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "external_0525_or_052_specialization_sufficient": False,
        "prime_base_restriction_auto_breaks_half_barrier": False,
        "square_phase_rigidity_attack_target_identified": True,
        "first_half_prime_square_input_current_corpus_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FIRST_HALF,
        "hardpoint_after_router": f"{SQUARE_PHASE} OR {NO_EXCEPTION} OR {NONFINAL}",
        "next_direct_attack_target": SQUARE_PHASE,
        "parallel_attack_targets": [NO_EXCEPTION, NONFINAL],
        "scaling_rows": scaling_rows(),
        "structure_rows": structure_rows(),
        "decision_rows": decision_rows(),
        "external_references": [
            {
                "name": "Baker-Harman-Pintz, The difference between consecutive primes, II",
                "url": "https://doi.org/10.1112/plms/83.3.532",
                "exponent": "0.525",
            },
            {
                "name": "Runbo Li, The number of primes in short intervals and numerical calculations for Harman's sieve",
                "url": "https://arxiv.org/abs/2308.04458",
                "exponent": "0.52 for sufficiently large x",
            },
        ],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "把通用短区间定理专门化到 `X=P^2` 后，`X^0.525` 与 `X^0.52` "
            "分别变成 `P^1.05` 与 `P^1.04`，仍长于目标窗口 `P`。"
            "限制 `P` 为素数确实给出平方相位刚性：小模禁类为 `r=-P^2 mod q`，"
            "且整个 CRT 相位向量落在平方轨道上；但这只提供新的攻击入口，"
            "当前尚未推出每个素数平方端点后长度 `P` 内必有素数。"
            "因此不能把指数自动压到 `1/2` 以下；下一步应直接攻 square-phase 粗幸存下界，"
            "或证明任何 square-phase 覆盖失败都会产生已登记 PDEC/SAE/预算矛盾。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 素数基点 1/2 指数障碍审查路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_0525_or_052_specialization_sufficient={fmt_bool(result['external_0525_or_052_specialization_sufficient'])}",
        f"prime_base_restriction_auto_breaks_half_barrier={fmt_bool(result['prime_base_restriction_auto_breaks_half_barrier'])}",
        f"square_phase_rigidity_attack_target_identified={fmt_bool(result['square_phase_rigidity_attack_target_identified'])}",
        f"first_half_prime_square_input_current_corpus_proved={fmt_bool(result['first_half_prime_square_input_current_corpus_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 尺度换算",
        "",
        "| input | interval for X | after X=P^2 | target | sufficient |",
        "| --- | --- | --- | --- | ---: |",
    ]
    for item in result["scaling_rows"]:
        lines.append(
            f"| {table_cell(item['input'])} | `{item['interval_for_X']}` | "
            f"`{item['after_X_equals_P2']}` | `{item['target_length']}` | `{fmt_bool(item['sufficient'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. P 为素数带来的结构刚性",
            "",
            "| structure | content | effect |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["structure_rows"]:
        lines.append(
            f"| `{item['structure']}` | {table_cell(item['content'])} | {table_cell(item['effect'])} |"
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
            f"- 主攻 `{SQUARE_PHASE}`：证明负平方相位短段中存在统一粗幸存残洞。",
            f"- 若 square-phase 粗幸存失败，必须生成 PDEC/SAE/ColumnCRT 缺陷并接回 `{NONFINAL}`。",
            f"- 平行强路线 `{NO_EXCEPTION}`：证明通用短区间异常集不含任何素数平方端点；这强于平均结果。",
            "",
            "## 5. 外部参考",
            "",
            "| source | exponent | url |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["external_references"]:
        lines.append(f"| {table_cell(item['name'])} | `{item['exponent']}` | {item['url']} |")
    lines.extend(
        [
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
                "next_direct_attack_target": result["next_direct_attack_target"],
                "external_specialization_sufficient": result["external_0525_or_052_specialization_sufficient"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
