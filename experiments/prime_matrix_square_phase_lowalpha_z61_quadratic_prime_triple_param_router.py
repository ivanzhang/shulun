#!/usr/bin/env python3
"""审计 z=61 二次剩余类三重素性输入的单参数多项式形态。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_quadratic_prime_triple_param_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json"
)
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.md"

NEXT_TARGET = "PolynomialPrimeTupleInputOrPersistentPhasePDEC"
LOCAL_AUDIT_PRIME_BOUND = 199


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        "docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json": file_sha256(
            SOURCE_JSON
        ),
        "experiments/prime_matrix_square_phase_lowalpha_z61_quadratic_prime_triple_param_router.py": file_sha256(
            Path(__file__).resolve()
        ),
    }


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def primes_upto(n: int) -> list[int]:
    """生成小素数表。"""
    primes: list[int] = []
    for value in range(2, n + 1):
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return primes


def eval_poly(coeffs: list[int], t_value: int) -> int:
    """计算 c2*t^2+c1*t+c0。"""
    return coeffs[0] * t_value * t_value + coeffs[1] * t_value + coeffs[2]


def audit() -> dict[str, Any]:
    """执行单参数素性三元组审计。"""
    source = load(SOURCE_JSON)
    a_value = source["coefficient_A"]
    root_r = source["selected_p_mod_A"]
    s0 = source["selected_s"]
    selected_p = source["selected_p"]
    selected_a4 = source["selected_a4"]
    selected_a2 = source["selected_a2"]

    p_poly = [0, a_value, root_r]
    s_poly = [a_value, 2 * root_r, s0]
    a4_poly = [71 * a_value, 71 * 2 * root_r, 71 * s0 - 1]
    a2_poly = [74 * a_value, 74 * 2 * root_r, 74 * s0 - 1]

    sample_closed = (
        eval_poly(p_poly, 0) == selected_p
        and eval_poly(s_poly, 0) == s0
        and eval_poly(a4_poly, 0) == selected_a4
        and eval_poly(a2_poly, 0) == selected_a2
    )

    local_rows = []
    no_local_obstruction = True
    for prime in primes_upto(LOCAL_AUDIT_PRIME_BOUND):
        surviving_residues = [
            t
            for t in range(prime)
            if eval_poly(p_poly, t) % prime
            and eval_poly(a4_poly, t) % prime
            and eval_poly(a2_poly, t) % prime
        ]
        if not surviving_residues:
            no_local_obstruction = False
        local_rows.append(
            {
                "prime": prime,
                "surviving_residue_count": len(surviving_residues),
                "first_surviving_residues": surviving_residues[:12],
                "local_obstruction": len(surviving_residues) == 0,
            }
        )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_quadratic_prime_triple_param_router",
        "status": "z61_quadratic_prime_triple_reduced_to_polynomial_prime_tuple_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "p_polynomial": {"name": "p(t)", "coefficients_c2_c1_c0": p_poly},
        "s_polynomial": {"name": "s(t)", "coefficients_c2_c1_c0": s_poly},
        "a4_polynomial": {"name": "a4(t)=71s(t)-1", "coefficients_c2_c1_c0": a4_poly},
        "a2_polynomial": {"name": "a2(t)=74s(t)-1", "coefficients_c2_c1_c0": a2_poly},
        "selected_t": 0,
        "sample_polynomial_recovery_closed": sample_closed,
        "local_audit_prime_bound": LOCAL_AUDIT_PRIME_BOUND,
        "local_obstruction_rows": local_rows,
        "no_local_obstruction_up_to_bound": no_local_obstruction,
        "polynomial_prime_tuple_input_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "选择平方根类 `p≡200003 (mod A)` 后，companion 输入变成单参数多项式素性三元组："
            "`p(t)=A t+200003`、`s(t)=A t^2+400006t+132`、"
            "`a4(t)=71s(t)-1`、`a2(t)=74s(t)-1`。"
            "小素数局部审计未发现覆盖性局部障碍，但这仍是多项式素数值输入，"
            "不是已证标准定理；必须作为新输入证明，或排斥 PersistentPhase-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 quadratic prime triple parameterization",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sample_polynomial_recovery_closed={fmt_bool(result['sample_polynomial_recovery_closed'])}",
        f"local_audit_prime_bound={result['local_audit_prime_bound']}",
        f"no_local_obstruction_up_to_bound={fmt_bool(result['no_local_obstruction_up_to_bound'])}",
        f"polynomial_prime_tuple_input_proved={fmt_bool(result['polynomial_prime_tuple_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单参数多项式",
        "",
        "| polynomial | coefficients `[c2,c1,c0]` |",
        "| --- | --- |",
        f"| `{result['p_polynomial']['name']}` | `{result['p_polynomial']['coefficients_c2_c1_c0']}` |",
        f"| `{result['s_polynomial']['name']}` | `{result['s_polynomial']['coefficients_c2_c1_c0']}` |",
        f"| `{result['a4_polynomial']['name']}` | `{result['a4_polynomial']['coefficients_c2_c1_c0']}` |",
        f"| `{result['a2_polynomial']['name']}` | `{result['a2_polynomial']['coefficients_c2_c1_c0']}` |",
        "",
        "## 2. 局部障碍审计",
        "",
        "| prime | surviving residues | first residues | obstruction |",
        "| ---: | ---: | --- | --- |",
    ]
    for row in result["local_obstruction_rows"][:30]:
        lines.append(
            f"| {row['prime']} | {row['surviving_residue_count']} | "
            f"`{row['first_surviving_residues']}` | {fmt_bool(row['local_obstruction'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：选定 CRT 根类下的单参数多项式正规形。",
            "- 已检查：小素数局部障碍未在审计范围内出现。",
            "- 未闭合：证明该多项式素性三元组有全局 companion，或排斥 PersistentPhase-PDEC。",
            "- 结论：这仍是强素性输入，不能作为已证事实调用。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "sample_polynomial_recovery_closed": result["sample_polynomial_recovery_closed"],
                "no_local_obstruction_up_to_bound": result["no_local_obstruction_up_to_bound"],
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
