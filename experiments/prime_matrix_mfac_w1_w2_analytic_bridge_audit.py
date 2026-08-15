"""审计 MFAC W1→W2 解析桥的外部证明包合同。"""

import argparse
import json
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.md")
REQUIRED_LEMMAS = (
    "tail_l2_upper",
    "coprime_restricted_tail_bound",
    "euler_phi_aggregation",
    "chebyshev_transfer",
)
FORBIDDEN_INPUTS = frozenset(
    {
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin",
        "Chebyshev_error",
        "target_energy_bridge",
        "chebyshev_energy_bridge",
        "finite_profile",
        "numerical_experiment",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {
        "chebyshev_energy_bridge_proved",
        "w2_closed",
        "rh_proved",
        "rh_consequence",
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
    """要求指定解析引理以内建真值形式登记。"""
    if type(contract.get(field_name)) is not bool or contract[field_name] is not True:
        raise ValueError(f"{field_name} 必须是内建 True")


def _validate_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """验证非循环的 W1→W2 外部解析证明包声明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(
        field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract
    )
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")

    uses = _checked_string_tuple(contract.get("uses"), "uses")
    claimed_bridge_uses = _checked_string_tuple(
        contract.get("claimed_bridge_uses", ()), "claimed_bridge_uses"
    )
    forbidden = tuple(item for item in uses if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden)}")
    forbidden_claimed = tuple(
        item for item in claimed_bridge_uses if item in FORBIDDEN_INPUTS
    )
    if forbidden_claimed:
        raise ValueError(
            f"claimed_bridge_uses 含禁止循环依赖：{', '.join(forbidden_claimed)}"
        )
    undeclared = tuple(item for item in claimed_bridge_uses if item not in uses)
    if undeclared:
        raise ValueError(
            f"claimed_bridge_uses 含未声明依赖：{', '.join(undeclared)}"
        )
    for field_name in REQUIRED_LEMMAS:
        _require_builtin_true(contract, field_name)
    if contract.get("uniformity_variable") != "truncation":
        raise ValueError("uniformity_variable 必须是 truncation")
    if contract.get("constant_dependency") != "fixed_test_function":
        raise ValueError("constant_dependency 必须是 fixed_test_function")
    return {
        "uses": uses,
        "claimed_bridge_uses": claimed_bridge_uses,
        "required_lemmas": REQUIRED_LEMMAS,
        "uniformity_variable": "truncation",
        "constant_dependency": "fixed_test_function",
    }


def audit_w1_w2_analytic_bridge(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W1→W2 外部解析证明包，绝不提升为定理结论。"""
    checked = _validate_contract(contract)
    return {
        **checked,
        "forbidden_dependency_check": "passed",
        "tail_l2_upper_status": "externally_assumed",
        "coprime_restricted_tail_bound_status": "externally_assumed",
        "euler_phi_aggregation_status": "externally_assumed",
        "chebyshev_transfer_status": "externally_assumed",
        "w1_to_w2_status": "assumption_chain_registered",
        "chebyshev_energy_bridge_status": "unproved",
        "rh_proved": False,
    }


def default_contract() -> dict[str, object]:
    """返回只登记外部解析证明包的默认合法合同。"""
    return {
        "uses": (
            "tail_l2_upper_lemma",
            "coprime_restricted_tail_bound_lemma",
            "euler_phi_aggregation_lemma",
            "chebyshev_transfer_lemma",
        ),
        "tail_l2_upper": True,
        "coprime_restricted_tail_bound": True,
        "euler_phi_aggregation": True,
        "chebyshev_transfer": True,
        "uniformity_variable": "truncation",
        "constant_dependency": "fixed_test_function",
        "claimed_bridge_uses": (
            "tail_l2_upper_lemma",
            "coprime_restricted_tail_bound_lemma",
            "euler_phi_aggregation_lemma",
            "chebyshev_transfer_lemma",
        ),
    }


def _render_markdown(payload: Mapping[str, object]) -> str:
    """渲染明确保留未证明边界的人读证书。"""
    uses = ", ".join(f"`{item}`" for item in payload["uses"])
    lemmas = "\n".join(f"- `{item}`：外部证明包已登记。" for item in REQUIRED_LEMMAS)
    return f"""# MFAC W1→W2 解析桥合同审计

## 已登记输入

- 声明来源：{uses}
- 截断统一性变量：`{payload['uniformity_variable']}`
- 常数依赖：`{payload['constant_dependency']}`

## 外部解析引理

{lemmas}

## 状态边界

```text
w1_to_w2_status={payload['w1_to_w2_status']}
chebyshev_energy_bridge_status={payload['chebyshev_energy_bridge_status']}
rh_proved=false
```

本证书仅登记外部解析证明包及其防循环合同；它不证明 Möbius 尾和 L²--Upper、
互素限制尾和界、Euler--φ 聚合、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py
```
"""


def write_certificate(
    payload: Mapping[str, object], json_out: Path, markdown_out: Path
) -> None:
    """写出机器证书和包含未证明边界的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_out.write_text(_render_markdown(payload), encoding="utf-8")


def main() -> None:
    """运行默认合同并写出 JSON、Markdown 审计证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC W1→W2 解析桥合同证书")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    payload = audit_w1_w2_analytic_bridge(default_contract())
    write_certificate(payload, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
