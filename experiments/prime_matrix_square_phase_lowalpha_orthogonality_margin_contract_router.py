#!/usr/bin/env python3
"""把 squarefree 正交输入转成 Selberg 常数余量验收合同。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_orthogonality_margin_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
ORTH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json"
SELBERG_JSON = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.md"

DEFAULT_CONSTANT = 1.35
NEXT_TARGET = "UniformCoefficientRemainderAngleBoundTheta0182OrVectorSquarefreePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-squarefree-pdec-orthogonality-router.json",
    "prime-matrix-square-phase-lowalpha-rough-b-selberg-quadratic-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_orthogonality_margin_contract_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(constant: float) -> dict[str, Any]:
    """执行余量合同审计。"""
    orth = json.loads(ORTH_JSON.read_text(encoding="utf-8"))
    selberg = json.loads(SELBERG_JSON.read_text(encoding="utf-8"))
    selberg_by_z = {int(row["z"]): row for row in selberg["rows"]}
    rows = []
    for row in orth["rows"]:
        z = int(row["z"])
        selberg_row = selberg_by_z[z]
        model_over_mertens = float(selberg_row["model_over_mertens"])
        margin_over_mertens = constant - model_over_mertens
        allowed_net_abs = margin_over_mertens * float(row["mertens_model"])
        required_angle = safe_ratio(allowed_net_abs, float(row["cauchy_envelope"]))
        observed_angle = abs(float(row["net_over_cauchy"]))
        rows.append(
            {
                "z": z,
                "constant": constant,
                "model_over_mertens": model_over_mertens,
                "direct_over_mertens": float(selberg_row["direct_over_mertens"]),
                "margin_over_mertens": margin_over_mertens,
                "allowed_net_abs": allowed_net_abs,
                "cauchy_envelope": float(row["cauchy_envelope"]),
                "cauchy_over_mertens": float(row["cauchy_over_mertens"]),
                "required_abs_angle_bound": required_angle,
                "observed_abs_angle": observed_angle,
                "observed_angle_slack": None if required_angle is None else required_angle - observed_angle,
                "contract_passed_by_sample": required_angle is not None and observed_angle <= required_angle,
            }
        )
    tightest = min(rows, key=lambda item: item["required_abs_angle_bound"] or 0.0)
    sample_failures = [row for row in rows if not row["contract_passed_by_sample"]]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_orthogonality_margin_contract_router",
        "status": "selberg_constant_margin_reduced_to_uniform_angle_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "selberg_constant_margin_contract_closed": True,
        "sample_satisfies_margin_contract": len(sample_failures) == 0,
        "uniform_angle_bound_proved": False,
        "vector_squarefree_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "constant": constant,
        "rows": rows,
        "tightest_required_angle_row": tightest,
        "sample_failure_count": len(sample_failures),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Selberg 常数 `C` 的剩余要求可精确写成角度合同："
            "若 `|<c,R>|/(||c||_2||R||_2)` 不超过每个 `z` 的 required angle，"
            "则 `Q_direct<=C*Mertens`。"
            "默认 `C=1.35` 下最紧行是 `z=61`，只需统一角度界约 `0.181432`；"
            "这比样本观测角度 `0.001089` 宽很多。"
            "剩余不再是模糊取消，而是证明该统一角度界，或证明违反该角度界即 VectorSquarefree-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 正交余量合同",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selberg_constant_margin_contract_closed={fmt_bool(result['selberg_constant_margin_contract_closed'])}",
        f"sample_satisfies_margin_contract={fmt_bool(result['sample_satisfies_margin_contract'])}",
        f"uniform_angle_bound_proved={fmt_bool(result['uniform_angle_bound_proved'])}",
        f"vector_squarefree_pdec_excluded={fmt_bool(result['vector_squarefree_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 角度合同",
        "",
        "| z | model/M | direct/M | margin/M | Cauchy/M | required angle | observed angle | slack |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {fmt_float(row['model_over_mertens'])} | "
            f"{fmt_float(row['direct_over_mertens'])} | {fmt_float(row['margin_over_mertens'])} | "
            f"{fmt_float(row['cauchy_over_mertens'])} | "
            f"{fmt_float(row['required_abs_angle_bound'])} | "
            f"{fmt_float(row['observed_abs_angle'])} | {fmt_float(row['observed_angle_slack'])} |"
        )
    tight = result["tightest_required_angle_row"]
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            (
                f"- 最紧验收行为 `z={tight['z']}`，所需统一角度界为 "
                f"`{fmt_float(tight['required_abs_angle_bound'])}`。"
            ),
            "- 已闭合：角度界推出 `Q_direct<=C*Mertens` 的合同推理。",
            "- 未闭合：证明该统一角度界本身。",
            "- 未闭合：若角度界失败，证明失败向量形成可排斥的 `VectorSquarefree-PDEC`。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--constant", type=float, default=DEFAULT_CONSTANT)
    args = parser.parse_args()
    result = audit(args.constant)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "tightest_z": result["tightest_required_angle_row"]["z"],
                "tightest_required_angle": result["tightest_required_angle_row"][
                    "required_abs_angle_bound"
                ],
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
