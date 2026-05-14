#!/usr/bin/env python3
"""生成 final-tail 粗幸存下界的平方后半窗阻塞证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_final_tail_rough_survivor_obstruction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json
  docs/monograph/prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.md"

FINAL_TAIL_JSON = DOCS / "prime-matrix-inverse-alignment-final-tail-capacity-deficit-router.json"
FINAL_TAIL_LEDGER = DATA / "inverse-alignment-final-tail-capacity-probe-ledger.json"

SOURCE_FILES = [
    FINAL_TAIL_JSON,
    FINAL_TAIL_LEDGER,
    DOCS / "prime-matrix-zero-row-minrep-route-review.md",
    DOCS / "prime-matrix-inverse-alignment-min-x-phase-scan-router.json",
]

HARDPOINT = "UniformFinalTailRoughSurvivorLowerBoundOrRegisteredPhaseDefect"
FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
ROUGH_JACOBSTHAL = "PrimorialCutoffJacobsthalRoughSurvivorLowerBoundForPBlocks"
PDEC_AMPLIFICATION = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_final_tail_rough_survivor_obstruction_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def theorem_rows() -> list[dict[str, str]]:
    """列出阻塞边界的逻辑链。"""
    return [
        {
            "name": "x_equals_P_specialization",
            "status": "closed",
            "statement": "The final-tail lower bound must hold in particular for x=P, i.e. for the interval P^2< n <P^2+P.",
        },
        {
            "name": "nontail_residual_is_prime",
            "status": "closed",
            "statement": "After the final-tail cutoff, a residual n=P^2+r not hit by the largest tail prime cannot be composite; otherwise its non-P prime factors exceed P and their product is too large.",
        },
        {
            "name": "final_tail_implies_first_half_prime_square",
            "status": "closed",
            "statement": "Therefore a uniform final-tail rough survivor lower bound implies a prime in (P^2,P^2+P) for every prime P.",
        },
        {
            "name": "finite_probe_boundary",
            "status": "diagnostic_only",
            "statement": "The P<=251 probe supports the pattern but cannot be promoted to a proof of the first-half prime-square input.",
        },
        {
            "name": "self_contained_closure_status",
            "status": "open",
            "statement": "The current corpus has no self-contained proof of this first-half square short-interval input, so final-tail cannot close the row/column theorem by itself.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "FinalTailDecompositionImported",
            "closed": result["final_tail_decomposition_imported"],
            "proved": result["final_tail_decomposition_imported"],
            "meaning": "上一层已经证明 final-tail 残洞二分为最大尾素数倍数或真正素数。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "FinalTailUniformBoundImpliesFirstHalfPrimeSquare",
            "closed": True,
            "proved": True,
            "meaning": "把 final-tail 下界代入 x=P，立即要求 P^2 后长度 P 的前半窗有素数。",
            "remaining": FIRST_HALF,
        },
        {
            "gate": "FirstHalfPrimeSquareInputCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前合著语料没有给出该短区间素数输入的作者侧证明。",
            "remaining": FIRST_HALF,
        },
        {
            "gate": "UniformFinalTailRoughSurvivorLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "final-tail 有限探针不能升级为全局 Jacobsthal/rough survivor 下界。",
            "remaining": ROUGH_JACOBSTHAL,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "若不新增该强短区间输入，就必须走非 final-tail 的 PDEC/SAE/预算放大矛盾路线。",
            "remaining": f"{FIRST_HALF} OR {PDEC_AMPLIFICATION}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造阻塞证书。"""
    final_tail = load_json(FINAL_TAIL_JSON)
    imported = final_tail.get("final_tail_residual_decomposition_closed") is True
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_final_tail_rough_survivor_obstruction_router",
        "status": "final_tail_uniform_bound_reduced_to_first_half_prime_square_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_for_global_proof": True,
        "final_tail_decomposition_imported": imported,
        "final_tail_uniform_bound_implies_first_half_prime_square_input": imported,
        "first_half_prime_square_input_current_corpus_proved": False,
        "uniform_final_tail_rough_survivor_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{FIRST_HALF} OR {PDEC_AMPLIFICATION}",
        "next_direct_attack_target": FIRST_HALF,
        "parallel_attack_targets": [ROUGH_JACOBSTHAL, PDEC_AMPLIFICATION],
        "theorem_rows": theorem_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`UniformFinalTailRoughSurvivorLowerBound` 已被压到一个明确的强输入边界："
            "只要取 `x=P`，final-tail 残洞中任何非最大尾素数倍数的幸存者都必须是区间 `(P^2,P^2+P)` 内的素数。"
            "因此若要用 final-tail 路线直接闭合，就必须证明每个素数 `P` 的平方后前半窗含素数，"
            "或证明等价强度的 primorial cutoff 粗幸存下界。当前语料没有该作者侧无条件证明，"
            "所以本路线不能在此处宣布行/列命题闭合；下一步只能新增这个强短区间输入，"
            "或回到 PDEC/SAE/非持久预算放大路线寻找不依赖 first-half prime-square 的矛盾。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix inverse alignment final-tail 粗幸存阻塞路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"final_tail_uniform_bound_implies_first_half_prime_square_input={fmt_bool(result['final_tail_uniform_bound_implies_first_half_prime_square_input'])}",
        f"first_half_prime_square_input_current_corpus_proved={fmt_bool(result['first_half_prime_square_input_current_corpus_proved'])}",
        f"uniform_final_tail_rough_survivor_lower_bound_proved={fmt_bool(result['uniform_final_tail_rough_survivor_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 阻塞链",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
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
            "## 3. 下一步",
            "",
            f"- 若坚持 final-tail 直接路线，必须证明 `{FIRST_HALF}` 或等价强度的 `{ROUGH_JACOBSTHAL}`。",
            f"- 若不引入该强输入，则应转攻 `{PDEC_AMPLIFICATION}`，从低模缺陷、相位漂移或非持久预算侧寻找矛盾。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON 与 Markdown。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(
        "final_tail_uniform_bound_implies_first_half_prime_square_input="
        + fmt_bool(result["final_tail_uniform_bound_implies_first_half_prime_square_input"])
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
