# MFAC 中心化整除协方差谱剖面 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建实际整数中心化整除协方差的精确有限谱审计器，输出加权最小强制比、近退化向量和 dyadic 尺度诊断，同时严格禁止将有限读数升级为统一强制性、Mellin 收缩或 RH 证明。

**Architecture:** 一个标准库 Python 模块以 `Fraction` 构造 `C_X(d,e)` 和方差恒等式；仅在广义特征值近似阶段转换为浮点，并输出残差。审计入口固定有限 `X` 和 `D=floor(X^theta)`，生成 JSON/Markdown 证书；测试锁定代数恒等式、权重归一化、近零模式、CLI 写出和状态边界。

**Tech Stack:** Python 3 标准库（`argparse`、`dataclasses`、`fractions`、`json`、`math`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py`
  - 精确整除协方差核、方差二次型、加权 Jacobi 特征求解、有限尺度/双倍尺度审计与证书 CLI。
- Create: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py`
  - 锁定精确恒等式、广义最小特征值、有限状态和 CLI 边界。
- Create: `docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.json`
  - 默认有限尺度谱剖面机器证书。
- Create: `docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.md`
  - 默认人读证书，明确有限读数边界。
- Modify: `docs/monograph/external-theorem-index.md`
  - 只追加审计索引、有限范围结果和三项未闭合门。

### Task 1: 锁定中心化整除协方差的精确方差恒等式

**Files:**
- Create: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py`
- Create: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py`

- [x] **Step 1: 写出失败的核条目与方差恒等式测试**

```python
from fractions import Fraction

def test_centered_covariance_entries_match_small_exact_values(self) -> None:
    self.assertEqual(centered_covariance_entry(12, 2, 2), Fraction(3, 1))
    self.assertEqual(centered_covariance_entry(12, 2, 3), Fraction(0, 1))
    self.assertEqual(centered_covariance_entry(12, 3, 3), Fraction(8, 3))

def test_quadratic_form_equals_centered_divisibility_variance(self) -> None:
    coefficients = {2: Fraction(2, 1), 3: Fraction(-3, 1)}
    self.assertEqual(
        covariance_quadratic_form(12, coefficients),
        centered_divisibility_variance(12, coefficients),
    )
```

- [x] **Step 2: 运行测试，确认红灯**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py -v`

Expected: FAIL，提示 `centered_covariance_entry` 或 `covariance_quadratic_form` 未定义。

- [x] **Step 3: 最小实现精确核和方差和**

```python
def centered_covariance_entry(limit: int, left: int, right: int) -> Fraction:
    left_count = limit // left
    right_count = limit // right
    overlap = limit // (left * right // gcd(left, right))
    return Fraction(overlap, 1) - Fraction(left_count * right_count, limit)

def centered_divisibility_variance(
    limit: int, coefficients: Mapping[int, Fraction]
) -> Fraction:
    mean = Fraction(sum(value * (limit // index) for index, value in coefficients.items()), limit)
    return sum(
        (sum(value for index, value in coefficients.items() if number % index == 0) - mean) ** 2
        for number in range(1, limit + 1)
    )
```

实现同样只接受至少为 `2` 的内建整数索引和有限非空系数字典；输出保留 `Fraction`，不得提前浮点化。

- [x] **Step 4: 运行任务测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py -v`

Expected: 两个精确测试 PASS。

### Task 2: 锁定加权最小强制比与数值残差合同

**Files:**
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py`
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py`

- [x] **Step 1: 写出失败的广义特征值测试**

```python
def test_weighted_minimum_coercivity_ratio_matches_diagonal_small_case(self) -> None:
    result = weighted_coercivity_profile(limit=12, cutoff=3)
    self.assertAlmostEqual(result["minimum_ratio_estimate"], 0.5)
    self.assertLess(result["maximum_eigen_residual"], 1e-10)
    self.assertEqual(result["status"], "finite_profile_only")
```

- [x] **Step 2: 运行定向测试，确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_centered_divisibility_covariance_audit_test.MFACCenteredDivisibilityCovarianceAuditTest.test_weighted_minimum_coercivity_ratio_matches_diagonal_small_case -v`

Expected: FAIL，提示 `weighted_coercivity_profile` 未定义。

- [x] **Step 3: 最小实现权重归一化与 Jacobi 特征值估计**

对索引 `d=2,...,D` 构造对称实矩阵

```python
normalized[row][column] = (
    math.sqrt(indices[row] * indices[column])
    * float(covariance[row][column])
    / limit
)
```

它的最小特征值即
`Q_X(a) / (X * sum(a_d**2 / d))` 的有限维数值读数。实现 `symmetric_jacobi_eigendecomposition`，返回升序特征值、归一化向量和

```python
max(abs(sum(matrix[row][column] * vector[column] for column in range(size))
        - eigenvalue * vector[row]) for row in range(size))
```

作为残差。若迭代次数达到 `128 * size * size` 仍有非对角元绝对值大于 `1e-12`，抛出 `RuntimeError`，不得静默输出不可靠特征值。

- [x] **Step 4: 运行任务测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py -v`

Expected: 精确方差和加权最小比测试均 PASS，证书状态仍为 `finite_profile_only`。

### Task 3: 锁定尺度剖面、近退化向量和 dyadic 诊断

**Files:**
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py`
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py`

- [x] **Step 1: 写出失败的有限尺度诊断测试**

```python
def test_dyadic_comparison_never_upgrades_finite_profiles_to_uniform_theorem(self) -> None:
    result = compare_dyadic_profiles(limit=64, theta=0.5)
    self.assertEqual(result["status"], "finite_dyadic_diagnostic_only")
    self.assertFalse(result["uniform_weighted_coercivity_proved"])
    self.assertFalse(result["actual_mellin_contraction_present"])
    self.assertFalse(result["rh_proved"])
    self.assertGreater(result["current"]["cutoff"], 1)
    self.assertGreater(result["next"]["cutoff"], 1)
```

- [x] **Step 2: 运行定向测试，确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_centered_divisibility_covariance_audit_test.MFACCenteredDivisibilityCovarianceAuditTest.test_dyadic_comparison_never_upgrades_finite_profiles_to_uniform_theorem -v`

Expected: FAIL，提示 `compare_dyadic_profiles` 未定义。

- [x] **Step 3: 最小实现 cutoff、剖面和比较器**

```python
def cutoff_from_theta(limit: int, theta: float) -> int:
    if not 0.0 < theta < 1.0:
        raise ValueError("theta 必须严格位于 0 与 1 之间")
    return max(2, min(limit, math.floor(limit ** theta)))

def compare_dyadic_profiles(limit: int, theta: float) -> dict[str, Any]:
    current = weighted_coercivity_profile(limit, cutoff_from_theta(limit, theta))
    following = weighted_coercivity_profile(2 * limit, cutoff_from_theta(2 * limit, theta))
    return {
        "status": "finite_dyadic_diagnostic_only",
        "current": current,
        "next": following,
        "minimum_ratio_change": following["minimum_ratio_estimate"] - current["minimum_ratio_estimate"],
        "uniform_weighted_coercivity_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
    }
```

从最小特征向量中输出绝对值最大的三个 `(index, coefficient)`，仅将其称为 `near_degenerate_support`，而非解析反例。

- [x] **Step 4: 运行任务测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py -v`

Expected: 剖面、dyadic 和非升级状态测试均 PASS。

### Task 4: 写出默认有限证书与解析义务边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py`
- Modify: `experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [x] **Step 1: 写出失败的端到端证书测试**

```python
def test_certificate_records_finite_profile_without_rh_claim(self) -> None:
    certificate = audit_centered_divisibility_covariance(limit=256, theta=0.25)
    with tempfile.TemporaryDirectory() as directory:
        json_path = Path(directory) / "certificate.json"
        markdown_path = Path(directory) / "certificate.md"
        write_certificate(certificate, json_path, markdown_path)
        payload = json.loads(json_path.read_text(encoding="utf-8"))
    self.assertEqual(payload["status"], "finite_covariance_profile_not_uniform_theorem")
    self.assertFalse(payload["uniform_weighted_coercivity_proved"])
    self.assertFalse(payload["actual_mellin_contraction_present"])
    self.assertFalse(payload["rh_proved"])
```

- [x] **Step 2: 运行端到端测试，确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_centered_divisibility_covariance_audit_test.MFACCenteredDivisibilityCovarianceAuditTest.test_certificate_records_finite_profile_without_rh_claim -v`

Expected: FAIL，提示审计入口或证书写出函数未定义。

- [x] **Step 3: 最小实现审计入口、CLI 和文档**

```python
def audit_centered_divisibility_covariance(limit: int, theta: float) -> dict[str, Any]:
    profile = weighted_coercivity_profile(limit, cutoff_from_theta(limit, theta))
    return {
        "certificate_type": "prime_matrix_mfac_centered_divisibility_covariance_audit",
        "status": "finite_covariance_profile_not_uniform_theorem",
        "parameters": {"limit": limit, "theta": theta},
        "profile": profile,
        "dyadic_diagnostic": compare_dyadic_profiles(limit, theta),
        "uniform_weighted_coercivity_proved": False,
        "actual_chebyshev_energy_bridge_proved": False,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "UniformCenteredDivisibilityCoercivityAndNoncircularChebyshevEnergyBridge",
    }
```

CLI 必须支持 `--limit`、`--theta`、`--json-out`、`--markdown-out`。Markdown 必须分别列出精确方差恒等式、有限谱读数、近退化支持、三项解析义务，并包含“不构成 RH 证明”。索引只能新增有限审计记录。

- [x] **Step 4: 运行测试、生成默认证书并检查范围**

Run: `python3 -m unittest experiments/prime_matrix_mfac_centered_divisibility_covariance_audit_test.py -v && python3 experiments/prime_matrix_mfac_centered_divisibility_covariance_audit.py && git diff --check`

Expected: 全部新测试 PASS；默认证书保持 `uniform_weighted_coercivity_proved=false`、`actual_mellin_contraction_present=false` 与 `rh_proved=false`。

### Task 5: 全量回归和人工结论审查

**Files:**
- Modify: 本计划涉及的全部文件

- [x] **Step 1: 运行 MFAC 全族回归**

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`

Expected: 全部测试 PASS。

- [x] **Step 2: 检查禁止升级状态**

Run: `rg -n "uniform_weighted_coercivity_proved=true|actual_mellin_contraction_present=true|rh_proved=true" docs/monograph/prime-matrix-mfac-centered-divisibility-covariance-audit.* docs/monograph/external-theorem-index.md`

Expected: 无匹配。

- [ ] **Step 3: 检查暂存范围，等待用户决定是否提交**

Run: `git diff --check && git status --short`

Expected: 无空白错误；不暂存用户单独维护的 `AGENTS.md`；未获得明确提交请求前不得执行 `git commit`。
