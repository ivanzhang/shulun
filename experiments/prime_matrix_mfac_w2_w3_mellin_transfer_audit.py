"""审计 MFAC W2→W3 实际 Mellin 传递的外部证明包合同。"""

import argparse
import json
from math import isfinite
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.md")
REQUIRED_LEMMAS = (
    "actual_dyadic_chebyshev_energy_bound",
    "dyadic_scale_partition",
    "weighted_scale_summability",
    "mellin_plancherel_transfer",
)
FORBIDDEN_INPUTS = frozenset(
    {
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin_contraction",
        "target_mellin_bound",
        "w3_spectral_contraction",
        "finite_profile",
        "numerical_experiment",
        "free_multiplicative_model",
        "Mertens_cancellation",
        "PNT",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {
        "rh_proved",
        "w3_closed",
        "actual_mellin_half_plane_contraction",
        "mellin_transfer_proved",
    }
)


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证字符串序列，拒绝裸字符串和非字符串元素。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _require_builtin_true(contract: Mapping[str, object], field_name: str) -> None:
    """要求指定外部解析引理以内建真值形式登记。"""
    if type(contract.get(field_name)) is not bool or contract[field_name] is not True:
        raise ValueError(f"{field_name} 必须是内建 True")


def _require_half_plane_parameter(value: object) -> float:
    """验证半平面参数严格位于开区间 (1/2, 1)。"""
    if type(value) not in (int, float) or not isfinite(float(value)):
        raise ValueError("half_plane_parameter 必须是有限内建实数")
    parameter = float(value)
    if not 0.5 < parameter < 1.0:
        raise ValueError("half_plane_parameter 必须位于 (1/2, 1)")
    return parameter


def _validate_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """验证 W2→W3 的非循环外部 Mellin 传递证明包。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(
        field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract
    )
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")

    uses = _checked_string_tuple(contract.get("uses"), "uses")
    if not uses:
        raise ValueError("uses 不能为空")
    claimed_transfer_uses = _checked_string_tuple(
        contract.get("claimed_transfer_uses", ()), "claimed_transfer_uses"
    )
    forbidden_uses = tuple(item for item in uses if item in FORBIDDEN_INPUTS)
    if forbidden_uses:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden_uses)}")
    forbidden_claimed = tuple(
        item for item in claimed_transfer_uses if item in FORBIDDEN_INPUTS
    )
    if forbidden_claimed:
        raise ValueError(
            "claimed_transfer_uses 含禁止循环依赖："
            f"{', '.join(forbidden_claimed)}"
        )
    undeclared = tuple(item for item in claimed_transfer_uses if item not in uses)
    if undeclared:
        raise ValueError(
            f"claimed_transfer_uses 含未声明依赖：{', '.join(undeclared)}"
        )
    for field_name in REQUIRED_LEMMAS:
        _require_builtin_true(contract, field_name)
    if contract.get("actual_error_object") != "psi_minus_identity":
        raise ValueError("actual_error_object 必须是 psi_minus_identity")
    if contract.get("dyadic_scale_variable") != "X_to_2X":
        raise ValueError("dyadic_scale_variable 必须是 X_to_2X")
    if contract.get("mellin_measure") != "dt_over_t_squared":
        raise ValueError("mellin_measure 必须是 dt_over_t_squared")
    if (
        contract.get("constant_dependency")
        != "fixed_test_function_and_half_plane_parameter"
    ):
        raise ValueError(
            "constant_dependency 必须是 "
            "fixed_test_function_and_half_plane_parameter"
        )
    return {
        "uses": uses,
        "claimed_transfer_uses": claimed_transfer_uses,
        "required_lemmas": REQUIRED_LEMMAS,
        "actual_error_object": "psi_minus_identity",
        "dyadic_scale_variable": "X_to_2X",
        "mellin_measure": "dt_over_t_squared",
        "half_plane_parameter": _require_half_plane_parameter(
            contract.get("half_plane_parameter")
        ),
        "constant_dependency": "fixed_test_function_and_half_plane_parameter",
    }


def audit_w2_w3_mellin_transfer(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W2→W3 外部传递证明包，绝不提升为 W3 或 RH 结论。"""
    checked = _validate_contract(contract)
    return {
        **checked,
        "forbidden_dependency_check": "passed",
        "actual_dyadic_chebyshev_energy_bound_status": "externally_assumed",
        "dyadic_scale_partition_status": "externally_assumed",
        "weighted_scale_summability_status": "externally_assumed",
        "mellin_plancherel_transfer_status": "externally_assumed",
        "w2_to_w3_status": "assumption_chain_registered",
        "actual_mellin_half_plane_contraction_status": "unproved",
        "w3_spectral_contraction_status": "unproved",
        "rh_proved": False,
    }


def default_contract(half_plane_parameter: float = 0.75) -> dict[str, object]:
    """返回只登记实际 Mellin 传递证明包的默认合法合同。"""
    return {
        "uses": (
            "actual_dyadic_chebyshev_energy_bound_lemma",
            "dyadic_scale_partition_lemma",
            "weighted_scale_summability_lemma",
            "mellin_plancherel_transfer_lemma",
        ),
        "actual_dyadic_chebyshev_energy_bound": True,
        "dyadic_scale_partition": True,
        "weighted_scale_summability": True,
        "mellin_plancherel_transfer": True,
        "actual_error_object": "psi_minus_identity",
        "dyadic_scale_variable": "X_to_2X",
        "mellin_measure": "dt_over_t_squared",
        "half_plane_parameter": half_plane_parameter,
        "constant_dependency": "fixed_test_function_and_half_plane_parameter",
        "claimed_transfer_uses": (
            "actual_dyadic_chebyshev_energy_bound_lemma",
            "dyadic_scale_partition_lemma",
            "weighted_scale_summability_lemma",
            "mellin_plancherel_transfer_lemma",
        ),
    }


def _render_markdown(payload: Mapping[str, object]) -> str:
    """渲染明确保留 W3/RH 未证明边界的人读证书。"""
    uses = ", ".join(f"`{item}`" for item in payload["uses"])
    lemmas = "\n".join(f"- `{item}`：外部证明包已登记。" for item in REQUIRED_LEMMAS)
    return f"""# MFAC W2→W3 实际 Mellin 传递合同审计

## 已登记输入

- 声明来源：{uses}
- 实际误差对象：`{payload['actual_error_object']}`
- dyadic 尺度变量：`{payload['dyadic_scale_variable']}`
- Mellin 测度：`{payload['mellin_measure']}`
- 半平面参数：`{payload['half_plane_parameter']}`
- 常数依赖：`{payload['constant_dependency']}`

## 外部解析引理

{lemmas}

## 状态边界

```text
w2_to_w3_status={payload['w2_to_w3_status']}
actual_mellin_half_plane_contraction_status={payload['actual_mellin_half_plane_contraction_status']}
w3_spectral_contraction_status={payload['w3_spectral_contraction_status']}
rh_proved=false
```

本证书只登记实际 dyadic 能量至 Mellin 半平面范数的外部证明包；它不证明
Chebyshev 能量界、尺度可和性、Mellin/Plancherel 传递、半平面收缩、零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py \\
  --half-plane-parameter 0.75
```
"""


def write_certificate(
    payload: Mapping[str, object], json_out: Path, markdown_out: Path
) -> None:
    """写出机器证书和显式保留未证明边界的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_out.write_text(_render_markdown(payload), encoding="utf-8")


def main() -> None:
    """运行默认合同并写出 JSON、Markdown 审计证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC W2→W3 实际 Mellin 传递合同证书")
    parser.add_argument("--half-plane-parameter", type=float, default=0.75)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    payload = audit_w2_w3_mellin_transfer(
        default_contract(args.half_plane_parameter)
    )
    write_certificate(payload, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
