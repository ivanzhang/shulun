# MFAC Euler–Gauss–Riemann 三层因子化审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 有限核验 Euler Möbius 反演、Gauss LCM Gram 与 Riemann Mellin 定义域三层因子化，并把跨尺度前缀和强制性登记为未证明门。

**Architecture:** 一个标准库模块实现算术系数、有限恒等式、严格来源合同、JSON/Markdown 证书和 CLI；一个 `unittest` 模块覆盖逐点恒等式、Gram 等式、离散校正与防循环状态。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`math`、`pathlib`、`typing`、`unittest`）。

---

### Task 1: 建立 Euler–Gauss 红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test.py`

- [x] **Step 1: 测试有限 Möbius 反演、Gram 与离散校正**

```python
def test_finite_factorization_matches_lambda_gram_and_continuous_correction(self) -> None:
    audit = audit_euler_gauss_riemann_factorization(limit=30)
    self.assertEqual(audit["euler_inversion_mismatch_count"], 0)
    self.assertAlmostEqual(audit["gauss_gram_residual"], 0.0)
    self.assertAlmostEqual(audit["discrete_continuous_correction_residual"], 0.0)
```

- [x] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test.MFACEulerGaussRiemannFactorizationAuditTest.test_finite_factorization_matches_lambda_gram_and_continuous_correction -v`

Expected: FAIL with `ModuleNotFoundError`。

### Task 2: 实现有限三层核验

**Files:**
- Create: `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py`

- [x] **Step 1: 实现系数、divisor transform、LCM Gram 和校正采样**

```python
def audit_euler_gauss_riemann_factorization(limit: int) -> dict[str, object]:
    """有限核验三层因子化，绝不升级为 Mellin 收缩或 RH。"""
    ...
```

系数固定为 `-mobius(d) * log(d)`；对整数与 `n + 0.5` 采样点验证 `floor(x)-x` 校正。

- [x] **Step 2: 运行 Task 1 测试确认转绿**

Run: 同上。Expected: PASS。

### Task 3: 添加定义域与防循环红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test.py`

- [x] **Step 1: 测试 Mellin 域、禁项与伪造结论拒绝**

```python
def test_contract_rejects_bad_mellin_domain_cycles_and_promoted_conclusions(self) -> None:
    with self.assertRaisesRegex(ValueError, "real_part"):
        audit_mellin_identity_contract({"real_part": 1.0, ...})
    for source in ("RH", "Mellin_contraction", "finite_profile"):
        ...
    with self.assertRaisesRegex(ValueError, "目标结论"):
        audit_mellin_identity_contract({..., "rh_proved": False})
```

- [x] **Step 2: 运行测试确认红灯**

Expected: FAIL，直到禁项与结论字段被完整验证。

### Task 4: 证书与 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py`
- Modify: `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.md`

- [x] **Step 1: 写出证书与 CLI**

CLI 接受 `--limit`、`--json-out`、`--markdown-out`；证书必须列出三层公式、
`real_part_greater_than_one` 定义域和 `cross_scale_prefix_coercivity_status=unproved`。

- [x] **Step 2: 添加脚本路径 CLI 测试并完成验证**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test -v
python3 experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py --limit 96
```

Expected: 全部 PASS，默认 JSON/Markdown 均保持 RH 未证明边界。
