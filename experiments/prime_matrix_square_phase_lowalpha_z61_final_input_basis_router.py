#!/usr/bin/env python3
"""汇总 z=61 strict 自足线的最终输入基与剩余守门项。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_final_input_basis_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-final-input-basis-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-final-input-basis-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-final-input-basis-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DYADIC_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json"
NORMAL_FORM_JSON = (
    DOCS
    / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json"
)
QUADRATIC_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json"
ADMISSIBILITY_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.json"
)
PDEC_JSON = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"

OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-final-input-basis-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-final-input-basis-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def eval_poly(coefficients: list[int], t_value: int) -> int:
    """Horner 法计算从高到低排列的多项式。"""
    value = 0
    for coefficient in coefficients:
        value = value * t_value + coefficient
    return value


def is_prime(value: int) -> bool:
    """朴素确定性素性检验，足够覆盖本证书样本。"""
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    step = 5
    while step * step <= value:
        if value % step == 0 or value % (step + 2) == 0:
            return False
        step += 6
    return True


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    paths = [
        DYADIC_JSON,
        NORMAL_FORM_JSON,
        QUADRATIC_JSON,
        ADMISSIBILITY_JSON,
        PDEC_JSON,
        Path(__file__).resolve(),
    ]
    return {str(path.relative_to(ROOT)): file_sha256(path) for path in paths}


def make_gate(
    name: str,
    closed: bool,
    blocks_final: bool,
    evidence: str,
    meaning: str,
) -> dict[str, Any]:
    """构造守门项。"""
    return {
        "gate": name,
        "closed": closed,
        "blocks_final": blocks_final,
        "evidence": evidence,
        "meaning": meaning,
    }


def run() -> dict[str, Any]:
    """生成最终输入基证书。"""
    dyadic = load_json(DYADIC_JSON)
    normal_form = load_json(NORMAL_FORM_JSON)
    quadratic = load_json(QUADRATIC_JSON)
    admissibility = load_json(ADMISSIBILITY_JSON)
    pdec = load_json(PDEC_JSON)

    selected_t = int(quadratic["selected_t"])
    p_poly = quadratic["p_polynomial"]["coefficients_c2_c1_c0"]
    a4_poly = quadratic["a4_polynomial"]["coefficients_c2_c1_c0"]
    a2_poly = quadratic["a2_polynomial"]["coefficients_c2_c1_c0"]
    sample_values = {
        "t": selected_t,
        "p": eval_poly(p_poly, selected_t),
        "a4": eval_poly(a4_poly, selected_t),
        "a2": eval_poly(a2_poly, selected_t),
    }
    sample_prime_rows = [
        {"name": name, "value": value, "prime": is_prime(value)}
        for name, value in sample_values.items()
        if name != "t"
    ]
    sample_triple_prime = all(row["prime"] for row in sample_prime_rows)

    exact_admissibility_closed = bool(admissibility["exact_admissibility_closed"])
    schinzel_input = bool(admissibility["schinzel_hypothesis_h_level_input_proved"])
    bateman_horn_input = bool(admissibility["bateman_horn_level_input_proved"])
    persistent_pdec_excluded = bool(admissibility["persistent_phase_pdec_excluded"]) or bool(
        pdec["primitive_multiatom_same_formal_unit_pdec_closed"]
    )
    pdec_admission_boundary_closed = bool(pdec["persistent_terminal_admission_boundary_closed"])
    materialized_pdec_closed = bool(pdec["current_materialized_persistent_terminal_instances_closed"])

    local_chain_closed = all(
        [
            dyadic["local_dyadic_companion_equivalence_closed"],
            normal_form["shifted_square_window_algebraic_normal_form_closed_for_sample"],
            quadratic["sample_polynomial_recovery_closed"],
            exact_admissibility_closed,
            sample_triple_prime,
        ]
    )
    external_prime_tuple_input_available = schinzel_input or bateman_horn_input
    final_z61_gate_closed = local_chain_closed and (
        external_prime_tuple_input_available or persistent_pdec_excluded
    )

    gates = [
        make_gate(
            "Z61FormalUnitAndNoTheoremSwitch",
            bool(
                dyadic["same_theorem_target_preserved"]
                and quadratic["same_theorem_target_preserved"]
                and admissibility["same_theorem_target_preserved"]
                and dyadic["no_theorem_switch"]
                and quadratic["no_theorem_switch"]
                and admissibility["no_theorem_switch"]
            ),
            False,
            "target=bucket unbalanced<=8, omega=4, shell=(8D,16D]",
            "本证书仍在同一个 z=61 formal unit 内工作，不把目标偷换为别的命题。",
        ),
        make_gate(
            "LocalDyadicCompanionEquivalence",
            bool(dyadic["local_dyadic_companion_equivalence_closed"]),
            False,
            dyadic["status"],
            "dyadic companion 的局部等价链已经闭合。",
        ),
        make_gate(
            "ShiftedSquareWindowNormalForm",
            bool(normal_form["shifted_square_window_algebraic_normal_form_closed_for_sample"]),
            False,
            normal_form["normal_form_equation"],
            "平方窗口已经正规化为单参数二次进位方程。",
        ),
        make_gate(
            "PolynomialTupleExactAdmissibility",
            exact_admissibility_closed,
            False,
            (
                f"degree={admissibility['product_degree']}, "
                f"content={admissibility['product_content']}, "
                f"no_fixed_prime_divisor={fmt_bool(admissibility['no_fixed_prime_divisor_proved'])}"
            ),
            "primitive、不可约、无固定素因子已闭合；局部同余障碍耗尽。",
        ),
        make_gate(
            "SampleT0Recovery",
            sample_triple_prime,
            False,
            f"t={selected_t}, p={sample_values['p']}, a4={sample_values['a4']}, a2={sample_values['a2']}",
            "样本点可恢复局部 companion；它不是全局输入。",
        ),
        make_gate(
            "SchinzelOrBatemanHornLevelInput",
            external_prime_tuple_input_available,
            not external_prime_tuple_input_available and not persistent_pdec_excluded,
            "simultaneous prime values for p(t), a4(t), a2(t)",
            "若走外部素性路线，必须提交 Schinzel H / Bateman-Horn 等级输入或等价强度定理。",
        ),
        make_gate(
            "PersistentPhasePDECAdmissionBoundary",
            pdec_admission_boundary_closed,
            False,
            pdec["status"],
            "持久终端准入边界已闭合；裸持久标签不能直接作为终端。",
        ),
        make_gate(
            "CurrentMaterializedPersistentInstances",
            materialized_pdec_closed,
            False,
            "current materialized primitive non-tautological candidates = 0",
            "当前已物化实例关闭，但这不排斥全局 family。",
        ),
        make_gate(
            "PrimitiveMultiAtomSameFormalUnitPDECExclusion",
            persistent_pdec_excluded,
            not external_prime_tuple_input_available and not persistent_pdec_excluded,
            "global U_CRT < L_PDEC for every admitted same-formal-unit primitive multi-atom certificate",
            "若走内部自足路线，必须排斥同 formal unit 的 primitive 多原子 PDEC family。",
        ),
    ]

    open_blocking_gates = [gate["gate"] for gate in gates if gate["blocks_final"]]
    theorem_boundary = {
        "closed_implication": (
            "LocalZ61ChainClosed AND "
            "(SchinzelOrBatemanHornLevelInput OR PrimitiveMultiAtomSameFormalUnitPDECExclusion) "
            "=> Z61CompanionGateClosed"
        ),
        "local_z61_chain_closed": local_chain_closed,
        "external_prime_tuple_input_available": external_prime_tuple_input_available,
        "persistent_phase_pdec_excluded": persistent_pdec_excluded,
        "final_z61_gate_closed": final_z61_gate_closed,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_final_input_basis_router",
        "status": "z61_final_input_basis_reduced_to_schinzel_level_or_primitive_multiatom_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_bucket": dyadic["target_bucket"],
        "target_omega": dyadic["target_omega"],
        "target_shell": dyadic["target_shell"],
        "phase_modulus_b": 28842,
        "selected_root_class": normal_form["selected_p_mod_A"],
        "normal_form": {
            "A": normal_form["coefficient_A"],
            "C": normal_form["constant_C"],
            "equation": normal_form["normal_form_equation"],
            "crt_root_class_count_mod_A": normal_form["crt_root_class_count_mod_A"],
        },
        "sample_values": sample_values,
        "sample_prime_rows": sample_prime_rows,
        "gates": gates,
        "open_blocking_gates": open_blocking_gates,
        "theorem_boundary": theorem_boundary,
        "narrowest_internal_hardpoint": "PrimitiveMultiAtomSameFormalUnitPDECCertificateForB28842",
        "narrowest_external_hardpoint": "SchinzelHypothesisHLevelInputForZ61PolynomialPrimeTuple",
        "direct_next_attack_order": [
            "B28842SameFormalUnitPrimitiveMultiAtomPDECExclusion",
            "Z61PolynomialPrimeTupleSchinzelLevelInputOrExternalTheoremMatching",
        ],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "z=61 strict 自足线的局部链条已经压到底：dyadic companion 等价、平方窗口正规形、"
            "单参数多项式三元组、以及 primitive/不可约/无固定素因子全部闭合。"
            "因此继续在局部同余或有限样本上硬挤不会推出全局闭合；剩余守门项精确二分为："
            "外部 Schinzel/Bateman-Horn 等级的三多项式同步素值输入，或内部同 formal unit 的 "
            "primitive 多原子 PDEC family 排斥。当前已物化 PDEC 实例为零，只关闭实例和准入边界，"
            "不关闭全局 family。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    boundary = result["theorem_boundary"]
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 final input basis",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_modulus_b={result['phase_modulus_b']}",
        f"selected_root_class={result['selected_root_class']}",
        f"local_z61_chain_closed={fmt_bool(boundary['local_z61_chain_closed'])}",
        f"external_prime_tuple_input_available={fmt_bool(boundary['external_prime_tuple_input_available'])}",
        f"persistent_phase_pdec_excluded={fmt_bool(boundary['persistent_phase_pdec_excluded'])}",
        f"final_z61_gate_closed={fmt_bool(boundary['final_z61_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(boundary['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最终输入基定理",
        "",
        f"`{boundary['closed_implication']}`。",
        "",
        "反过来说，在本仓库当前输入集中，局部链条已闭合但两个全局守门项均未提交，",
        "所以不能把该 z=61 线路登记为无条件闭合。",
        "",
        "## 2. 守门表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for gate in result["gates"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=gate["gate"],
                closed=fmt_bool(gate["closed"]),
                blocks=fmt_bool(gate["blocks_final"]),
                evidence=table_cell(gate["evidence"]),
                meaning=table_cell(gate["meaning"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 样本恢复不是全局证明",
            "",
            "| object | value | prime |",
            "| --- | ---: | --- |",
        ]
    )
    for row in result["sample_prime_rows"]:
        lines.append(f"| `{row['name']}` | {row['value']} | `{fmt_bool(row['prime'])}` |")

    lines.extend(
        [
            "",
            "样本点 `t=0` 说明局部 companion 实例真实存在；但全局命题需要同类输入在证明链所需尺度上成立。",
            "这正是 Schinzel/Bateman-Horn 级同步素值输入，或内部 PDEC 排斥必须承担的内容。",
            "",
            "## 4. 下一步最窄硬点",
            "",
            f"- 内部自足线：`{result['narrowest_internal_hardpoint']}`。",
            f"- 外部对接线：`{result['narrowest_external_hardpoint']}`。",
            "- 优先顺序：先攻 `B28842` 同 formal unit primitive 多原子 PDEC 容量排斥；若改走外部线，必须严格匹配三多项式同步素值定理。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for filename, digest in result["source_hashes"].items():
        lines.append(f"| `{filename}` | `{digest}` |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, default=OUT_JSON)
    parser.add_argument("--md", type=Path, default=OUT_MD)
    args = parser.parse_args()

    result = run()
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")
    print(f"status={result['status']}")
    print(f"open_blocking_gates={result['open_blocking_gates']}")


if __name__ == "__main__":
    main()
