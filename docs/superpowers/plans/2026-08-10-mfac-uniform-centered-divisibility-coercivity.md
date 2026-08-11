# MFAC 中心化整除协方差统一强制性双轨审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 以精确有限尺度误差界和显式平方自由见证，审计并证伪中心化整除极限核的“维度无关常数谱隙”命题。

**Architecture:** 新模块独立于既有有限协方差谱审计，复用其精确中心化核。模块首先实现 `K_X`、`K_infinity` 及取整误差的显式上界；随后由整除关联矩阵的 Möbius 逆构造平方自由见证，并输出 Rayleigh 比证书。默认产物明确区分“UDC 已被此见证族否定”与仍未建立的 Chebyshev/Mellin/RH 链条。

**Tech Stack:** Python 3 标准库（`fractions`、`math`、`json`、`argparse`、`unittest`），现有 `experiments` 审计模式。

**Traceability:** 本计划落实已批准闭环规格 `docs/superpowers/specs/2026-08-11-mfac-rh-closure-attack-surface-design.md` 中的 W0（反例与归一化筛选）；它不实现 W1、W2 或 W3。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py`
  - 规范化核、极限核、误差界、平方自由 Möbius 见证、证书 CLI。
- Create: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py`
  - 精确恒等式、误差上界、见证消元、Rayleigh 比、禁止升级与文件证书测试。
- Create: `docs/monograph/prime-matrix-mfac-uniform-centered-divisibility-coercivity-audit.json`
  - 默认机器可读证书。
- Create: `docs/monograph/prime-matrix-mfac-uniform-centered-divisibility-coercivity-audit.md`
  - 人读审计结论、显式见证公式和范围边界。
- Modify: `docs/monograph/external-theorem-index.md`
  - 增加 UDC 特定命题被显式见证否定的记录；不改写既有 RH 主线。

### Task 1: 写出规范化核与误差上界的红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py`

- [ ] **Step 1: 写出极限核和有限误差测试**

```python
from fractions import Fraction
import unittest

from experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit import (
    finite_normalized_kernel_entry,
    finite_to_limit_entry_error_bound,
    limit_normalized_kernel_entry,
    finite_to_limit_operator_error_bound,
)


class MFACUniformCenteredDivisibilityCoercivityAuditTest(unittest.TestCase):
    def test_limit_kernel_matches_gcd_formula(self) -> None:
        self.assertAlmostEqual(limit_normalized_kernel_entry(2, 6), 1 / (12**0.5))
        self.assertAlmostEqual(limit_normalized_kernel_entry(5, 5), 4 / 5)

    def test_finite_to_limit_error_respects_entrywise_bound(self) -> None:
        limit, left, right = 60, 4, 6
        error = abs(
            finite_normalized_kernel_entry(limit, left, right)
            - limit_normalized_kernel_entry(left, right)
        )
        self.assertLessEqual(error, finite_to_limit_entry_error_bound(limit, left, right))

    def test_operator_error_bound_has_explicit_subcritical_scale(self) -> None:
        self.assertEqual(
            finite_to_limit_operator_error_bound(limit=100, cutoff=10),
            Fraction(9, 4),
        )
```

- [ ] **Step 2: 运行测试，确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_limit_kernel_matches_gcd_formula -v`

Expected: FAIL，提示模块或函数尚未定义。

- [ ] **Step 3: 实现精确对象与统一误差界**

在新模块中实现以下接口：

```python
def limit_normalized_kernel_entry(left: int, right: int) -> float:
    return (gcd(left, right) - 1) / sqrt(left * right)


def finite_normalized_kernel_entry(limit: int, left: int, right: int) -> float:
    covariance = centered_covariance_entry(limit, left, right)
    return sqrt(left * right) * float(covariance) / limit


def finite_to_limit_entry_error_bound(limit: int, left: int, right: int) -> float:
    return sqrt(left * right) * (1 + 1 / left + 1 / right + 1 / limit) / limit


def finite_to_limit_operator_error_bound(limit: int, cutoff: int) -> Fraction:
    return Fraction(5 * cutoff * (cutoff - 1), 2 * limit)
```

`finite_to_limit_operator_error_bound` 使用逐行绝对和界：对 `2 <= d,e <= D`，逐项误差不超过
`5D/(2X)`，共有 `D-1` 个列项。实现必须验证 `limit`、`cutoff`、索引为内建整数，并复用
`centered_covariance_entry`，不得复制其取整核逻辑。

- [ ] **Step 4: 运行 Task 1 测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_finite_to_limit_error_respects_entrywise_bound experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_operator_error_bound_has_explicit_subcritical_scale -v`

Expected: PASS。

- [ ] **Step 5: 检查本任务改动范围**

Run: `git diff --check && git diff -- experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py`

Expected: 无空白错误；只出现 Task 1 的新模块和测试内容。

### Task 2: 构造平方自由 Möbius 反例见证

**Files:**
- Modify: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py`

- [ ] **Step 1: 写出见证消元与 Rayleigh 比的红灯测试**

```python
def test_squarefree_witness_isolates_its_terminal_divisor_layer(self) -> None:
    witness = squarefree_divisor_witness(6)
    self.assertAlmostEqual(divisibility_transform(witness, 2), 0.0)
    self.assertAlmostEqual(divisibility_transform(witness, 3), 0.0)
    self.assertAlmostEqual(divisibility_transform(witness, 6), 1.0)

def test_squarefree_witness_has_exact_rayleigh_ratio(self) -> None:
    certificate = squarefree_witness_certificate(6)
    self.assertEqual(certificate["rayleigh_ratio_exact"], "2/11")
    self.assertAlmostEqual(certificate["rayleigh_ratio"], 2 / 11)

def test_primorial_witness_ratios_decay_on_first_three_levels(self) -> None:
    ratios = [item["rayleigh_ratio"] for item in primorial_witness_certificates(3)]
    self.assertGreater(ratios[0], ratios[1])
    self.assertGreater(ratios[1], ratios[2])
```

- [ ] **Step 2: 运行测试，确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_squarefree_witness_has_exact_rayleigh_ratio -v`

Expected: FAIL，提示平方自由见证接口未定义。

- [ ] **Step 3: 实现 Möbius 逆见证与精确证书**

实现仅接受平方自由 `terminal` 的接口。对每个 `d | terminal`、`d >= 2`，定义

```python
coefficient[d] = sqrt(d) * mobius(terminal // d)
```

并实现：

```python
def divisibility_transform(coefficients: Mapping[int, float], divisor: int) -> float:
    return sum(value / sqrt(index) for index, value in coefficients.items() if index % divisor == 0)


def squarefree_witness_certificate(terminal: int) -> dict[str, object]:
    # 对平方自由 terminal=m，Q_infinity=phi(m)，||x||^2=sigma(m)-1。
    # 返回精确分数及其浮点读数，作为 UDC 的显式反例证书。
```

`primorial_witness_certificates(count)` 必须返回以 `6, 30, 210, ...` 为终端的前 `count` 个
可用见证，且每个终端都保持在相应有限主子式索引范围内。使用标准库自行筛素数、分解、
平方自由验证、`phi`、`sigma` 与 Möbius 值；不引入第三方依赖。

代码及 docstring 需用中文说明以下精确结论：对于 `q >= 2`，整除变换仅在 `q=terminal`
时为 `1`；故极限二次型为 `phi(terminal)`，Rayleigh 比严格为
`phi(terminal) / (sigma(terminal) - 1)`。

- [ ] **Step 4: 运行 Task 2 测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_squarefree_witness_isolates_its_terminal_divisor_layer experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_primorial_witness_ratios_decay_on_first_three_levels -v`

Expected: PASS；`6,30,210` 的精确 Rayleigh 比依次为 `2/11`、`8/71`、`48/575`。

- [ ] **Step 5: 写出命题状态的回归测试**

```python
def test_audit_marks_only_udc_as_refuted(self) -> None:
    certificate = audit_uniform_centered_divisibility_coercivity(limit=4096, theta=0.75)
    self.assertTrue(certificate["udc_refuted_by_explicit_witnesses"])
    self.assertFalse(certificate["actual_chebyshev_energy_bridge_proved"])
    self.assertFalse(certificate["actual_mellin_contraction_present"])
    self.assertFalse(certificate["rh_proved"])
```

Expected: FAIL，提示审计入口未定义。

### Task 3: 生成双轨审计证书与文档边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-uniform-centered-divisibility-coercivity-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-uniform-centered-divisibility-coercivity-audit.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 实现审计入口、CLI 和证书写出函数**

```python
def audit_uniform_centered_divisibility_coercivity(limit: int, theta: float) -> dict[str, object]:
    cutoff = cutoff_from_theta(limit, theta)
    witnesses = [
        item for item in primorial_witness_certificates(8)
        if item["terminal"] <= cutoff
    ]
    return {
        "certificate_type": "prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit",
        "status": "explicit_squarefree_witnesses_refute_constant_udc",
        "parameters": {"limit": limit, "theta": theta, "cutoff": cutoff},
        "finite_to_limit_operator_error_bound": str(
            finite_to_limit_operator_error_bound(limit, cutoff)
        ),
        "squarefree_witnesses": witnesses,
        "udc_refuted_by_explicit_witnesses": True,
        "uniform_centered_divisibility_coercivity_proved": False,
        "actual_chebyshev_energy_bridge_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "QuantifiedScaleDependentCoercivityOrAlternativeEnergyBeforeChebyshevBridge",
    }
```

CLI 参数为 `--limit`、`--theta`、`--json-out`、`--markdown-out`。默认值使用
`limit=4096`、`theta=0.75`，以确保默认 cutoff 至少容纳 `terminal=210`；证书不得运行
全矩阵特征分解，也不得把 `E(X,D)` 小于一误写成谱隙结论。

- [ ] **Step 2: 写出端到端证书红灯测试并验证**

```python
def test_write_certificate_records_udc_refutation_without_rh_claim(self) -> None:
    certificate = audit_uniform_centered_divisibility_coercivity(limit=4096, theta=0.75)
    with tempfile.TemporaryDirectory() as directory:
        json_path = Path(directory) / "certificate.json"
        markdown_path = Path(directory) / "certificate.md"
        write_certificate(certificate, json_path, markdown_path)
        payload = json.loads(json_path.read_text(encoding="utf-8"))
    self.assertEqual(payload["status"], "explicit_squarefree_witnesses_refute_constant_udc")
    self.assertTrue(payload["udc_refuted_by_explicit_witnesses"])
    self.assertFalse(payload["rh_proved"])
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.MFACUniformCenteredDivisibilityCoercivityAuditTest.test_write_certificate_records_udc_refutation_without_rh_claim -v`

Expected: FAIL，直至 `write_certificate` 实现完成；完成后 PASS。

- [ ] **Step 3: 写入默认文档与外部定理索引**

Markdown 必须写出：

```text
UDC_constant_spectral_gap_refuted_by_explicit_squarefree_witnesses=true
uniform_centered_divisibility_coercivity_proved=false
actual_chebyshev_energy_bridge_proved=false
actual_mellin_contraction_present=false
rh_proved=false
```

文档须给出见证公式、`phi(m)/(sigma(m)-1)`、其在 primorial 序列上趋零的理由，以及下列
严格范围：这仅否定已定义的 `K_infinity` 常数谱隙 UDC，不否定所有尺度依赖强制性、其他
能量或 RH。索引记录只能新增本命题的负面结论和新的正向门槛。

- [ ] **Step 4: 运行 Task 3 测试和生成默认证书**

Run: `python3 -m unittest experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py -v && python3 experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit.py && git diff --check`

Expected: 全部新测试 PASS；默认 JSON/Markdown 存在；禁止升级字段保持 false。

- [ ] **Step 5: 检查结论范围**

Run: `rg -n "uniform_centered_divisibility_coercivity_proved=true|actual_chebyshev_energy_bridge_proved=true|actual_mellin_contraction_present=true|rh_proved=true" docs/monograph/prime-matrix-mfac-uniform-centered-divisibility-coercivity-audit.* docs/monograph/external-theorem-index.md`

Expected: 无匹配。

### Task 4: 全量 MFAC 回归与人工审查

**Files:**
- Modify: 本计划涉及的全部文件

- [ ] **Step 1: 运行新旧中心化协方差审计回归**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py experiments/prime_matrix_mfac_uniform_centered_divisibility_coercivity_audit_test.py -v`

Expected: PASS；既有有限谱审计的状态语义不改变。

- [ ] **Step 2: 运行 MFAC 审计族回归**

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`

Expected: PASS；如出现既存无关失败，仅记录并停止扩展修复范围。

- [ ] **Step 3: 审查工作区和用户维护文件**

Run: `git diff --check && git status --short`

Expected: 无空白错误；不得覆盖、暂存或提交用户单独维护的 `AGENTS.md`；未收到明确提交请求前不得执行 `git commit`。
