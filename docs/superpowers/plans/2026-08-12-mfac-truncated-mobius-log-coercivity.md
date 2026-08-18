# MFAC 截断 Möbius--log 系数族强制性审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为固定线性截断的 Möbius--log 系数族生成可复算有限能量剖面、依赖合同与反例压力测试，同时严格保持其为 `numerical_only` 而非统一强制性或 RH 结论。

**Architecture:** 新审计器复用 `prime_matrix_mfac_centered_divisibility_covariance_audit.py` 的精确有理中心化核；系数中的 `log` 以浮点计算，因此模块显式分离“精确核恒等式”和“有限精度实际族评估”。审计器只接受预注册的 `linear` 窗口，计算直接平方和与协方差二次型的残差、归一化比率、禁止输入合同和对照见证；JSON/Markdown 证书永久标记为有限诊断。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`typing`、`unittest`）；现有 `experiments/` 审计与 `docs/monograph/` 证书模式。

**Design Source:** `docs/superpowers/specs/2026-08-12-mfac-truncated-mobius-log-coercivity-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py`
  - 固定截断系数、精确核驱动的有限能量、依赖合同、有限证书 CLI。
- Create: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`
  - 系数合同、平方和/二次型一致性、归一化与证书边界的单元测试。
- Create: `docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.json`
  - 默认有限尺度机器证书。
- Create: `docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.md`
  - 默认人读证书，明确不构成统一强制性或 RH 证明。

不修改 `AGENTS.md`，不创建提交；提交策略由用户另行决定。

### Task 1: 写出系数族与依赖合同的红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`

- [ ] **Step 1: 写出窗口、Möbius 系数和依赖合同测试**

```python
import math
import unittest

from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    audit_coefficient_contract,
    cutoff_from_theta,
    linear_window,
    truncated_mobius_log_coefficients,
)


class MFACTruncatedMobiusLogCoercivityAuditTest(unittest.TestCase):
    def test_linear_window_has_fixed_endpoints(self) -> None:
        self.assertEqual(linear_window(0.0), 1.0)
        self.assertEqual(linear_window(1.0), 0.0)
        self.assertAlmostEqual(linear_window(0.25), 0.75)

    def test_coefficients_use_squarefree_mobius_log_linear_window(self) -> None:
        coefficients = truncated_mobius_log_coefficients(limit=256, theta=0.5)
        cutoff = cutoff_from_theta(256, 0.5)
        self.assertEqual(cutoff, 16)
        self.assertAlmostEqual(coefficients[2], math.log(2.0) * 0.75)
        self.assertAlmostEqual(
            coefficients[6],
            -math.log(6.0) * (1.0 - math.log(6.0) / math.log(float(cutoff))),
        )
        self.assertNotIn(4, coefficients)
        self.assertNotIn(cutoff, coefficients)

    def test_contract_rejects_target_and_analytic_inputs(self) -> None:
        audit = audit_coefficient_contract(
            {"uses": ("X", "d", "mobius", "log", "fixed_linear_window")}
        )
        self.assertEqual(audit["classification"], "coefficient_input_not_rejected")
        rejected = audit_coefficient_contract({"uses": ("X", "psi(X)-X", "Mellin")})
        self.assertEqual(
            rejected["classification"],
            "coefficient_uses_target_or_forbidden_analytic_input",
        )
        self.assertEqual(rejected["forbidden_inputs"], ("Mellin", "psi(X)-X"))
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.MFACTruncatedMobiusLogCoercivityAuditTest.test_coefficients_use_squarefree_mobius_log_linear_window -v`

Expected: FAIL，原因是审计模块尚不存在。

### Task 2: 实现预注册系数族和防循环合同

**Files:**
- Create: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`

- [ ] **Step 1: 实现输入验证、平方自由 Möbius 和线性窗口**

```python
FORBIDDEN_COEFFICIENT_INPUTS = frozenset(
    {
        "psi(X)-X",
        "Chebyshev_error",
        "Mellin",
        "zeta_zero",
        "explicit_formula",
        "RH",
    }
)


def linear_window(position: object) -> float:
    """返回预注册线性窗口在 [0, 1] 上的值。"""
    if type(position) not in (int, float) or not 0.0 <= float(position) <= 1.0:
        raise ValueError("position 必须是位于 [0, 1] 的有限实数")
    return 1.0 - float(position)


def mobius_value(index: int) -> int:
    """以试除法返回 Möbius 函数值，供有限审计使用。"""
    remaining = index
    prime_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            prime_count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def truncated_mobius_log_coefficients(limit: int, theta: float) -> dict[int, float]:
    """构造固定线性截断的非零 Möbius--log 系数。"""
    cutoff = cutoff_from_theta(limit, theta)
    logarithmic_cutoff = log(float(cutoff))
    return {
        index: -mobius * log(float(index)) * linear_window(log(float(index)) / logarithmic_cutoff)
        for index in range(2, cutoff + 1)
        if (mobius := mobius_value(index)) != 0
        and linear_window(log(float(index)) / logarithmic_cutoff) != 0.0
    }
```

- [ ] **Step 2: 实现合同审计与严格参数校验**

```python
def audit_coefficient_contract(contract: Mapping[str, Any]) -> dict[str, object]:
    """拒绝系数定义读取目标误差或被禁止解析输入。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = contract.get("uses", ())
    if isinstance(uses, str) or not isinstance(uses, Iterable):
        raise ValueError("contract uses 必须为非裸字符串的可迭代字符串对象")
    checked_uses = tuple(uses)
    if any(type(item) is not str for item in checked_uses):
        raise ValueError("contract uses 的所有元素必须为字符串")
    forbidden_inputs = tuple(sorted(set(checked_uses).intersection(FORBIDDEN_COEFFICIENT_INPUTS)))
    return {
        "classification": (
            "coefficient_uses_target_or_forbidden_analytic_input"
            if forbidden_inputs
            else "coefficient_input_not_rejected"
        ),
        "forbidden_inputs": forbidden_inputs,
    }
```

- [ ] **Step 3: 运行 Task 1 全部测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test -v`

Expected: PASS。

### Task 3: 写出有限能量、归一化和一致性测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`

- [ ] **Step 1: 添加直接平方和、二次型和归一化比率的测试**

```python
from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    direct_centered_energy,
    normalized_energy_ratio,
    quadratic_centered_energy,
    weighted_mass,
)


    def test_direct_and_kernel_energies_agree_with_floating_residual(self) -> None:
        coefficients = truncated_mobius_log_coefficients(limit=64, theta=0.5)
        direct = direct_centered_energy(64, coefficients)
        quadratic = quadratic_centered_energy(64, coefficients)
        self.assertGreater(direct, 0.0)
        self.assertAlmostEqual(direct, quadratic, places=10)

    def test_weighted_mass_and_ratio_are_positive(self) -> None:
        coefficients = truncated_mobius_log_coefficients(limit=64, theta=0.5)
        mass = weighted_mass(64, coefficients)
        ratio = normalized_energy_ratio(64, coefficients)
        self.assertGreater(mass, 0.0)
        self.assertGreater(ratio, 0.0)
        self.assertTrue(math.isfinite(ratio))
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.MFACTruncatedMobiusLogCoercivityAuditTest.test_direct_and_kernel_energies_agree_with_floating_residual -v`

Expected: FAIL，原因是能量函数尚未定义。

### Task 4: 实现精确核驱动的有限能量诊断

**Files:**
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`

- [ ] **Step 1: 用既有精确有理核实现二次型与直接平方和**

```python
from experiments.prime_matrix_mfac_centered_divisibility_covariance_audit import (
    centered_covariance_entry,
)


def quadratic_centered_energy(limit: int, coefficients: Mapping[int, float]) -> float:
    """用精确中心化核条目计算实际浮点系数的有限二次型。"""
    checked = _checked_float_coefficients(limit, coefficients)
    return sum(
        left_value * right_value * float(centered_covariance_entry(limit, left, right))
        for left, left_value in checked.items()
        for right, right_value in checked.items()
    )


def direct_centered_energy(limit: int, coefficients: Mapping[int, float]) -> float:
    """直接计算中心化整除负载平方和，用于核恒等式数值核验。"""
    checked = _checked_float_coefficients(limit, coefficients)
    mean = sum(value * (limit // index) / limit for index, value in checked.items())
    return sum(
        (sum(value for index, value in checked.items() if number % index == 0) - mean) ** 2
        for number in range(1, limit + 1)
    )


def weighted_mass(limit: int, coefficients: Mapping[int, float]) -> float:
    """计算设计规格中的 X sum |a_d|^2/d 归一化质量。"""
    checked = _checked_float_coefficients(limit, coefficients)
    return limit * sum(value * value / index for index, value in checked.items())


def normalized_energy_ratio(limit: int, coefficients: Mapping[int, float]) -> float:
    """返回有限诊断比率，禁止解释为统一强制性常数。"""
    mass = weighted_mass(limit, coefficients)
    if mass <= 0.0:
        raise ValueError("weighted mass 必须严格为正")
    return quadratic_centered_energy(limit, coefficients) / mass
```

- [ ] **Step 2: 在 `audit_truncated_mobius_log_coercivity` 中报告残差与有限状态**

```python
def audit_truncated_mobius_log_coercivity(limit: int, theta: float) -> dict[str, Any]:
    """生成预注册系数族的有限诊断，不外推为全尺度命题。"""
    coefficients = truncated_mobius_log_coefficients(limit, theta)
    direct = direct_centered_energy(limit, coefficients)
    quadratic = quadratic_centered_energy(limit, coefficients)
    return {
        "certificate_type": "prime_matrix_mfac_truncated_mobius_log_coercivity_audit",
        "status": "numerical_only_finite_structured_coercivity_profile",
        "parameters": {"limit": limit, "theta": theta, "window": "linear"},
        "coefficient_contract": audit_coefficient_contract(
            {"uses": ("X", "d", "mobius", "log", "fixed_linear_window")}
        ),
        "coefficient_support": tuple(sorted(coefficients)),
        "direct_energy": direct,
        "quadratic_energy": quadratic,
        "identity_floating_point_residual": abs(direct - quadratic),
        "weighted_mass": weighted_mass(limit, coefficients),
        "normalized_energy_ratio": normalized_energy_ratio(limit, coefficients),
        "structured_coercivity_status": "unproved",
        "chebyshev_bridge_status": "not_started",
        "mellin_status": "not_started",
        "rh_proved": False,
    }
```

- [ ] **Step 3: 运行 Task 3 全部测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test -v`

Expected: PASS。

### Task 5: 写出有限证书与 CLI 的红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`

- [ ] **Step 1: 添加证书边界和文件写入测试**

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    audit_truncated_mobius_log_coercivity,
    write_certificate,
)


    def test_certificate_stays_numerical_only_and_never_claims_rh(self) -> None:
        payload = audit_truncated_mobius_log_coercivity(limit=128, theta=0.25)
        self.assertEqual(payload["status"], "numerical_only_finite_structured_coercivity_profile")
        self.assertEqual(payload["structured_coercivity_status"], "unproved")
        self.assertFalse(payload["rh_proved"])
        self.assertLess(payload["identity_floating_point_residual"], 1e-9)

    def test_write_certificate_preserves_contract_and_boundary(self) -> None:
        with TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            write_certificate(audit_truncated_mobius_log_coercivity(128, 0.25), json_path, markdown_path)
            stored = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertFalse(stored["rh_proved"])
            self.assertIn("不构成 RH 证明", markdown_path.read_text(encoding="utf-8"))
```

- [ ] **Step 2: 运行证书测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.MFACTruncatedMobiusLogCoercivityAuditTest.test_write_certificate_preserves_contract_and_boundary -v`

Expected: FAIL，原因是 `write_certificate` 尚未定义。

### Task 6: 实现默认产物、CLI 和最终验证

**Files:**
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.md`

- [ ] **Step 1: 实现 JSON/Markdown 写入和预注册 CLI**

```python
def write_certificate(certificate: Mapping[str, Any], json_path: Path, markdown_path: Path) -> None:
    """写出有限诊断证书并保留不升级边界。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    markdown_path.write_text(
        "# MFAC 截断 Möbius--log 系数族有限强制性审计\n\n"
        f"- 参数：`X={certificate['parameters']['limit']}`，`theta={certificate['parameters']['theta']}`，窗口：`linear`\n"
        f"- 有限归一化能量比：`{certificate['normalized_energy_ratio']}`\n"
        f"- 直接平方和与核二次型残差：`{certificate['identity_floating_point_residual']}`\n\n"
        "```text\nstructured_coercivity_status=unproved\nchebyshev_bridge_status=not_started\nmellin_status=not_started\nrh_proved=false\n```\n\n"
        "此证书仅记录固定有限尺度的浮点诊断；它不构成统一强制性、Chebyshev 能量桥、Mellin 收缩或 RH 证明。\n",
        encoding="utf-8",
    )


def main() -> None:
    """生成默认有限证书；仅允许预注册线性窗口。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 截断 Möbius--log 系数族有限审计证书")
    parser.add_argument("--limit", type=int, default=4096)
    parser.add_argument("--theta", type=float, default=0.25)
    parser.add_argument("--window", choices=("linear",), default="linear")
    parser.add_argument("--json-out", type=Path, default=Path("docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.json"))
    parser.add_argument("--markdown-out", type=Path, default=Path("docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.md"))
    args = parser.parse_args()
    write_certificate(audit_truncated_mobius_log_coercivity(args.limit, args.theta), args.json_out, args.markdown_out)
```

- [ ] **Step 2: 运行模块生成默认证书**

Run: `python3 experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py --limit 4096 --theta 0.25 --window linear`

Expected: 创建两个 `docs/monograph/prime-matrix-mfac-truncated-mobius-log-coercivity-audit.*` 文件；内容含 `status=numerical_only` 和 `rh_proved=false`。

- [ ] **Step 3: 运行特定、相邻与全量 MFAC 测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py -v && python3 -m unittest experiments.prime_matrix_mfac_centered_divisibility_covariance_audit_test.py experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test.py -v && python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v && git diff --check`

Expected: 全部 PASS，且无空白错误。若既有无关测试失败，仅记录其名称和错误，不修改无关模块。

- [ ] **Step 4: 检查变更范围，不提交**

Run: `git status --short && git diff --check`

Expected: 仅包含本计划列出的新审计器、测试与证书，以及用户已存在的 `AGENTS.md` 修改；不执行 `git add` 或 `git commit`。
