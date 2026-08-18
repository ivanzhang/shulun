"""审计全 epsilon Mertens 条件化 L2--Upper 的依赖边界。"""

import argparse
import json
from math import isfinite
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.json"
)
DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.md"
)
REQUIRED_USES = frozenset(
    {
        "finite_divisor_identity",
        "euler_phi_identity",
        "Mertens_cancellation",
        "partial_summation",
        "coprimality_inclusion_exclusion",
    }
)
OPEN_OBLIGATIONS = (
    "CoprimeRestrictedPartialSummation",
    "TailBoundWithParameterDependence",
    "EulerPhiL2Aggregation",
)
FORBIDDEN_CYCLIC_USES = frozenset(
    {
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin",
        "target_l2_upper",
        "unconditional_l2_upper",
    }
)


def _require_positive_builtin_real(value: object, field_name: str) -> float:
    """验证单 epsilon 实例化使用的有限正内建实数。"""
    if type(value) not in (int, float) or not isfinite(float(value)):
        raise ValueError(f"{field_name} 必须是有限内建实数")
    checked = float(value)
    if checked <= 0.0:
        raise ValueError(f"{field_name} 必须严格为正")
    return checked


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """拒绝裸字符串、空字符串和非字符串依赖项。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _check_noncyclic_dependencies(
    uses: tuple[str, ...], claimed_bound_uses: tuple[str, ...]
) -> None:
    """拒绝循环输入，并确保所有界来源已经在合同中声明。"""
    forbidden = tuple(item for item in uses if item in FORBIDDEN_CYCLIC_USES)
    if forbidden:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed_bound_uses if item not in uses)
    if undeclared:
        raise ValueError(f"claimed_bound_uses 含未声明依赖：{', '.join(undeclared)}")


def audit_mertens_all_epsilon_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记全 epsilon Mertens 条件链，不把它升级为解析证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    claimed_bound_uses = _checked_string_tuple(
        contract.get("claimed_bound_uses", ()), "claimed_bound_uses"
    )
    _check_noncyclic_dependencies(uses, claimed_bound_uses)
    if not REQUIRED_USES.issubset(uses):
        raise ValueError("uses 缺少全 epsilon 条件链所需依赖")
    if contract.get("for_every_epsilon") is not True:
        raise ValueError("for_every_epsilon 必须为 True")
    if contract.get("epsilon_domain") != "positive_real":
        raise ValueError("epsilon_domain 必须是 positive_real")
    if contract.get("assumption") != "M(x)=O_epsilon(x^(1/2+epsilon))":
        raise ValueError("assumption 必须是标准全 epsilon Mertens 型界")
    if contract.get("constant_dependency") != "C_epsilon_depends_on_epsilon_only":
        raise ValueError("constant_dependency 必须限定为仅依赖 epsilon")
    if contract.get("uniform_in_epsilon") is not False:
        raise ValueError("uniform_in_epsilon 必须为 False")
    epsilon = _require_positive_builtin_real(contract.get("epsilon"), "epsilon")
    mertens_constant = _require_positive_builtin_real(
        contract.get("mertens_constant"), "mertens_constant"
    )
    return {
        "uses": uses,
        "claimed_bound_uses": claimed_bound_uses,
        "forbidden_dependency_check": "passed",
        "mertens_assumption_status": "externally_assumed",
        "epsilon_quantifier": "for_every_positive_epsilon",
        "epsilon_instance": epsilon,
        "mertens_constant_instance": mertens_constant,
        "constant_uniform_in_epsilon": False,
        "open_obligations": OPEN_OBLIGATIONS,
        "conditional_l2_upper_status": "assumption_chain_registered",
        "unconditional_l2_upper_status": "unproved",
        "rh_proved": False,
    }


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出条件链证书，明确不构成无条件解析结论。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(
        "# MFAC 全 epsilon Mertens 条件化 L2--Upper 审计\n\n"
        f"- 单实例：`epsilon={certificate['epsilon_instance']}`\n"
        "- 全称量词：`for_every_positive_epsilon`\n"
        "- 常数：`C_epsilon` 仅可依赖当前 epsilon，且不要求 epsilon 一致。\n\n"
        "```text\n"
        "mertens_assumption_status=externally_assumed\n"
        "conditional_l2_upper_status=assumption_chain_registered\n"
        "unconditional_l2_upper_status=unproved\n"
        "rh_proved=false\n"
        "```\n\n"
        "互素限制分部求和、带参数尾和界和 Euler--phi L2 聚合仍是开放证明义务；"
        "本证书不证明 Mertens 型界、Mass--Lower、Chebyshev 能量桥、Mellin 收缩、"
        "零自由区域或 RH。\n",
        encoding="utf-8",
    )


def main() -> None:
    """生成默认全 epsilon Mertens 条件链审计证书。"""
    parser = argparse.ArgumentParser(
        description="生成 MFAC 全 epsilon Mertens 条件化 L2 审计"
    )
    parser.add_argument("--epsilon", type=float, default=0.1)
    parser.add_argument("--mertens-constant", type=float, default=1.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = audit_mertens_all_epsilon_contract(
        {
            "uses": (
                "finite_divisor_identity",
                "euler_phi_identity",
                "Mertens_cancellation",
                "partial_summation",
                "coprimality_inclusion_exclusion",
            ),
            "for_every_epsilon": True,
            "epsilon_domain": "positive_real",
            "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
            "constant_dependency": "C_epsilon_depends_on_epsilon_only",
            "uniform_in_epsilon": False,
            "epsilon": args.epsilon,
            "mertens_constant": args.mertens_constant,
            "claimed_bound_uses": (),
        }
    )
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
