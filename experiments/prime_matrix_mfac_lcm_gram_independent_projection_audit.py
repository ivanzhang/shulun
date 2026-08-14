"""审计 MFAC 独立投影—LCM Gram 恒等式合同。"""

import argparse
import json
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.md")

FORBIDDEN_INPUTS = frozenset({"Chebyshev_error", "psi(X)-X", "Lambda(n)-1", "target_energy", "Mellin", "zero_free_region", "zeta_zero", "explicit_formula", "RH", "PNT", "Mertens_cancellation"})
FORBIDDEN_CONCLUSION_FIELDS = frozenset({"actual_chebyshev_projection", "residual_control", "w2_closed", "rh_proved", "projection_identity_proved"})

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


def _check_sources(uses: tuple[str, ...], projection_uses: tuple[str, ...], gram_uses: tuple[str, ...], claimed: tuple[str, ...]) -> None:
    """拒绝循环输入，并要求恒等式来源已预先声明。"""
    declared = uses + projection_uses + gram_uses
    forbidden = tuple(item for item in declared if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止输入：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed if item not in declared)
    if undeclared:
        raise ValueError(f"claimed_identity_uses 含未声明依赖：{', '.join(undeclared)}")


def audit_lcm_gram_independent_projection_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记独立投影—LCM Gram 接口，绝不把它升级为证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    forbidden_fields = tuple(field for field in FORBIDDEN_CONCLUSION_FIELDS if field in contract)
    if forbidden_fields:
        raise ValueError(f"contract 含目标结论循环字段：{', '.join(forbidden_fields)}")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    projection = _require_mapping(contract.get("projection_contract"), "projection_contract")
    gram = _require_mapping(contract.get("gram_contract"), "gram_contract")
    required = {"space": "L2([X,2X])", "quantifier": "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX", "feature_independence": "registered_independent_of_chebyshev_target"}
    if any(projection.get(key) != value for key, value in required.items()):
        raise ValueError("projection_contract 含错误空间、量词或独立性声明")
    for field in ("feature_family", "constant_projection"):
        if type(projection.get(field)) is not str or not projection[field]:
            raise ValueError("projection_contract 缺少非空语义字段")
    if projection.get("closed_subspace") is not True or projection.get("orthogonal_projection") is not True:
        raise ValueError("projection_contract 必须声明闭子空间和正交投影")
    projection_uses = _checked_string_tuple(projection.get("uses"), "projection_contract.uses")
    for field in ("kernel", "coefficient_coordinates", "normalization", "constant_projection"):
        if type(gram.get(field)) is not str or not gram[field]:
            raise ValueError("gram_contract 缺少非空语义字段")
    if gram.get("lcm_overlap") != "registered_lcm_divisibility_overlap":
        raise ValueError("gram_contract.lcm_overlap 必须登记实际 LCM overlap")
    if gram["constant_projection"] != projection["constant_projection"]:
        raise ValueError("两个 constant_projection 必须一致")
    gram_uses = _checked_string_tuple(gram.get("uses"), "gram_contract.uses")
    claimed = _checked_string_tuple(contract.get("claimed_identity_uses", ()), "claimed_identity_uses")
    _check_sources(uses, projection_uses, gram_uses, claimed)
    return {"uses": uses, "projection_uses": projection_uses, "gram_uses": gram_uses, "claimed_identity_uses": claimed, "forbidden_input_check": "passed", "projection_space_status": "registered_unproved", "lcm_gram_identity_status": "registered_unproved", "finite_normalization_status": "not_used_as_proof", "actual_chebyshev_projection_status": "not_started", "residual_control_status": "not_started", "w2_actual_chebyshev_energy_bridge_status": "unproved", "rh_proved": False}


def default_contract() -> dict[str, object]:
    """返回不读取 Chebyshev 数据的默认独立投影合同。"""
    return {
        "uses": ("finite_lcm_overlap_identity", "independent_feature_registration"),
        "projection_contract": {
            "space": "L2([X,2X])",
            "quantifier": "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX",
            "feature_family": "independent_divisibility_features",
            "feature_independence": "registered_independent_of_chebyshev_target",
            "closed_subspace": True,
            "orthogonal_projection": True,
            "constant_projection": "off_constant_projection",
            "uses": ("finite_lcm_overlap_identity",),
        },
        "gram_contract": {
            "kernel": "registered_lcm_gram_kernel",
            "coefficient_coordinates": "projection_coordinates",
            "normalization": "dyadic_L2_normalization",
            "lcm_overlap": "registered_lcm_divisibility_overlap",
            "constant_projection": "off_constant_projection",
            "uses": ("finite_lcm_overlap_identity",),
        },
        "claimed_identity_uses": ("finite_lcm_overlap_identity",),
    }


def write_certificate(certificate: Mapping[str, object], json_path: Path, markdown_path: Path) -> None:
    """写出独立投影合同证书，并保留所有未证明边界。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    markdown_path.write_text(
        "# MFAC LCM Gram 独立投影恒等式合同\n\n"
        "- 空间：`L2([X,2X])`\n"
        "- 量词：对所有充分大实数 `X` 与所有 `f in H_X` 登记。\n"
        "- 特征族：独立于 Chebyshev 目标。\n\n"
        "```text\nprojection_space_status=registered_unproved\n"
        "lcm_gram_identity_status=registered_unproved\n"
        "actual_chebyshev_projection_status=not_started\n"
        "residual_control_status=not_started\n"
        "w2_actual_chebyshev_energy_bridge_status=unproved\n"
        "rh_proved=false\n```\n\n"
        "本合同不证明正交投影存在、LCM Gram 恒等式、Chebyshev 映射、残差、W2 或 RH。\n",
        encoding="utf-8",
    )


def main() -> None:
    """生成独立投影—LCM Gram 合同证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC LCM Gram 独立投影合同")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    write_certificate(audit_lcm_gram_independent_projection_contract(default_contract()), args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
