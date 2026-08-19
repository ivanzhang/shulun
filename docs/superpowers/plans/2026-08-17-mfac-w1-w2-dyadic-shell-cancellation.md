# MFAC W1→W2 相邻 Dyadic 壳抵消审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development`（推荐）或 `superpowers:executing-plans` 逐任务实施。本计划使用 checkbox（`- [ ]`）语法跟踪执行状态。

**Goal:** 构建有限 dyadic 壳账本审计器，精确核验 `Δ_j`、`N_j`、`F_D` 到 Möbius 核能量的重组，同时永久保持相邻壳支付、残余可和、远壳聚合与 W1→W2 开放。

**Architecture:** 单个标准库 Python 模块复用项目的精确 Möbius/Euler--φ/`gcd` 核模式，独立实现壳边界、块账本、严格合同、证书与 CLI；单元测试先固定状态、边界壳和精确残差，再实现最小功能。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`typing`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py` — 壳账本、合同、证书与 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.py` — 状态、账本、边界、合同和 CLI TDD。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.json` — 默认机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.md` — 默认人读证书。

## 锁定接口

1. `limit` 仅接受 `type(limit) is int and limit >= 3`。
2. `finite_dyadic_shell_ledger(limit)` 返回 `shells`、`block_matrix`、`diagonal_shell_energy`、`near_shell_energy`、`far_shell_energy`、`total_kernel_energy`，及：
   - `block_reassembly_residual == "0"`；
   - `near_far_reassembly_residual == "0"`；
   - `kernel_identity_residual == "0"`。
3. 壳记录字段为 `index`、`start`、`stop`、`is_truncated`；`limit=12` 必须给出最后壳 `[8,12)` 并标记 `is_truncated=True`。
4. `N_j` 由同壳非对角有序项与 `2Q_{j,j+1}` 组成；`F_D` 只含 `|j-k|>=2` 的有序块。所有值用 `Fraction` 精确计算并转字符串。
5. 合同把 `adjacent_shell_cancellation_lemma`、`summable_residual_lemma`、`far_shell_aggregation_lemma` 固定为内建 `False`；候选 `True` 一律拒绝。

### Task 1: 建立红灯状态测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.py`

- [ ] **Step 1: 写入固定开放状态测试**

```python
def test_valid_contract_keeps_all_shell_obligations_open(self) -> None:
    payload = audit_dyadic_shell_cancellation(default_contract(), limit=12)
    self.assertEqual(payload["finite_shell_ledger_status"], "verified_finite")
    self.assertEqual(payload["adjacent_shell_cancellation_obligation_status"], "open")
    self.assertEqual(payload["summable_residual_obligation_status"], "open")
    self.assertEqual(payload["far_shell_aggregation_obligation_status"], "open")
    self.assertEqual(payload["w1_to_w2_status"], "unproved")
    self.assertFalse(payload["rh_proved"])
```

- [ ] **Step 2: 运行红灯测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.MFACW1W2DyadicShellCancellationAuditTest.test_valid_contract_keeps_all_shell_obligations_open -v`

Expected: `ModuleNotFoundError`。

### Task 2: 实现最小合同入口

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py`

- [ ] **Step 1: 实现 `default_contract()` 与最小 `audit_dyadic_shell_cancellation()`**

最小载荷固定返回有限账本已核验、三项壳义务 `open`、`coprime_restricted_tail_bound_status=open`、`w1_to_w2_status=unproved`、`rh_proved=False`；不得实现或接收全局引理证明。

- [ ] **Step 2: 运行 Task 1 转绿**

Run: Task 1 命令。

Expected: PASS。

### Task 3: 锁定精确壳账本与截断边界红灯

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.py`

- [ ] **Step 1: 写入账本测试**

```python
def test_finite_ledger_reassembles_kernel_and_marks_boundary_shell(self) -> None:
    payload = finite_dyadic_shell_ledger(12)
    self.assertEqual(payload["block_reassembly_residual"], "0")
    self.assertEqual(payload["near_far_reassembly_residual"], "0")
    self.assertEqual(payload["kernel_identity_residual"], "0")
    self.assertEqual(payload["shells"][-1]["start"], 8)
    self.assertEqual(payload["shells"][-1]["stop"], 12)
    self.assertTrue(payload["shells"][-1]["is_truncated"])
```

增加 `limit in (True, 2, 12.0, "12")` 的拒绝测试；断言有限负 `N_j` 至多产生 `finite_cancellation_witnessed_or_not_witnessed`，不会关闭义务。

- [ ] **Step 2: 运行红灯测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.MFACW1W2DyadicShellCancellationAuditTest.test_finite_ledger_reassembles_kernel_and_marks_boundary_shell -v`

Expected: FAIL because `finite_dyadic_shell_ledger` is absent。

### Task 4: 实现精确壳分解

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py`

- [ ] **Step 1: 实现 `_require_limit()`、`mobius_value()`、`euler_phi()` 与 `_dyadic_shells()`**

所有函数添加中文 docstring；`_dyadic_shells(12)` 返回 `[2,4)`、`[4,8)`、`[8,12)`，最后壳明确标记截断。

- [ ] **Step 2: 实现 `finite_dyadic_shell_ledger()`**

使用 `a_d=Fraction(mobius_value(d), d)`、`K(d,e)=gcd(d,e)-1` 计算有序 `Q[j][k]`；由块矩阵独立计算总核、`Σ_j(Δ_j+N_j)` 与 `F_D`，输出三项 `Fraction` 零残差和有限见证状态。

- [ ] **Step 3: 运行 Task 3 转绿**

Run: Task 3 命令及非法截断测试。

Expected: PASS；边界壳不被误作完整壳。

### Task 5: 合同防火墙 TDD

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py`

- [ ] **Step 1: 写入并运行合同红灯**

覆盖未知/禁止来源、裸字符串、空 `uses`、缺失或额外 `claimed_uses`、错误截断统一变量、错误常数依赖、三项解析引理任意 `True`，以及规格所有结论提升字段。预期最小入口失败。

- [ ] **Step 2: 实现 `_validate_contract()` 并转绿**

允许来源仅为 `finite_arithmetic`、`mobius_definition`、`gcd_relation`、`dyadic_decomposition`、`euler_phi_divisor_sum`、`finite_sum_identity`；`claimed_uses` 键集合精确覆盖 `finite_shell_identity`、`finite_near_ledger`、`finite_far_ledger`。三个解析引理只能为内建 `False`。

- [ ] **Step 3: 运行完整新模块测试**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test -v`

Expected: PASS。

### Task 6: 证书、CLI 与回归

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-dyadic-shell-cancellation-audit.md`

- [ ] **Step 1: 写入 CLI 红灯测试**

在 `TemporaryDirectory` 调用脚本路径 `--limit 12 --json-out ... --markdown-out ...`；断言 JSON 可解析、边界壳存在、三个解析义务为 `open`，且 Markdown 包含“不证明统一 L² 上界”。

- [ ] **Step 2: 实现 `render_markdown()`、`write_certificate()` 与 `main()`**

CLI 接受 `--limit`、`--json-out`、`--markdown-out`。默认 Markdown 展示壳区间、三类账本、三项残差、有限见证和所有开放状态。

- [ ] **Step 3: 运行端到端与相邻回归**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test \
  experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test \
  experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test \
  experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test -v
python3 experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py --limit 512
git diff --check
```

Expected: 全部 PASS；证书存在；三项解析义务仍为 `open`；差异检查无输出。

## 实施完成判据

- 壳账本、近邻/远壳拆分和总核均为精确有限恒等式。
- 有限符号记录不改变三项解析义务、统一尾和界、W1→W2 或 RH 状态。
- 防火墙与 CLI 边界都有负向自动化测试。
