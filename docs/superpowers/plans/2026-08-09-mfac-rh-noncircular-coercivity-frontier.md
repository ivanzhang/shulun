# MFAC RH 非循环强制性前沿 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 MFAC 从一维非循环 LCM Gram 见证推进为可证伪的有限维统一性审计，并显式阻断把有限证书升级为 Mellin 收缩或 RH 证明的跳步。

**Architecture:** 新模块只使用实际整数 LCM Gram 条目与精确有理数；一个候选族生成器负责去常数正交化，另一个有限维审计器输出最小能量和依赖合同。Mertens 模块同步降级退化的层内洗牌代理。文档只登记证书与未闭合的解析引理。

**Tech Stack:** Python 3 标准库（`fractions`、`dataclasses`、`json`、`unittest`）。

---

### Task 1: 将 Mertens 层内洗牌降级为退化诊断

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Modify: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.json`
- Modify: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.md`

- [ ] **Step 1: 写出退化层测试**

```python
def test_squarefree_omega_layers_are_marked_as_sign_deterministic(self) -> None:
    result = diagnose_layer_shuffle({1: [-1, -1], 2: [1, 1]})
    self.assertTrue(result["sign_deterministic_by_layer"])
    self.assertEqual(result["comparison_status"], "degenerate_not_independent_baseline")
```

- [ ] **Step 2: 确认红灯**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: FAIL，提示 `diagnose_layer_shuffle` 未定义。

- [ ] **Step 3: 最小实现退化分类**

```python
def diagnose_layer_shuffle(layers: Mapping[int, Sequence[int]]) -> dict[str, bool | str]:
    deterministic = all(len(set(values)) <= 1 for values in layers.values())
    return {
        "sign_deterministic_by_layer": deterministic,
        "comparison_status": (
            "degenerate_not_independent_baseline" if deterministic
            else "nondegenerate_empirical_permutation_only"
        ),
    }
```

- [ ] **Step 4: 确认绿灯并重写证书措辞**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v && python3 experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

Expected: 所有测试通过，证书把层内洗牌称为退化诊断而非独立基线。

### Task 2: 固定有限维非循环见证族合同

**Files:**
- Create: `experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit.py`
- Create: `experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py`

- [ ] **Step 1: 写出不读取目标误差的失败测试**

```python
def test_candidate_contract_rejects_target_error_dependency(self) -> None:
    result = audit_candidate_contract({"uses": ["psi(X)-X"]})
    self.assertEqual(result["status"], "forbidden_target_dependency")

def test_e2_candidate_is_exactly_orthogonal_to_constant_direction(self) -> None:
    candidate = e2_offconstant_candidate(12)
    self.assertEqual(candidate.constant_inner_product, Fraction(0, 1))
```

- [ ] **Step 2: 确认红灯**

Run: `python3 -m unittest experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py -v`

Expected: FAIL，提示候选模块不存在。

- [ ] **Step 3: 最小实现精确 `e_2` 候选及合同审计**

```python
def e2_offconstant_candidate(limit: int) -> Candidate:
    coefficient = Fraction(limit // 2, limit)
    return Candidate(
        coefficient=coefficient,
        constant_inner_product=Fraction(limit // 2, 1) - coefficient * limit,
    )
```

合同拒绝 `psi(X)-X`、`Chebyshev_error`、`Mellin`、`zeta_zero` 与 `explicit_formula`，且只接受明确的字符串依赖列表。

- [ ] **Step 4: 确认绿灯**

Run: `python3 -m unittest experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py -v`

Expected: 精确正交测试与依赖拒绝测试均通过。

### Task 3: 审计有限维 Gram 强制性，禁止统一性外推

**Files:**
- Modify: `experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit.py`
- Modify: `experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-uniform-offconstant-coercivity-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-uniform-offconstant-coercivity-audit.md`

- [ ] **Step 1: 写出有限范围状态测试**

```python
def test_finite_scan_never_claims_uniform_coercivity(self) -> None:
    certificate = audit_finite_family(limits=[12, 18], indices=[2, 3])
    self.assertEqual(certificate["status"], "finite_coercivity_scan_not_uniform_theorem")
    self.assertFalse(certificate["uniform_coercivity_proved"])
```

- [ ] **Step 2: 确认红灯**

Run: `python3 -m unittest experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py -v`

Expected: FAIL，提示 `audit_finite_family` 未定义。

- [ ] **Step 3: 最小实现精确 Gram 扫描**

对每个 `limit` 与候选索引建立有理数 Gram 矩阵；输出对角能量、所有 `2x2` 主子式和数值化最小特征值，仅将其标记为有限扫描读数。任何转换成浮点的结果必须检查有限性。

- [ ] **Step 4: 确认绿灯及证书边界**

Run: `python3 -m unittest experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py -v && python3 experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit.py`

Expected: 测试与默认证书生成通过，且 JSON 保持 `uniform_coercivity_proved=false`、`actual_mellin_contraction_present=false`、`rh_proved=false`。

### Task 4: 登记 Mellin 提升前必须证明的解析引理

**Files:**
- Create: `docs/monograph/mfac-offconstant-coercivity-to-mellin-obligation.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写出精确义务清单**

文档必须将以下三项拆开：全尺度强制常数、实际 Chebyshev 误差到见证能量的非循环桥接、由 dyadic 能量到 Mellin 范数的可和性。不得把任何一项写成已经成立。

- [ ] **Step 2: 范围检查**

Run: `rg -n "rh_proved=true|actual_mellin_contraction_present=true" docs/monograph/mfac-offconstant-coercivity-to-mellin-obligation.md docs/monograph/external-theorem-index.md`

Expected: 无匹配。

### Task 5: 全量验证与提交

**Files:**
- Modify: 本计划涉及的全部文件

- [ ] **Step 1: 运行回归验证**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py experiments/prime_matrix_mfac_uniform_offconstant_coercivity_audit_test.py -v`

Expected: 全部测试通过。

- [ ] **Step 2: 检查工作区范围**

Run: `git diff --check && git status --short`

Expected: 无空白错误；不暂存用户单独修改的 `AGENTS.md`。

- [ ] **Step 3: 创建存档提交**

Run: `git add <本计划对应文件> && git commit -m "规划 MFAC 非循环强制性前沿"`

Expected: 仅包含 MFAC 审计、研究设计、计划和证书文件。
