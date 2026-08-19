# MFAC Möbius 尾和整体 L² 门槛审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将固定线性截断 Möbius--log 系数族的极限核能量改写为 Euler--\(\varphi\) 平方和，分别审计分母质量、整体 Möbius 尾和 L² 分子及其外部依赖边界；所有输出保持有限数值诊断或明确条件命题，不宣称 RH 结论。

**Architecture:** 新模块只以截断上界 `D` 为参数，复用既有 `mobius_value` 与线性窗口定义，但不写入有限 `X` 协方差证书。它以 `Fraction` 验证纯有理 Euler--\(\varphi\) 恒等式，以浮点计算含 `log` 的目标系数族；分母和分子分别输出。任何声称 `E_D << log(D)^2` 的输入必须经过 `uses` 合同，未声明的 PNT/Mertens/零点/Mellin 类输入被拒绝。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`typing`、`unittest`）；复用 `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py`。

**Design Source:** `docs/superpowers/specs/2026-08-12-mfac-mobius-tail-l2-barrier-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py`
  - Euler--\(\varphi\) 分解、目标尾和、质量/能量有限剖面、`uses` 合同、CLI 证书。
- Create: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`
  - 精确恒等式、尾和公式、质量/能量诊断、依赖拒绝、证书边界和 CLI 测试。
- Create: `docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.json`
  - 默认有限尺度证书。
- Create: `docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.md`
  - 人读证书，明确 L2--Upper 未证明及依赖边界。

不修改现有 `AGENTS.md`，不改变截断 Möbius--log 主审计器的接口，不创建提交。

### Task 1: 写出 Euler--\(\varphi\) 精确恒等式红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 添加小有理系数的核/平方和一致性测试**

```python
from fractions import Fraction
import unittest

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import (
    euler_phi_square_energy,
    limit_kernel_energy,
)


class MFACMobiusTailL2AuditTest(unittest.TestCase):
    """验证 Möbius 尾和 L² 门槛的有限代数恒等式。"""

    def test_euler_phi_square_sum_matches_limit_kernel_for_rational_coefficients(self) -> None:
        """Euler--phi 平方和必须精确等于极限核二次型。"""
        coefficients = {
            2: Fraction(3, 2),
            3: Fraction(-2, 3),
            6: Fraction(5, 7),
        }
        self.assertEqual(
            limit_kernel_energy(coefficients),
            euler_phi_square_energy(coefficients),
        )
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test.MFACMobiusTailL2AuditTest.test_euler_phi_square_sum_matches_limit_kernel_for_rational_coefficients -v`

Expected: FAIL，原因是新审计模块尚不存在。

### Task 2: 实现纯有限 Euler--\(\varphi\) 分解

**Files:**
- Create: `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 实现整数验证、\(\varphi\) 与有理极限核**

```python
from fractions import Fraction
from math import gcd
from typing import Mapping


def euler_phi(index: object) -> int:
    """以有限试除法计算 Euler phi，用于精确代数审计。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    value = index
    remaining = index
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            value -= value // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        value -= value // remaining
    return value


def limit_kernel_energy(coefficients: Mapping[int, Fraction]) -> Fraction:
    """以精确有理数计算 sum a_d a_e ((d,e)-1)/(de)。"""
    checked = _checked_fraction_coefficients(coefficients)
    return sum(
        left_value * right_value * Fraction(gcd(left, right) - 1, left * right)
        for left, left_value in checked.items()
        for right, right_value in checked.items()
    )
```

- [ ] **Step 2: 实现尾和与 Euler--\(\varphi\) 平方和**

```python
def divisor_tail_sum(coefficients: Mapping[int, Fraction], divisor: int) -> Fraction:
    """返回 T(r)=sum_{r|d} a_d/d 的精确有限尾和。"""
    checked = _checked_fraction_coefficients(coefficients)
    if type(divisor) is not int or divisor < 2:
        raise ValueError("divisor 必须是至少为 2 的内建整数")
    return sum(value / index for index, value in checked.items() if index % divisor == 0)


def euler_phi_square_energy(coefficients: Mapping[int, Fraction]) -> Fraction:
    """以 sum_{r>=2} phi(r) T(r)^2 计算极限核能量。"""
    checked = _checked_fraction_coefficients(coefficients)
    cutoff = max(checked)
    return sum(
        Fraction(euler_phi(divisor), 1) * divisor_tail_sum(checked, divisor) ** 2
        for divisor in range(2, cutoff + 1)
    )
```

- [ ] **Step 3: 运行 Task 1 测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test -v`

Expected: PASS。

### Task 3: 写出目标 Möbius 尾和与浮点分解红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 添加平方自由展开和浮点能量一致性测试**

```python
import math

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import (
    euler_phi_square_energy_float,
    mobius_log_tail_sum,
    truncated_mobius_log_limit_coefficients,
)


    def test_squarefree_tail_formula_agrees_with_direct_divisor_tail(self) -> None:
        """平方自由 r 的闭式 Möbius 尾和必须匹配直接因子求和。"""
        cutoff = 64
        coefficients = truncated_mobius_log_limit_coefficients(cutoff)
        self.assertAlmostEqual(
            mobius_log_tail_sum(cutoff, 6),
            sum(value / index for index, value in coefficients.items() if index % 6 == 0),
            places=12,
        )
        self.assertEqual(mobius_log_tail_sum(cutoff, 4), 0.0)

    def test_float_euler_phi_energy_matches_direct_limit_kernel(self) -> None:
        """含 log 的浮点系数也必须保留可报告的代数残差。"""
        coefficients = truncated_mobius_log_limit_coefficients(64)
        direct = limit_kernel_energy_float(coefficients)
        decomposed = euler_phi_square_energy_float(coefficients)
        self.assertGreater(direct, 0.0)
        self.assertAlmostEqual(direct, decomposed, places=10)
        self.assertTrue(math.isfinite(decomposed))
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test.MFACMobiusTailL2AuditTest.test_squarefree_tail_formula_agrees_with_direct_divisor_tail -v`

Expected: FAIL，原因是浮点目标系数与尾和函数尚未定义。

### Task 4: 实现目标系数、尾和与有限 L² 剖面

**Files:**
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 复用已审计 Möbius 并实现 `D` 参数系数族**

```python
from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    mobius_value,
)


def truncated_mobius_log_limit_coefficients(cutoff: object) -> dict[int, float]:
    """构造 a_D(d)，其中 D=cutoff，且只返回 2<=d<D 的非零浮点系数。"""
    checked_cutoff = _require_cutoff(cutoff)
    logarithmic_cutoff = log(float(checked_cutoff))
    return {
        index: -mobius * log(float(index)) * (1.0 - log(float(index)) / logarithmic_cutoff)
        for index in range(2, checked_cutoff)
        if (mobius := mobius_value(index)) != 0
    }
```

- [ ] **Step 2: 实现平方自由闭式尾和与浮点平方和**

```python
def mobius_log_tail_sum(cutoff: object, divisor: object) -> float:
    """返回目标系数族的 T_D(r)；非平方自由 r 精确返回 0.0。"""
    checked_cutoff = _require_cutoff(cutoff)
    if type(divisor) is not int or not 2 <= divisor < checked_cutoff:
        raise ValueError("divisor 必须是位于 [2, cutoff) 的内建整数")
    if mobius_value(divisor) == 0:
        return 0.0
    logarithmic_cutoff = log(float(checked_cutoff))
    return -mobius_value(divisor) / divisor * sum(
        mobius_value(multiplier)
        * log(float(divisor * multiplier))
        / multiplier
        * (1.0 - log(float(divisor * multiplier)) / logarithmic_cutoff)
        for multiplier in range(1, checked_cutoff // divisor + 1)
        if divisor * multiplier < checked_cutoff
        and gcd(divisor, multiplier) == 1
    )


def euler_phi_square_energy_float(coefficients: Mapping[int, float]) -> float:
    """以浮点系数计算 Euler--phi 分解能量，供有限诊断使用。"""
    checked = _checked_float_coefficients(coefficients)
    cutoff = max(checked) + 1
    return sum(
        euler_phi(divisor)
        * sum(value / index for index, value in checked.items() if index % divisor == 0) ** 2
        for divisor in range(2, cutoff)
    )
```

- [ ] **Step 3: 实现有限剖面且明确保持 `numerical_only`**

```python
def audit_mobius_tail_l2(cutoff: object) -> dict[str, object]:
    """输出固定 D 的 L² 门槛数值诊断，不升级为 L2--Upper 定理。"""
    checked_cutoff = _require_cutoff(cutoff)
    coefficients = truncated_mobius_log_limit_coefficients(checked_cutoff)
    numerator = euler_phi_square_energy_float(coefficients)
    mass = sum(value * value / index for index, value in coefficients.items())
    return {
        "certificate_type": "prime_matrix_mfac_mobius_tail_l2_audit",
        "status": "numerical_only_mobius_tail_l2_profile",
        "cutoff": checked_cutoff,
        "coefficient_support_size": len(coefficients),
        "limit_kernel_energy": limit_kernel_energy_float(coefficients),
        "euler_phi_square_energy": numerator,
        "energy_identity_residual": abs(limit_kernel_energy_float(coefficients) - numerator),
        "mass": mass,
        "normalized_ratio": numerator / mass,
        "log_scaled_ratio": log(float(checked_cutoff)) * numerator / mass,
        "l2_upper_status": "unproved",
        "mass_lower_status": "unproved",
        "mobius_cancellation_dependency_status": "unresolved",
        "rh_proved": False,
    }
```

- [ ] **Step 4: 运行 Task 3 全部测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test -v`

Expected: PASS。

### Task 5: 写出 Möbius 消去依赖合同红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 添加未声明解析输入拒绝测试**

```python
from experiments.prime_matrix_mfac_mobius_tail_l2_audit import audit_l2_upper_contract


    def test_l2_contract_rejects_undeclared_mertens_and_zero_inputs(self) -> None:
        """L2--Upper 不得把 Mertens 或零点输入伪装成结构自足推导。"""
        independent = audit_l2_upper_contract(
            {"uses": ("finite_divisor_identity", "euler_phi_identity")}
        )
        self.assertEqual(independent["classification"], "no_external_mobius_estimate_declared")

        conditional = audit_l2_upper_contract(
            {"uses": ("Mertens_cancellation", "PNT")}
        )
        self.assertEqual(
            conditional["classification"],
            "conditional_on_named_mobius_estimate",
        )
        self.assertEqual(
            conditional["analytic_dependencies"],
            ("Mertens_cancellation", "PNT"),
        )

        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_l2_upper_contract(
                {"uses": ("finite_divisor_identity",), "claimed_bound_uses": ("Mellin",)}
            )
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test.MFACMobiusTailL2AuditTest.test_l2_contract_rejects_undeclared_mertens_and_zero_inputs -v`

Expected: FAIL，原因是合同审计函数尚未定义。

### Task 6: 实现依赖合同、证书与 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_mobius_tail_l2_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.md`

- [ ] **Step 1: 实现 `uses` 合同审计**

```python
ANALYTIC_MOBIUS_DEPENDENCIES = frozenset(
    {
        "PNT",
        "Mertens_cancellation",
        "zero_free_region",
        "zeta_zero",
        "explicit_formula",
        "Mellin",
        "RH",
    }
)


def audit_l2_upper_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """分类 L2--Upper 的外部 Möbius 消去依赖，不允许隐式读取。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = _checked_string_tuple(contract.get("uses", ()), "uses")
    claimed = _checked_string_tuple(contract.get("claimed_bound_uses", uses), "claimed_bound_uses")
    undeclared = tuple(sorted(set(claimed).difference(uses)))
    if undeclared:
        raise ValueError("claimed_bound_uses 含未声明输入: " + ", ".join(undeclared))
    dependencies = tuple(sorted(set(uses).intersection(ANALYTIC_MOBIUS_DEPENDENCIES)))
    return {
        "classification": (
            "conditional_on_named_mobius_estimate"
            if dependencies
            else "no_external_mobius_estimate_declared"
        ),
        "analytic_dependencies": dependencies,
    }
```

- [ ] **Step 2: 将合同结果接入有限审计与证书**

```python
def write_certificate(certificate: Mapping[str, object], json_path: Path, markdown_path: Path) -> None:
    """写出有限 L² 诊断，并明示解析上界尚未证明。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(
        "# MFAC Möbius 尾和整体 L² 有限审计\n\n"
        f"- 截断：`D={certificate['cutoff']}`\n"
        f"- 有限比率：`{certificate['normalized_ratio']}`\n"
        f"- log 缩放比率：`{certificate['log_scaled_ratio']}`\n"
        f"- Euler--phi 残差：`{certificate['energy_identity_residual']}`\n\n"
        "```text\n"
        "l2_upper_status=unproved\n"
        "mass_lower_status=unproved\n"
        "mobius_cancellation_dependency_status=unresolved\n"
        "rh_proved=false\n"
        "```\n\n"
        "该证书只验证有限代数分解与数值剖面；不构成 L2--Upper、Mass--Lower、"
        "统一强制性、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH 证明。\n",
        encoding="utf-8",
    )
```

- [ ] **Step 3: 实现仅接受 `--cutoff` 的 CLI 并生成默认产物**

```python
def main() -> None:
    """生成 Möbius 尾和 L² 门槛的有限证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC Möbius 尾和 L² 有限审计")
    parser.add_argument("--cutoff", type=int, default=4096)
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.json"),
    )
    parser.add_argument(
        "--markdown-out",
        type=Path,
        default=Path("docs/monograph/prime-matrix-mfac-mobius-tail-l2-audit.md"),
    )
    args = parser.parse_args()
    certificate = audit_mobius_tail_l2(args.cutoff)
    certificate["l2_upper_contract"] = audit_l2_upper_contract(
        {"uses": ("finite_divisor_identity", "euler_phi_identity")}
    )
    write_certificate(certificate, args.json_out, args.markdown_out)
```

- [ ] **Step 4: 添加证书和 CLI 测试并运行完整验证**

```python
    def test_certificate_never_promotes_l2_profile_to_theorem(self) -> None:
        """文件证书必须保留 L² 上界未证明与 RH 边界。"""
        with TemporaryDirectory() as directory:
            json_path = Path(directory) / "audit.json"
            markdown_path = Path(directory) / "audit.md"
            certificate = audit_mobius_tail_l2(64)
            certificate["l2_upper_contract"] = audit_l2_upper_contract(
                {"uses": ("finite_divisor_identity", "euler_phi_identity")}
            )
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["l2_upper_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不构成 L2--Upper", markdown_path.read_text(encoding="utf-8"))
```

Run: `python3 experiments/prime_matrix_mfac_mobius_tail_l2_audit.py --cutoff 4096 && python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test -v && python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v && git diff --check`

Expected: 默认 JSON/Markdown 生成；新测试和全量 MFAC 测试通过；证书含 `l2_upper_status=unproved` 与 `rh_proved=false`。若既有无关测试失败，只记录失败项，不修改无关模块。

- [ ] **Step 5: 检查范围，不提交**

Run: `git status --short && git diff --check`

Expected: 仅包含本计划声明的新模块、测试、证书与规格/计划，以及用户原有 `AGENTS.md` 修改；不执行 `git add` 或 `git commit`。
