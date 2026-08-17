# MFAC W1→W2 双线性核对角—非对角抵消审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development`（推荐）或 `superpowers:executing-plans` 逐任务实施。本计划使用 checkbox（`- [ ]`）语法跟踪执行状态。

**Goal:** 新增非循环有限核审计器，精确核验 Möbius 尾和 Euler--φ 能量的 `gcd(d,e)-1` 核展开、Gram 表示及对角—非对角分解，同时保持统一 L² 界、W1→W2 和 RH 未证明。

**Architecture:** 单个标准库模块实现严格来源合同、`Fraction` 有限模型、有限抵消见证、JSON/Markdown 证书及 CLI；测试先行锁定状态、精确核残差、来源防火墙和证书边界。本期合同将 `offdiagonal_cancellation_lemma` 固定为内建 `False`，不接受调用者声称已得到全局抵消。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`typing`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py` — 合同、精确核模型、证书和 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py` — 状态、数学、合同和 CLI 测试。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.json` — 默认机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.md` — 默认人读证书。

## 锁定接口与有限断言

1. `limit` 必须满足 `type(limit) is int and limit >= 3`。
2. `finite_bilinear_kernel_model(limit)` 计算：
   - `divisor_sum_energy = Σ_r φ(r)T_D(r)^2`；
   - `kernel_energy = Σ_{d,e} a_d a_e(gcd(d,e)-1)`；
   - `gram_energy = Σ_{d,e}a_da_eΣ_{r|d,r|e,r>=2}φ(r)`；
   - `diagonal_energy`、`offdiagonal_energy` 与三项精确零残差。
3. 若有限 `offdiagonal_energy < 0`，只登记 `finite_cancellation_witnessed`；否则为 `not_witnessed`。无论符号，`diagonal_cancellation_obligation_status=open`。
4. 以 `D=12` 作为回归样本：`offdiagonal_energy == "-277/450"`，绝不外推为全局抵消。
5. `default_contract()` 含 `kernel_identity=True`、`gram_positivity=True`、`offdiagonal_cancellation_lemma=False`、`uniformity_variable="truncation"`、`constant_dependency="fixed_test_function"`，及精确三项 `claimed_uses`：`finite_kernel_identity`、`finite_gram_positivity`、`finite_cancellation_witness`。
6. 允许来源仅为 `finite_arithmetic`、`mobius_definition`、`gcd_relation`、`euler_phi_divisor_sum`、`finite_gram_decomposition`、`finite_sum_identity`；未知、禁止、空、裸字符串、未声明和额外义务全部拒绝。

### Task 1: 写入状态合同红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py`

- [ ] **Step 1: 写入公开入口期望**

```python
def test_valid_contract_keeps_uniform_conclusions_open(self) -> None:
    payload = audit_bilinear_kernel_cancellation(default_contract(), limit=12)
    self.assertEqual(payload["finite_kernel_identity_status"], "verified_finite")
    self.assertEqual(payload["finite_gram_positivity_status"], "verified_finite")
    self.assertEqual(payload["diagonal_cancellation_obligation_status"], "open")
    self.assertEqual(payload["coprime_restricted_tail_bound_status"], "open")
    self.assertEqual(payload["w1_to_w2_status"], "unproved")
    self.assertFalse(payload["rh_proved"])
```

- [ ] **Step 2: 运行并观察红灯**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.MFACW1W2BilinearKernelCancellationAuditTest.test_valid_contract_keeps_uniform_conclusions_open -v
```

Expected: FAIL with `ModuleNotFoundError`。

### Task 2: 实现最小状态入口

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py`

- [ ] **Step 1: 定义默认合同与最小审计函数**

```python
def audit_bilinear_kernel_cancellation(
    contract: Mapping[str, object], limit: object
) -> dict[str, object]:
    """登记有限核结论，绝不提升统一解析状态。"""
    del contract, limit
    return {
        "finite_kernel_identity_status": "verified_finite",
        "finite_gram_positivity_status": "verified_finite",
        "diagonal_cancellation_obligation_status": "open",
        "coprime_restricted_tail_bound_status": "open",
        "w1_to_w2_status": "unproved",
        "rh_proved": False,
    }
```

`default_contract()` 必须把 `offdiagonal_cancellation_lemma` 写为内建 `False`。

- [ ] **Step 2: 运行 Task 1 并确认转绿**

Run: Task 1 命令。

Expected: PASS。

### Task 3: 写入精确核模型红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py`

- [ ] **Step 1: 锁定三种能量与有限见证**

```python
def test_model_matches_divisor_kernel_gram_and_diagonal_split(self) -> None:
    payload = finite_bilinear_kernel_model(12)
    self.assertEqual(payload["candidate_indices"], tuple(range(2, 12)))
    self.assertEqual(payload["divisor_kernel_residual"], "0")
    self.assertEqual(payload["kernel_gram_residual"], "0")
    self.assertEqual(payload["diagonal_offdiagonal_residual"], "0")
    self.assertGreaterEqual(Fraction(payload["gram_energy"]), 0)
    self.assertEqual(payload["offdiagonal_energy"], "-277/450")
    self.assertEqual(payload["finite_cancellation_status"], "finite_cancellation_witnessed")
    self.assertEqual(payload["diagonal_cancellation_obligation_status"], "open")
```

同一测试类增加 `limit in (True, 2, 12.0, "12")` 的 `ValueError` 断言。

- [ ] **Step 2: 运行并观察红灯**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.MFACW1W2BilinearKernelCancellationAuditTest.test_model_matches_divisor_kernel_gram_and_diagonal_split -v
```

Expected: FAIL because `finite_bilinear_kernel_model` is absent。

### Task 4: 实现精确有限核与分解

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py`

- [ ] **Step 1: 实现数论和输入辅助函数**

实现 `_require_limit()`、`mobius_value()`、`euler_phi()`；每个函数有中文 docstring，拒绝非内建正整数。

- [ ] **Step 2: 实现 `finite_bilinear_kernel_model()`**

```python
coefficient = Fraction(mobius_value(index), index)
kernel = gcd(left_index, right_index) - 1
gram_kernel = sum(
    (Fraction(euler_phi(modulus), 1)
     for modulus in range(2, checked_limit)
     if left_index % modulus == 0 and right_index % modulus == 0),
    Fraction(0, 1),
)
```

分别独立求和生成 `divisor_sum_energy`、`kernel_energy`、`gram_energy`，以及对角/非对角账本。将 `Fraction` 渲染为稳定字符串；所有残差必须精确为零。只有有限符号满足时才写 `finite_cancellation_witnessed`。

- [ ] **Step 3: 运行 Task 3 并确认转绿**

Run: Task 3 命令和非法截断测试。

Expected: PASS；不输出任何统一 L² 或 RH 结论。

### Task 5: 写入来源防火墙红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py`

- [ ] **Step 1: 写入伪造来源和结论测试**

```python
def test_contract_rejects_unallowed_sources_extra_claims_and_promotions(self) -> None:
    unknown = default_contract()
    unknown["uses"] += ("unregistered_source",)
    with self.assertRaisesRegex(ValueError, "未允许"):
        audit_bilinear_kernel_cancellation(unknown, limit=12)

    forged = default_contract()
    forged["offdiagonal_cancellation_lemma"] = True
    with self.assertRaisesRegex(ValueError, "offdiagonal_cancellation_lemma"):
        audit_bilinear_kernel_cancellation(forged, limit=12)

    promoted = default_contract()
    promoted["uniform_l2_upper_proved"] = True
    with self.assertRaisesRegex(ValueError, "uniform_l2_upper_proved"):
        audit_bilinear_kernel_cancellation(promoted, limit=12)
```

增加非 `Mapping` 合同、裸字符串、空来源、禁止来源、缺失/额外 `claimed_uses`、错误统一变量、错误常数依赖、非内建 `bool` 和全部规格结论字段的断言。

- [ ] **Step 2: 运行并观察红灯**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.MFACW1W2BilinearKernelCancellationAuditTest.test_contract_rejects_unallowed_sources_extra_claims_and_promotions -v
```

Expected: FAIL because minimal audit has no strict validation。

### Task 6: 实现合同验证并整合模型

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py`

- [ ] **Step 1: 实现严格 `_validate_contract()`**

`uses` 必须是非空 `tuple` 或 `list` 的字符串序列且为允许集子集。`claimed_uses` 必须是键集合精确等于 `finite_kernel_identity`、`finite_gram_positivity`、`finite_cancellation_witness` 的 `Mapping`，每项为非空 `uses` 子集。`kernel_identity`/`gram_positivity` 必须是内建 `True`，`offdiagonal_cancellation_lemma` 必须是内建 `False`。任何禁止结论字段只要出现即拒绝。

- [ ] **Step 2: 合并固定状态与有限模型**

```python
checked = _validate_contract(contract)
finite = finite_bilinear_kernel_model(limit)
return {
    **checked,
    **finite,
    "finite_kernel_identity_status": "verified_finite",
    "finite_gram_positivity_status": "verified_finite",
    "diagonal_cancellation_obligation_status": "open",
    "coprime_restricted_tail_bound_status": "open",
    "w1_to_w2_status": "unproved",
    "rh_proved": False,
}
```

- [ ] **Step 3: 运行完整新模块测试**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test -v
```

Expected: PASS。

### Task 7: 实现证书、CLI 和回归

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-bilinear-kernel-cancellation-audit.md`

- [ ] **Step 1: 写入 CLI 红灯测试**

在 `TemporaryDirectory` 用脚本路径运行 `--limit 12 --json-out ... --markdown-out ...`。断言 JSON 中 `offdiagonal_energy == "-277/450"`、`diagonal_cancellation_obligation_status == "open"`；Markdown 包含：

```text
finite_kernel_identity_status=verified_finite
finite_gram_positivity_status=verified_finite
diagonal_cancellation_obligation_status=open
coprime_restricted_tail_bound_status=open
w1_to_w2_status=unproved
rh_proved=false
```

并包含中文“不证明统一 L² 上界”边界。先运行该测试并确认因 CLI 缺失而失败。

- [ ] **Step 2: 实现写证书和 CLI**

实现 `render_markdown()`、`write_certificate()` 和 `main()`。默认输出为本任务两份 `docs/monograph/` 文件；CLI 接受 `--limit`、`--json-out` 与 `--markdown-out`。Markdown 显示三种能量、三类残差、对角/非对角项、有限见证和六项状态。

- [ ] **Step 3: 运行端到端和相邻回归**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test \
  experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test \
  experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test -v
python3 experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py --limit 512
git diff --check
```

Expected: 全部 PASS；默认证书存在；统一性义务仍为 `open`；差异检查无输出。

## 实施完成判据

- 仅验证有限 `gcd-1` 核、Gram 表示和对角—非对角账本的精确代数关系。
- 有限负非对角项只能写为 `finite_cancellation_witnessed`，不生成统一 L²、W1→W2、Chebyshev 或 RH 证明状态。
- 来源白名单、逐义务声明、伪造抵消和目标结论循环均有可重复负向测试。
- 证书用中文明确写出“正半定不等于统一有界”，并给出可运行 CLI 示例。
