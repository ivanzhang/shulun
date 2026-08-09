# MFAC 全局自由乘法 Mellin 增长模反模型 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 审计自由局部有限乘法模型中的精确 Möbius 交替恒等式与 `beta>1/2` Mellin 增长模，证明 schema-level alternation 不足以给出实际整数的平方根消去。

**Architecture:** 新模块把有限自由交换单子作为可复算的代数样本：枚举单子元素、约数和、`mu_A` 与 `Lambda_A`，逐点检查 exact divisor-lattice identity。独立的连续轮廓函数验证对抗性增长模和最终导数正性。语料适配器只读既有前沿文档，明确缺失实际整数嵌入与 Mellin 收缩合同；完整 synthetic contraction fixture 只测试合同分类，不是算术证明。

**Tech Stack:** Python 3 标准库、`unittest`、JSON、Markdown。

---

## 文件结构

- 新建 `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py`：自由单子、精确 identity、Mellin 轮廓、合同分类、证书和 CLI。
- 新建 `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`：TDD 测试，覆盖恒等式、增长模、嵌入拒绝、synthetic 正例与证书边界。
- 新建 `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.json`：机器证书。
- 新建 `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.md`：人读边界与下一门。
- 修改 `docs/monograph/claim-status-table.md`：登记全局自由模型只否定 schema-only 推论。
- 修改 `docs/monograph/external-theorem-index.md`：登记 `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula`，不称为外部定理或 RH 进展。

### Task 1: 实现有限自由单子与精确交替恒等式

**Files:**
- Create: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py`
- Test: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`

- [ ] **Step 1: 写入精确 divisor-lattice identity 的失败测试**

```python
from prime_matrix_mfac_global_free_mellin_mode_no_go_audit import (
    FreeMonoidModel,
    audit_divisor_lattice_identity,
)


def test_free_monoid_preserves_lambda_equals_negative_mu_convolution_log(self) -> None:
    model = FreeMonoidModel({"a": 2.0, "b": 3.0, "c": 5.0})
    certificate = audit_divisor_lattice_identity(model, bound=30.0)

    self.assertTrue(certificate["identity_holds"])
    self.assertGreater(certificate["element_count"], 3)
    self.assertEqual(certificate["first_failure"], None)


def test_squarefree_depth_controls_alternating_divisor_sign(self) -> None:
    model = FreeMonoidModel({"a": 2.0, "b": 3.0})

    self.assertEqual(model.mobius((1, 1)), 1)
    self.assertEqual(model.mobius((1, 0)), -1)
    self.assertEqual(model.mobius((0, 1)), -1)
    self.assertEqual(model.mobius((2, 0)), 0)
```

- [ ] **Step 2: 运行测试，确认红色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v`
Expected: FAIL，因为自由单子模型与审计函数尚不存在。

- [ ] **Step 3: 实现局部有限枚举、Möbius 与 Lambda**

```python
@dataclass(frozen=True)
class FreeMonoidModel:
    """局部有限的带尺度自由交换单子，不代表自然数素数。"""

    atom_scales: dict[str, float]

    def divisors(self, exponent_vector: tuple[int, ...]) -> list[tuple[int, ...]]:
        return list(product(*(range(exponent + 1) for exponent in exponent_vector)))

    def lambda_value(self, exponent_vector: tuple[int, ...]) -> float:
        nonzero = [index for index, exponent in enumerate(exponent_vector) if exponent]
        if len(nonzero) != 1:
            return 0.0
        return math.log(self.scales[nonzero[0]])
```

`audit_divisor_lattice_identity` 必须逐元素计算：

```python
expected = -sum(
    model.mobius(divisor) * model.log_norm(divisor)
    for divisor in model.divisors(element)
)
```

并使用 `math.isclose` 比较 `expected` 与 `lambda_value(element)`；不得硬编码单个样本的结论。

- [ ] **Step 4: 运行测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v`
Expected: PASS；有限自由单子逐点满足 identity，squarefree 深度给出交替符号。

- [ ] **Step 5: 提交代数核心（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py
git commit -m "审计 MFAC 自由乘法交替恒等式"
```

### Task 2: 固定 Mellin 增长模与实际嵌入拒绝合同

**Files:**
- Modify: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py`
- Modify: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`

- [ ] **Step 1: 写入增长模、最终正性和合同分类的失败测试**

```python
from prime_matrix_mfac_global_free_mellin_mode_no_go_audit import (
    classify_contraction_contract,
    normalized_mellin_mode,
    positivity_threshold,
)


def test_beta_above_half_has_unbounded_normalized_mellin_subsequence(self) -> None:
    beta = 0.75
    tau = 1.0
    epsilon = 0.1
    first = normalized_mellin_mode(2.0 * math.pi, beta, tau, epsilon)
    second = normalized_mellin_mode(4.0 * math.pi, beta, tau, epsilon)

    self.assertGreater(abs(second), abs(first))
    self.assertGreater(second / first, 1.0)


def test_target_shell_derivative_is_positive_after_explicit_threshold(self) -> None:
    threshold = positivity_threshold(beta=0.75, tau=3.0, epsilon=0.1)
    self.assertGreater(threshold, 0.0)
    self.assertGreater(target_theta_derivative(threshold * 2.0, 0.75, 3.0, 0.1), 0.0)


def test_free_model_is_rejected_without_actual_integer_embedding(self) -> None:
    result = classify_contraction_contract({
        "fixed_actual_integer_embedding": False,
        "fixed_actual_chebyshev_measure": False,
    })
    self.assertEqual(result["classification"], "free_model_not_actual_integer_rh_attack")
    self.assertFalse(result["actual_chebyshev_mellin_contraction_present"])
```

- [ ] **Step 2: 运行测试，确认增长模与合同函数尚未实现**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v`
Expected: FAIL，因为 Mellin 函数、阈值计算和合同分类器尚不存在。

- [ ] **Step 3: 实现解析轮廓与完整合同字段**

```python
REQUIRED_CONTRACTION_FIELDS = (
    "fixed_actual_integer_embedding",
    "fixed_actual_chebyshev_measure",
    "exact_error_recurrence_on_actual_rows",
    "non_tagged_signed_kernel",
    "positive_or_coercive_energy_identity",
    "mellin_half_plane_spectral_contraction",
    "no_use_of_rh_or_zero_free_input",
)


def normalized_mellin_mode(t: float, beta: float, tau: float, epsilon: float) -> float:
    """返回自由轮廓的归一化 Mellin 增长模。"""
    return epsilon * math.exp((beta - 0.5) * t) * math.cos(tau * t)


def target_theta_derivative(x: float, beta: float, tau: float, epsilon: float) -> float:
    """计算目标连续 shell 轮廓的一阶导数。"""
    phase = tau * math.log(x)
    return 1.0 + epsilon * x ** (beta - 1.0) * (
        beta * math.cos(phase) - tau * math.sin(phase)
    )


def positivity_threshold(beta: float, tau: float, epsilon: float) -> float:
    """给出导数至少为 1/2 的充分阈值。"""
    amplitude = epsilon * math.hypot(beta, tau)
    return max(1.0, (2.0 * amplitude) ** (1.0 / (1.0 - beta)))


def classify_contraction_contract(record: dict[str, Any]) -> dict[str, Any]:
    """区分自由模型、完整 synthetic 合同与未闭合实际合同。"""
    if not record.get("fixed_actual_integer_embedding"):
        return {
            **record,
            "classification": "free_model_not_actual_integer_rh_attack",
            "actual_chebyshev_mellin_contraction_present": False,
        }
    complete = all(record.get(field) for field in REQUIRED_CONTRACTION_FIELDS)
    return {
        **record,
        "classification": "synthetic_complete_contraction_contract" if complete else "actual_contraction_contract_incomplete",
        "actual_chebyshev_mellin_contraction_present": complete and not record.get("synthetic_fixture", False),
    }
```

`positivity_threshold` 必须基于：

```text
1 - epsilon * sqrt(beta^2 + tau^2) * X^(beta-1) > 0
```

给出一个充分而非最优的阈值。完整 synthetic contraction fixture 必须要求所有
`REQUIRED_CONTRACTION_FIELDS` 为真，但返回值仍带：

```text
synthetic_fixture=true
rh_proved=false
```

- [ ] **Step 4: 运行测试，确认增长模与拒绝路径绿色**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v`
Expected: PASS；`beta>1/2` 子序列增长、充分正性阈值与自由模型拒绝均成立。

- [ ] **Step 5: 提交 Mellin 合同（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py
git commit -m "审计 MFAC 自由 Mellin 增长模"
```

### Task 3: 生成当前语料证书并同步前沿状态

**Files:**
- Modify: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py`
- Modify: `experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.md`
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写入当前语料与证书边界的失败测试**

```python
def test_current_corpus_has_no_actual_chebyshev_mellin_contraction(self) -> None:
    certificate = audit_current_corpus(ROOT)
    self.assertTrue(certificate["exact_divisor_lattice_identity_available"])
    self.assertTrue(certificate["free_mellin_growth_countermodel_constructed"])
    self.assertFalse(certificate["alternation_only_implies_sqrt_cancellation"])
    self.assertFalse(certificate["actual_chebyshev_mellin_contraction_present"])
    self.assertEqual(
        certificate["next_positive_gate"],
        "ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula",
    )
    self.assertFalse(certificate["rh_proved"])


def test_writer_keeps_countermodel_distinct_from_rh_counterexample(self) -> None:
    certificate = audit_current_corpus(ROOT)
    with tempfile.TemporaryDirectory() as directory:
        markdown_path = Path(directory) / "certificate.md"
        write_certificate(certificate, Path(directory) / "certificate.json", markdown_path)
        markdown = markdown_path.read_text(encoding="utf-8")
    self.assertIn("不是自然数素数的反例", markdown)
    self.assertIn("不对应实际 zeta 零点", markdown)
    self.assertIn("rh_proved=false", markdown)
```

- [ ] **Step 2: 运行测试，确认语料适配器与写出函数失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v`
Expected: FAIL，因为 `audit_current_corpus`、`write_certificate` 与 CLI 尚未实现。

- [ ] **Step 3: 实现只读适配器、证书和 CLI**

`audit_current_corpus` 必须只读：

```text
docs/monograph/mfac-frontier-conclusion-and-proof-obligation-chain-20260807.md
docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json
docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json
```

它必须检查这些材料不含实际 Mellin 收缩合同，并把这种“当前语料缺口”与“数学上不存在收缩律”严格分开。CLI 默认写出本任务的 JSON/Markdown 证书，并支持 `--json-out` 与 `--markdown-out`。

- [ ] **Step 4: 运行定向测试、生成证书并检查格式**

Run: `python3 -m unittest experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py -v && python3 experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py && git diff --check`
Expected: PASS；证书只说明自由模型排除 schema-only 推论，未声称自然数 RH 反例或 RH 结论。

- [ ] **Step 5: 同步索引并运行全族回归**

在 `claim-status-table.md` 与 `external-theorem-index.md` 登记：本审计只说明 alternation/recurrence 不足以强迫平方根消去；它不证明实际整数上的增长模、零点存在、零点排除、`ψ` 界或 RH。

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`
Expected: PASS；MFAC 审计族含新测试且全绿。

- [ ] **Step 6: 提交证书与状态同步（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit_test.py docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.json docs/monograph/prime-matrix-mfac-global-free-mellin-mode-no-go-audit.md docs/monograph/claim-status-table.md docs/monograph/external-theorem-index.md
git commit -m "审计 MFAC 全局自由 Mellin 反模型"
```

## 计划自检

- 有限自由单子身份、Mellin 增长、最终正性、实际整数嵌入拒绝、synthetic contraction fixture、当前语料缺口、非 RH 边界和状态索引均有对应任务。
- 任何数值实验只验证已编码模型；不把自由模型写成自然数 prime system 或 zeta 零点反例。
- `ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula` 只作为下一正向门登记，未被实现为已证明定理。
