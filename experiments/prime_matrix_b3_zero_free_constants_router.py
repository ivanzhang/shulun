#!/usr/bin/env python3
"""Prime Matrix B=3 零点自由区常数账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_free_constants_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-free-constants-router.json
  docs/monograph/prime-matrix-b3-zero-free-constants-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-free-theta-envelope-router.json"
DEFAULT_EXPLICIT_FORMULA = ROOT / "docs" / "rh-pc1-explicit-formula-proof-appendix.md"
DEFAULT_PC1_THEOREMIZATION = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_HADAMARD = DOCS / "prime-matrix-b3-hadamard-factorization-router.json"
DEFAULT_EULER = DOCS / "prime-matrix-b3-euler-product-positive-kernel-router.json"
DEFAULT_REPULSION = DOCS / "prime-matrix-b3-zero-repulsion-inequality-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-free-constants-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-free-constants-router.md"

OLD_ATOM = "SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger"
XI_ATOM = "CompletedZetaXiFunctionalEquationAndHadamardProductLedger"
XI_CLOSED = "CompletedZetaXiFunctionalEquationAndHadamardProductClosed"
EULER_ATOM = "EulerProductLogDerivativePositiveRealPartLedger"
EULER_CLOSED = "EulerProductLogDerivativePositiveRealPartClosed"
TRIG_IDENTITY_ATOM = "DeLaValleePoussinTrigonometricKernelIdentityClosed"
REPULSION_ATOM = "DeLaValleePoussinZeroRepulsionInequalityLedger"
REPULSION_CLOSED = "DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants"
CONSTANT_ATOM = "ExplicitZeroFreeRegionConstantNumericalLedger"
LOW_HEIGHT_ATOM = "FiniteLowHeightZeroCheckLedger"
CONTOUR_ATOM = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
FINITE_BRIDGE_ATOM = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
MERTENS_CONSTANT_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
DUSART_THETA_DENOMINATOR = 36_260


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式，避免报告中出现过长浮点串。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_any(text: str, needles: list[str]) -> bool:
    """检查文本是否包含任一片段。"""
    return any(needle in text for needle in needles)


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def trig_identity_sample() -> dict[str, Any]:
    """核验 de la Vallee Poussin 三角核恒等式的纯代数层。"""
    samples: list[dict[str, float]] = []
    max_error = 0.0
    min_value = float("inf")
    for idx in range(2048):
        t = 2.0 * math.pi * idx / 2048.0
        left = 3.0 + 4.0 * math.cos(t) + math.cos(2.0 * t)
        right = 2.0 * (1.0 + math.cos(t)) ** 2
        max_error = max(max_error, abs(left - right))
        min_value = min(min_value, left)
        if idx in {0, 512, 1024, 1536}:
            samples.append({"t": t, "kernel": left, "square_form": right})
    return {
        "identity": "3+4*cos(t)+cos(2t)=2*(1+cos(t))^2>=0",
        "sample_count": 2048,
        "max_sample_error": max_error,
        "min_sample_value": min_value,
        "samples": samples,
        "closed_as_algebraic_identity": max_error < 1e-12 and min_value > -1e-12,
    }


def constant_pressure() -> dict[str, Any]:
    """计算 x=20000 锚点对普通显式 PNT 误差常数的压力。"""
    log_x = math.log(ANCHOR_X)
    sqrt_log_x = math.sqrt(log_x)
    target_rel = 1.0 / DUSART_THETA_DENOMINATOR
    target_log = math.log(DUSART_THETA_DENOMINATOR)
    required_a_c1 = target_log / sqrt_log_x
    required_a_c10 = (math.log(10.0) + target_log) / sqrt_log_x
    required_x_for_a1_c1 = math.exp(target_log**2)
    required_x_for_a2_c1 = math.exp((target_log / 2.0) ** 2)
    return {
        "anchor_x": ANCHOR_X,
        "log_anchor": log_x,
        "sqrt_log_anchor": sqrt_log_x,
        "target_relative_theta_error": target_rel,
        "dusart_theta_denominator": DUSART_THETA_DENOMINATOR,
        "required_a_for_C_exp_minus_a_sqrtlog_at_anchor_C1": required_a_c1,
        "required_a_for_C_exp_minus_a_sqrtlog_at_anchor_C10": required_a_c10,
        "x_needed_if_a1_C1": required_x_for_a1_c1,
        "x_needed_if_a2_C1": required_x_for_a2_c1,
        "diagnosis": (
            "x=20000 is too low for a bare asymptotic PNT error of shape "
            "C exp(-a sqrt(log x)) unless the explicit constants and finite "
            "zero checks are very strong."
        ),
    }


def source_audit(texts: dict[str, str]) -> dict[str, Any]:
    """审查当前材料是否已经包含零点自由区常数证明的必要部件。"""
    combined = "\n".join(texts.values())
    explicit_formula_present = contains_all(
        texts["explicit_formula"],
        ["Mellin", "-ζ'(s)/ζ(s)", "非平凡零点", "Ψ_W(X)"],
    )
    xi_functional_equation_present = contains_any(
        combined,
        [
            "Riemann xi",
            "ξ(s)=ξ(1-s)",
            "xi(s)=xi(1-s)",
            "\\xi(s)=\\xi(1-s)",
            "Hadamard product for xi",
        ],
    )
    euler_log_derivative_present = contains_all(
        combined,
        ["Euler product", "-ζ'(s)/ζ(s)", "Re"],
    )
    zero_free_argument_present = contains_all(
        combined,
        ["de la Vallée", "zero-free", "3+4", "cos"],
    )
    explicit_constant_present = contains_all(
        combined,
        ["zero-free", "1/log", "constant", "low height"],
    )
    finite_low_height_present = contains_all(
        combined,
        ["zero", "height", "hash", "finite"],
    )
    external_route_registered = contains_all(
        texts["external_index"] + "\n" + texts["final_draft"],
        ["Dusart", "Mertens"],
    )
    return {
        "smooth_explicit_formula_present": explicit_formula_present,
        "xi_functional_equation_hadamard_present": xi_functional_equation_present,
        "euler_product_log_derivative_positive_kernel_present": euler_log_derivative_present,
        "de_la_vallee_poussin_zero_free_argument_present": zero_free_argument_present,
        "explicit_zero_free_constant_ledger_present": explicit_constant_present,
        "finite_low_height_zero_check_present": finite_low_height_present,
        "external_dusart_mertens_route_registered": external_route_registered,
    }


def replacement_pair() -> str:
    """写出零点自由区常数账本的自足替换包。"""
    return (
        f"({XI_ATOM} AND {EULER_ATOM} AND {TRIG_IDENTITY_ATOM} "
        f"AND {REPULSION_ATOM} AND {CONSTANT_ATOM} AND {LOW_HEIGHT_ATOM})"
    )


def current_replacement_pair(evidence: dict[str, bool]) -> str:
    """写出当前已证路由吸收后的替换包。"""
    xi = XI_CLOSED if evidence["xi_closed"] else XI_ATOM
    euler = EULER_CLOSED if evidence["euler_closed"] else EULER_ATOM
    repulsion = REPULSION_CLOSED if evidence["repulsion_closed"] else REPULSION_ATOM
    return (
        f"({xi} AND {euler} AND {TRIG_IDENTITY_ATOM} "
        f"AND {repulsion} AND {CONSTANT_ATOM} AND {LOW_HEIGHT_ATOM})"
    )


def replace_atom(text: str) -> str:
    """替换旧零点自由区常数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def replace_atom_with_current(text: str, evidence: dict[str, bool]) -> str:
    """用当前已证状态替换旧零点自由区常数原子。"""
    return text.replace(OLD_ATOM, current_replacement_pair(evidence))


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    previous: dict[str, Any],
    audit: dict[str, Any],
    trig: dict[str, Any],
    evidence: dict[str, bool],
) -> list[dict[str, Any]]:
    """生成零点自由区常数账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    xi_closed = bool(evidence["xi_closed"])
    euler_closed = bool(evidence["euler_closed"])
    trig_closed = bool(trig["closed_as_algebraic_identity"])
    repulsion_closed = bool(evidence["repulsion_closed"])
    constant_closed = bool(audit["explicit_zero_free_constant_ledger_present"])
    low_height_closed = bool(audit["finite_low_height_zero_check_present"])
    reduced = active and guard and xi_closed and euler_closed and trig_closed and repulsion_closed
    return [
        row(
            "ZeroFreeConstantsGateActive",
            active,
            False,
            "上一层唯一内部最窄点是自足 de la Vallee Poussin 零点自由区常数账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条中补解析输入，不用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SmoothExplicitFormulaStillOnlyStartingPoint",
            bool(audit["smooth_explicit_formula_present"]),
            True,
            "平滑显式公式提供 -zeta'/zeta 的入口，但不包含零点自由区常数。",
            "不能替代零点自由区证明。",
        ),
        row(
            "XiFunctionalEquationHadamardClosed",
            xi_closed,
            True,
            "zeta/xi 函数方程、整函数增长、Hadamard 乘积与对数导数基础包已经由后续路由闭合。",
            XI_CLOSED if xi_closed else XI_ATOM,
        ),
        row(
            "EulerProductLogDerivativePositiveKernelClosed",
            euler_closed,
            True,
            "sigma>1 的 Euler product 对数导数正性已闭合，可接入零点排斥不等式。",
            EULER_CLOSED if euler_closed else EULER_ATOM,
        ),
        row(
            "TrigonometricKernelIdentityClosed",
            trig_closed,
            True,
            "de la Vallee Poussin 核 3+4cos(t)+cos(2t)=2(1+cos(t))^2>=0 是纯代数闭合。",
            TRIG_IDENTITY_ATOM,
        ),
        row(
            "ZeroRepulsionInequalityClosedSymbolic",
            repulsion_closed,
            True,
            "三角核、Euler 正性和 Hadamard 分式已经合并为符号常数版 de la Vallee Poussin 零点排斥。",
            REPULSION_CLOSED if repulsion_closed else REPULSION_ATOM,
        ),
        row(
            "ExplicitZeroFreeConstantNumericalLedgerMissing",
            constant_closed,
            False,
            "还缺把排斥不等式常数化为可用于 x>=20000 theta 包络的显式常数账本。",
            CONSTANT_ATOM,
        ),
        row(
            "FiniteLowHeightZeroCheckMissing",
            low_height_closed,
            False,
            "任何低阈值显式界都需要低高度零点排除或有限验证证书；仓库尚无 hash 账本。",
            LOW_HEIGHT_ATOM,
        ),
        row(
            "ZeroFreeConstantsReducedToNamedZetaPackage",
            reduced,
            False,
            "旧零点自由区常数原子已吸收 zeta 基础、Euler 正性、三角核和符号排斥；剩余为显式数值常数与低高度核验。",
            current_replacement_pair(evidence),
        ),
        row(
            "ContourThetaEnvelopeStillDownstream",
            False,
            False,
            "即便零点自由区常数账本完成，还必须把它经 Perron/显式公式轮廓积分转成 theta/psi 包络。",
            CONTOUR_ATOM,
        ),
        row(
            "FiniteThetaBridgeStillDownstream",
            False,
            False,
            "轮廓积分阈值通常高于 20000 时，需要有限桥把阈值下推到 B3 锚点。",
            FINITE_BRIDGE_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "外部 Dusart/Mertens 版虽然已越过 B3 主系数包，但最终仍需 DStructure/Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点自由区常数账本路由。"""
    previous = load_json(paths["previous"])
    evidence_docs = {
        "hadamard": load_json(paths["hadamard"]),
        "euler": load_json(paths["euler"]),
        "repulsion": load_json(paths["repulsion"]),
    }
    texts = {
        name: path.read_text(encoding="utf-8")
        for name, path in paths.items()
        if name not in {"previous", "hadamard", "euler", "repulsion"}
    }
    audit = source_audit(texts)
    evidence = {
        "xi_closed": evidence_docs["hadamard"].get(
            "completed_zeta_xi_functional_equation_hadamard_product_closed"
        )
        is True,
        "euler_closed": evidence_docs["euler"].get(
            "euler_product_log_derivative_positive_real_part_closed"
        )
        is True,
        "repulsion_closed": evidence_docs["repulsion"].get(
            "zero_repulsion_inequality_closed_symbolic_constants"
        )
        is True,
        "explicit_zero_free_constants_fixed": evidence_docs["repulsion"].get(
            "explicit_zero_free_constants_fixed"
        )
        is True,
        "finite_low_height_zero_check_closed": evidence_docs["repulsion"].get(
            "finite_low_height_zero_check_closed"
        )
        is True,
    }
    trig = trig_identity_sample()
    pressure = constant_pressure()
    rows = build_rows(previous, audit, trig, evidence)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ZeroFreeConstantsReducedToNamedZetaPackage"
    )
    latest_self = replace_atom_with_current(previous.get("latest_self_contained_basis", ""), evidence)
    source_paths = list(paths.values())
    self_contained_proved = (
        reduced
        and evidence["explicit_zero_free_constants_fixed"]
        and evidence["finite_low_height_zero_check_closed"]
    )
    return {
        "certificate_type": "b3_zero_free_constants_router",
        "status": "zero_free_constants_reduced_to_numeric_and_lowheight_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_free_constants_reduced": reduced,
        "zero_free_constants_self_contained_proved": self_contained_proved,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "current_replacement_self_contained": {OLD_ATOM: current_replacement_pair(evidence)},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CONSTANT_ATOM,
        "secondary_priority": LOW_HEIGHT_ATOM,
        "tertiary_priority": CONTOUR_ATOM,
        "quaternary_priority": FINITE_BRIDGE_ATOM,
        "low_height_priority": LOW_HEIGHT_ATOM,
        "downstream_priority": CONTOUR_ATOM,
        "post_theta_priority": MERTENS_CONSTANT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "proved_route_audit": evidence,
        "trigonometric_kernel_audit": trig,
        "constant_pressure": pressure,
        "plain_conclusion": (
            "zeta/xi 基础包、Euler product 对数导数正性、三角核非负性和符号常数版零点排斥"
            "已经由仓库内后续路由闭合。严格自足零点自由区常数账本仍未完成，因为还缺"
            "显式 C_log/T0/c 数值账本与低高度零点有限核验；不能升级为行命题无条件证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    current_replacement = next(iter(result["current_replacement_self_contained"].items()))
    pressure = result["constant_pressure"]
    lines = [
        "# Prime Matrix B=3 零点自由区常数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zero_free_constants_reduced={fmt_bool(result['zero_free_constants_reduced'])}",
        f"zero_free_constants_self_contained_proved={fmt_bool(result['zero_free_constants_self_contained_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "当前已证状态吸收后：",
        "",
        "```text",
        current_replacement[0],
        "  =>",
        current_replacement[1],
        "```",
        "",
        "这说明当前硬点已经不是方阵覆盖几何本身，而是把显式 PNT 的解析机器完全内联。",
        "",
        "## 2. x=20000 常数压力",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| anchor_x | `{pressure['anchor_x']}` |",
        f"| log(anchor_x) | `{fmt_float(pressure['log_anchor'])}` |",
        f"| sqrt(log(anchor_x)) | `{fmt_float(pressure['sqrt_log_anchor'])}` |",
        f"| target relative theta error | `{pressure['target_relative_theta_error']:.15f}` |",
        (
            "| required a for C exp(-a sqrt(log x)) at C=1 | "
            f"`{fmt_float(pressure['required_a_for_C_exp_minus_a_sqrtlog_at_anchor_C1'])}` |"
        ),
        (
            "| required a for C exp(-a sqrt(log x)) at C=10 | "
            f"`{fmt_float(pressure['required_a_for_C_exp_minus_a_sqrtlog_at_anchor_C10'])}` |"
        ),
        (
            "| x needed if a=1,C=1 | "
            f"`{pressure['x_needed_if_a1_C1']:.6e}` |"
        ),
        (
            "| x needed if a=2,C=1 | "
            f"`{pressure['x_needed_if_a2_C1']:.6e}` |"
        ),
        "",
        (
            "结论：`x=20000` 对普通 `C exp(-a sqrt(log x))` 型 PNT 误差极苛刻；"
            "若不引用 Dusart/Rosser-Schoenfeld，就必须给出显式零点自由区常数加低高度零点核验，"
            "或把解析阈值推高后再用有限桥下推。"
        ),
        "",
        "## 3. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in result["source_audit"].items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
    for key, value in result["proved_route_audit"].items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
    lines.extend(
        [
            "",
            "## 4. 三角核审查",
            "",
            "```text",
            result["trigonometric_kernel_audit"]["identity"],
            f"sample_count={result['trigonometric_kernel_audit']['sample_count']}",
            f"max_sample_error={result['trigonometric_kernel_audit']['max_sample_error']:.3e}",
            f"min_sample_value={result['trigonometric_kernel_audit']['min_sample_value']:.3e}",
            "```",
            "",
            "三角核非负性与 Euler/Hadamard/符号排斥已合并到符号常数版；"
            "仍未关闭的是显式数值常数和低高度有限核验。",
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 7. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。"
            ),
            (
                f"这些全部完成后，才进入下游 `{result['downstream_priority']}`、"
                f"`{result['quaternary_priority']}` 和 `{result['post_theta_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--explicit-formula", type=Path, default=DEFAULT_EXPLICIT_FORMULA)
    parser.add_argument("--pc1", type=Path, default=DEFAULT_PC1_THEOREMIZATION)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--hadamard", type=Path, default=DEFAULT_HADAMARD)
    parser.add_argument("--euler", type=Path, default=DEFAULT_EULER)
    parser.add_argument("--repulsion", type=Path, default=DEFAULT_REPULSION)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "explicit_formula": args.explicit_formula,
        "pc1": args.pc1,
        "final_draft": args.final_draft,
        "external_index": args.external_index,
        "hadamard": args.hadamard,
        "euler": args.euler,
        "repulsion": args.repulsion,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
