"""审计 MFAC W1 到 W2 的最小无条件 Chebyshev 能量桥合同。"""

import argparse
import json
from math import isfinite
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json"
)
DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md"
)

FORBIDDEN_INPUTS = frozenset(
    {
        "Chebyshev_error",
        "psi(X)-X",
        "target_energy",
        "Mellin",
        "zero_free_region",
        "zeta_zero",
        "explicit_formula",
        "RH",
        "PNT",
        "Mertens_cancellation",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {
        "w2_actual_chebyshev_energy_bridge",
        "w2_closed",
        "rh_proved",
        "target_energy_bound",
    }
)


def _require_mapping(value: object, field_name: str) -> Mapping[str, object]:
    """验证嵌套合同为 Mapping。"""
    if not isinstance(value, Mapping):
        raise ValueError(f"{field_name} 必须是 Mapping")
    return value


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """拒绝裸字符串、空字符串和非字符串依赖项。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _require_eta(value: object) -> float:
    """验证预注册可吸收常数 eta 位于 [0, 1)。"""
    if type(value) not in (int, float) or not isfinite(float(value)):
        raise ValueError("eta 必须是有限内建实数")
    eta = float(value)
    if not 0.0 <= eta < 1.0:
        raise ValueError("eta 必须位于 [0, 1)")
    return eta


def _check_noncyclic_sources(
    uses: tuple[str, ...],
    gram_uses: tuple[str, ...],
    error_uses: tuple[str, ...],
    claimed_bound_uses: tuple[str, ...],
) -> None:
    """拒绝目标/解析循环输入，并检查所有界来源已声明。"""
    declared = uses + gram_uses + error_uses
    forbidden = tuple(item for item in declared if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止输入：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed_bound_uses if item not in declared)
    if undeclared:
        raise ValueError(f"claimed_bound_uses 含未声明依赖：{', '.join(undeclared)}")


def audit_chebyshev_energy_bridge_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W1→W2 无条件桥接接口，绝不把合同升级为证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(
        field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract
    )
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    if contract.get("absolute_constant") != "exists_A_positive_independent_of_X_and_candidate":
        raise ValueError("absolute_constant 必须登记绝对常数 A")
    if contract.get("large_scale_quantifier") != "exists_X0_for_all_X_ge_X0":
        raise ValueError("large_scale_quantifier 必须登记所有充分大 X")
    gram = _require_mapping(contract.get("gram_contract"), "gram_contract")
    error = _require_mapping(contract.get("error_contract"), "error_contract")
    fields = ("coefficient_family", "kernel", "interval_correspondence", "constant_projection")
    if any(type(gram.get(field)) is not str or not gram[field] for field in fields):
        raise ValueError("gram_contract 缺少非空语义字段")
    if gram.get("nonnegative") is not True:
        raise ValueError("gram_contract.nonnegative 必须为 True")
    gram_uses = _checked_string_tuple(gram.get("uses"), "gram_contract.uses")
    if type(error.get("source")) is not str or not error["source"]:
        raise ValueError("error_contract.source 必须是非空字符串")
    eta = _require_eta(error.get("eta"))
    if error.get("absorption_target") != "B(X)<=eta*G(X)":
        raise ValueError("absorption_target 必须是 B(X)<=eta*G(X)")
    error_uses = _checked_string_tuple(error.get("uses"), "error_contract.uses")
    claimed_bound_uses = _checked_string_tuple(
        contract.get("claimed_bound_uses", ()), "claimed_bound_uses"
    )
    _check_noncyclic_sources(uses, gram_uses, error_uses, claimed_bound_uses)
    return {
        "bridge_uses": uses,
        "gram_uses": gram_uses,
        "error_uses": error_uses,
        "claimed_bound_uses": claimed_bound_uses,
        "eta": eta,
        "forbidden_input_check": "passed",
        "bridge_structure_status": "registered_unproved_contract",
        "absolute_constant_status": "registered_unproved",
        "large_scale_quantifier_status": "registered_unproved",
        "gram_nonnegativity_status": "declared_not_proved",
        "error_absorption_status": "absorption_obligation_open",
        "w2_actual_chebyshev_energy_bridge_status": "unproved",
        "rh_proved": False,
    }


def default_contract(eta: object) -> dict[str, object]:
    """返回只登记独立有限来源的默认最小桥接合同。"""
    return {
        "uses": (
            "finite_gram_identity",
            "independent_kernel_registration",
        ),
        "absolute_constant": "exists_A_positive_independent_of_X_and_candidate",
        "large_scale_quantifier": "exists_X0_for_all_X_ge_X0",
        "gram_contract": {
            "coefficient_family": "pre_registered_actual_coefficients",
            "kernel": "pre_registered_nonnegative_gram_kernel",
            "interval_correspondence": "dyadic_X_to_2X",
            "constant_projection": "off_constant_projection",
            "nonnegative": True,
            "uses": ("finite_gram_identity",),
        },
        "error_contract": {
            "source": "independent_remainder_decomposition",
            "eta": eta,
            "absorption_target": "B(X)<=eta*G(X)",
            "uses": ("independent_remainder_decomposition",),
        },
        "claimed_bound_uses": ("finite_gram_identity",),
    }


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出最小桥接合同证书，并保留未证明边界。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(
        "# MFAC W1→W2 最小无条件 Chebyshev 能量桥合同\n\n"
        "- 目标：`E(X)=integral_X^(2X)|psi(t)-t|^2 dt`\n"
        "- 桥接量词：存在绝对常数 `A>0` 与 `X0`，对所有 `X>=X0` 登记。\n"
        f"- 预注册误差吸收参数：`eta={certificate['eta']}`\n\n"
        "```text\n"
        "bridge_structure_status=registered_unproved_contract\n"
        "gram_nonnegativity_status=declared_not_proved\n"
        "error_absorption_status=absorption_obligation_open\n"
        "w2_actual_chebyshev_energy_bridge_status=unproved\n"
        "rh_proved=false\n"
        "```\n\n"
        "本合同不计算 psi，不证明 Gram 的实际构造或非负性，不证明误差吸收，"
        "不证明 W2、Mellin、零自由区域或 RH。\n",
        encoding="utf-8",
    )


def main() -> None:
    """生成 W1→W2 最小无条件桥接合同证书。"""
    parser = argparse.ArgumentParser(
        description="生成 MFAC W1 到 W2 Chebyshev 能量桥合同"
    )
    parser.add_argument("--eta", type=float, default=0.5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = audit_chebyshev_energy_bridge_contract(default_contract(args.eta))
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
