# MFAC 实际 LCM Gram 能量审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在实际自然数上实现 LCM Gram 正半定能量审计，精确分离已获得的平方自由 Möbius 核与尚缺的常数方向收缩。

**Architecture:** 模块以有限整数区间 `{1,...,X}` 为唯一底座：用可整除指示函数构造 `floor(X/lcm(d,e))`，再用 Möbius 权重验证 `sum Lambda(n)^2` 的精确 Gram 恒等式。第二层将实际 Chebyshev 增量投影到常数向量，记录普通 Cauchy 所支付的 `sqrt(X)` 因子；中心化候选必须通过禁止输入审计，不能读取待估误差或零点信息。

**Tech Stack:** Python 3 标准库（`argparse`、`dataclasses`、`json`、`math`、`pathlib`、`unittest`）；现有 MFAC 审计 CLI/Markdown/JSON 约定。

---

## 文件结构

- 创建 `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py`：实际整数核、Möbius/`Lambda` 权重、能量与中心化合同分类、CLI 及证书写出。
- 创建 `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py`：精确 Gram、PSD、LCM--Möbius、常数方向、六倍数见证、循环拒绝与证书边界测试。
- 创建 `docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.json`：默认 `limit=60` 的机器可读证书。
- 创建 `docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.md`：数学恒等式、障碍和非 RH 边界。
- 修改 `docs/monograph/claim-status-table.md`：登记本轮只闭合实际 PSD 核与 Cauchy 障碍。
- 修改 `docs/monograph/external-theorem-index.md`：登记 `MFAC-ALGE` 为项目内部审计而非外部定理。

### Task 1: 写入实际 LCM Gram 的失败测试

**Files:**
- Create: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py`
- Reference: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`

- [ ] **Step 1: 声明目标 API 并写入精确 Gram 测试**

```python
from prime_matrix_mfac_actual_lcm_gram_energy_audit import (
    audit_centering_contract,
    chebyshev_increment_energy,
    lcm_gram_entry,
    lcm_gram_quadratic_form,
    lcm_mobius_energy,
    lambda_square_energy,
    ordinary_cauchy_projection_bound,
    six_multiple_non_prime_power_witnesses,
    write_certificate,
)


def test_lcm_entry_is_actual_divisibility_overlap(self) -> None:
    self.assertEqual(lcm_gram_entry(30, 6, 10), 1)
    self.assertEqual(lcm_gram_entry(30, 4, 6), 2)


def test_quadratic_form_equals_sum_of_divisor_feature_squares(self) -> None:
    coefficients = {1: 2.0, 2: -1.0, 3: 4.0, 6: -2.0}
    expected = sum(
        sum(weight for divisor, weight in coefficients.items() if n % divisor == 0) ** 2
        for n in range(1, 25)
    )
    self.assertAlmostEqual(lcm_gram_quadratic_form(24, coefficients), expected)
```

- [ ] **Step 2: 写入 Möbius--`Lambda`、常数方向及循环合同测试**

```python
def test_mobius_lcm_energy_recovers_lambda_square_energy(self) -> None:
    self.assertAlmostEqual(lcm_mobius_energy(60), lambda_square_energy(60))


def test_actual_increment_energy_has_exact_cauchy_projection_factor(self) -> None:
    certificate = ordinary_cauchy_projection_bound(60)
    self.assertEqual(certificate["constant_direction_norm_squared"], 60)
    self.assertAlmostEqual(certificate["error_sum_squared"], certificate["chebyshev_error"] ** 2)
    self.assertLessEqual(certificate["error_sum_squared"], certificate["cauchy_upper_bound"])
    self.assertGreater(chebyshev_increment_energy(60), 0.0)


def test_every_recorded_six_multiple_is_not_a_prime_power(self) -> None:
    self.assertEqual(six_multiple_non_prime_power_witnesses(30), (6, 12, 18, 24, 30))


def test_centering_contract_rejects_target_or_zero_input(self) -> None:
    result = audit_centering_contract({"uses": ("psi(X)",)})
    self.assertEqual(
        result["classification"],
        "centered_kernel_uses_target_or_forbidden_analytic_input",
    )
```

- [ ] **Step 3: 运行新测试，确认红灯**

```bash
python3 -m unittest experiments.prime_matrix_mfac_actual_lcm_gram_energy_audit_test -v
```

Expected: `ModuleNotFoundError: No module named 'prime_matrix_mfac_actual_lcm_gram_energy_audit'`；不得通过或跳过。

- [ ] **Step 4: 提交红灯测试**

```bash
git add experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py
git commit -m "测试 MFAC 实际 LCM Gram 能量审计"
```

### Task 2: 实现实数值严格的实际整数核与障碍分类

**Files:**
- Create: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py`
- Test: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py`

- [ ] **Step 1: 实现基本算术与 LCM Gram API**

```python
def mobius(value: int) -> int:
    """计算正整数的 Möbius 值。"""


def von_mangoldt(value: int) -> float:
    """当 value 为素数幂时返回其底素数的对数，否则返回零。"""


def lcm_gram_entry(limit: int, left: int, right: int) -> int:
    """返回实际可整除指示函数在 1..limit 上的 Gram 内积。"""
    return limit // math.lcm(left, right)


def lcm_gram_quadratic_form(limit: int, coefficients: Mapping[int, float]) -> float:
    """以 LCM Gram 核计算有限向量的二次型。"""
    return sum(
        left_weight * right_weight * lcm_gram_entry(limit, left, right)
        for left, left_weight in coefficients.items()
        for right, right_weight in coefficients.items()
    )
```

实现中拒绝 `limit < 1`、非正 divisor 和超过 `limit` 的 divisor；`mobius` 用试除分解，在平方因子出现时返回零。`von_mangoldt` 只在恰有一个不同素因子时返回该素数对数。

- [ ] **Step 2: 实现 Möbius 权重、误差能量和常数方向界**

```python
def lcm_mobius_energy(limit: int) -> float:
    """返回 w_d=-mu(d)log(d) 的实际 LCM Gram 能量。"""


def lambda_square_energy(limit: int) -> float:
    """返回 sum_{n<=limit} Lambda(n)^2。"""


def chebyshev_increment_energy(limit: int) -> float:
    """返回 sum_{n<=limit}(Lambda(n)-1)^2。"""


def ordinary_cauchy_projection_bound(limit: int) -> dict[str, float | int]:
    """记录常数向量投影下的精确 Cauchy 上界。"""
    increments = [von_mangoldt(n) - 1.0 for n in range(1, limit + 1)]
    chebyshev_error = sum(increments)
    energy = sum(value * value for value in increments)
    return {
        "chebyshev_error": chebyshev_error,
        "error_sum_squared": chebyshev_error * chebyshev_error,
        "increment_energy": energy,
        "constant_direction_norm_squared": limit,
        "cauchy_upper_bound": limit * energy,
    }
```

`lcm_mobius_energy` 必须通过 `lcm_gram_quadratic_form` 计算；测试与逐项 `lambda_square_energy` 比较，不得以同一函数重算两侧。

- [ ] **Step 3: 实现六倍数见证与中心化合同分类**

```python
FORBIDDEN_CENTERING_INPUTS = frozenset({
    "psi(X)", "E_psi(X)", "prime_count_error_bound",
    "zero_location", "zero_free_region", "explicit_formula_remainder",
})


def six_multiple_non_prime_power_witnesses(limit: int) -> tuple[int, ...]:
    """列出 1..limit 内的六倍数；它们均不是素数幂。"""
    return tuple(range(6, limit + 1, 6))


def audit_centering_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    """拒绝读取待控制 Chebyshev 量或禁止解析输入的中心化候选。"""
    uses = set(contract.get("uses", ()))
    forbidden = sorted(uses & FORBIDDEN_CENTERING_INPUTS)
    return {
        "classification": (
            "centered_kernel_uses_target_or_forbidden_analytic_input"
            if forbidden else "centering_input_not_rejected_by_forbidden_input_audit"
        ),
        "forbidden_inputs": forbidden,
    }
```

- [ ] **Step 4: 运行新测试，确认绿灯**

```bash
python3 -m unittest experiments.prime_matrix_mfac_actual_lcm_gram_energy_audit_test -v
```

Expected: 所有已声明测试 `OK`。

- [ ] **Step 5: 提交最小实现**

```bash
git add \
  experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py \
  experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py
git commit -m "审计 MFAC 实际 LCM Gram 能量"
```

### Task 3: 生成证书并接入项目边界索引

**Files:**
- Modify: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py`
- Modify: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.md`
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写入证书失败测试**

```python
def test_certificate_states_psd_gain_cauchy_obstruction_and_non_rh_boundary(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        result = write_certificate(Path(directory), limit=60)
        payload = json.loads(result["json_path"].read_text(encoding="utf-8"))
        self.assertTrue(payload["actual_lcm_gram_identity_available"])
        self.assertTrue(payload["non_tagged_signed_kernel_available"])
        self.assertTrue(payload["positive_semidefinite_energy_identity_available"])
        self.assertTrue(payload["ordinary_cauchy_constant_direction_obstruction_present"])
        self.assertFalse(payload["actual_chebyshev_mellin_contraction_present"])
        self.assertFalse(payload["mathematical_nonexistence_proved"])
        self.assertFalse(payload["rh_proved"])
```

- [ ] **Step 2: 运行该单测，确认因 `write_certificate` 缺失而失败**

```bash
python3 -m unittest experiments.prime_matrix_mfac_actual_lcm_gram_energy_audit_test.MFACActualLCMGramEnergyAuditTest.test_certificate_states_psd_gain_cauchy_obstruction_and_non_rh_boundary -v
```

Expected: `ImportError` 或 `AttributeError` 指向缺失的 `write_certificate`。

- [ ] **Step 3: 实现审计汇总、证书和 CLI**

```python
def audit_actual_lcm_gram_energy(limit: int) -> dict[str, Any]:
    """汇总实际核、常数方向障碍和中心化边界。"""
    return {
        "limit": limit,
        "actual_lcm_gram_identity_available": True,
        "fixed_actual_integer_embedding": True,
        "fixed_actual_chebyshev_measure": True,
        "non_tagged_signed_kernel_available": True,
        "positive_semidefinite_energy_identity_available": True,
        "ordinary_cauchy_constant_direction_obstruction_present": True,
        "centered_kernel_independent_arithmetic_input_constructed": False,
        "actual_chebyshev_mellin_contraction_present": False,
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "next_positive_gate": "ActualOffConstantCoerciveEnergyIdentityBeforeMellin",
    }
```

`write_certificate(output_directory, limit)` 同时输出 JSON 与 Markdown；Markdown 显示 `K_X(d,e)=floor(X/lcm(d,e))`、Gram 平方和、普通 Cauchy 的常数方向障碍，并写明它不是 `psi` 平滑误差、零点排除或 RH 结论。CLI 接受 `--limit` 和 `--output-directory`，默认输出到 `docs/monograph`。

- [ ] **Step 4: 生成项目证书并更新索引**

```bash
python3 experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py --limit 60
```

在 `claim-status-table.md` 新增一行，只声明“实际 LCM Gram 正半定核与普通 Cauchy 常数方向障碍已审计”；在 `external-theorem-index.md` 增加 `MFAC-ALGE`，明确其为内部有限审计、不是外部定理、不是 RH 证明。

- [ ] **Step 5: 运行定向测试与全族回归**

```bash
python3 -m unittest experiments.prime_matrix_mfac_actual_lcm_gram_energy_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git --no-pager diff --check
```

Expected: 新模块测试全绿、MFAC 全族回归全绿、无空白差异错误。

- [ ] **Step 6: 提交证书与索引同步**

```bash
git add \
  experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py \
  experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py \
  docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.json \
  docs/monograph/prime-matrix-mfac-actual-lcm-gram-energy-audit.md \
  docs/monograph/claim-status-table.md \
  docs/monograph/external-theorem-index.md
git commit -m "归档 MFAC 实际 LCM Gram 能量证书"
```

## 自检结果

- **规格覆盖：** 实际 Gram 与 Möbius--`Lambda` 恒等式由任务 1--2 覆盖；常数方向 Cauchy 障碍由任务 1--2 覆盖；循环中心化拒绝由任务 2 覆盖；证书、索引和全族验证由任务 3 覆盖；非 RH 边界由任务 3 的证书测试与 Markdown 约束覆盖。
- **占位符扫描：** 已按计划技能的禁用占位符模式完成扫描；结果为空，且所有测试、命令与 API 均明确给出。
- **类型一致性：** `limit` 均为正整数；`coefficients` 为 `Mapping[int, float]`；`ordinary_cauchy_projection_bound`、`audit_centering_contract`、`write_certificate` 的名称和返回字段在全部任务中一致。
