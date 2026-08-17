# MFAC W1→W2 初等绝对值包络障碍审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development`（推荐）或 `superpowers:executing-plans` 逐任务实施。本计划使用 checkbox（`- [ ]`）跟踪执行状态。

**Goal:** 新增完全非循环的有限 Möbius 尾和绝对值包络审计器，精确验证有限不等式与 `r=2` 的 dyadic 有限增长见证，同时永久保持 W1→W2、统一 L² 上界和 RH 未证明。

**Architecture:** 单一标准库 Python 模块封装精确 `Fraction` 算术、严格来源合同、有限包络模型、dyadic 见证、JSON/Markdown 证书与 CLI；单元测试先行锁定算术、输入、反循环和输出边界。所有有限增长都记录为样本内结论，绝不推导全局发散。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`typing`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py` — 精确有限模型、合同验证、证书和 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.py` — TDD 红灯、反循环和 CLI 回归测试。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.json` — 默认机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.md` — 默认人读证书与使用边界。

## 锁定的合同与有限模型

1. `limit` 只接受内建 `int` 且 `limit >= 3`；拒绝 `bool`、浮点数、字符串和整数子类。
2. 对 `2 <= r < D`，模块以 `Fraction` 同时直接枚举 `T_D(r)` 与互素分解式，要求残差恰为零；再构造 `B_D(r)`，逐项验证 `B_D(r) - abs(T_D(r)) >= 0`，并验证 `A_D - E_D >= 0`。
3. `r=2` dyadic 序列选择不超过 `limit` 的最后 `dyadic_levels` 个连续二幂截断；例如 `limit=512, dyadic_levels=5` 固定为 `(32, 64, 128, 256, 512)`。`dyadic_levels` 必须为正内建整数，且不得超过可用二幂尺度数。
4. 对相邻尺度 `D, 2D`，精确记录
   `B_{2D}(2)-B_D(2) = 1/2 * sum_{D/2 <= m < D, m odd}(1/m)`；预声明单项下界 `1/(2*(D-1))`，因此仅登记该有限序列严格增长。该有限块不构成 `D→∞` 发散证明。
5. 合同字段为 `uses` 与 `claimed_uses`。两者均为严格字符串序列/映射；每项 `claimed_uses` 是 `uses` 的非空子集。只允许规格中的五种有限来源，拒绝全部禁止来源。任何证明性结论字段若存在，必须是内建 `bool` 的 `False`；固定状态字段不得被调用方提升。

### Task 1: 写入最小红灯测试与公开接口

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.py`

- [ ] **Step 1: 写入合法合同的状态边界测试**

测试期望的公开 API 为 `default_contract()` 与
`audit_elementary_envelope_barrier(contract, limit=..., dyadic_levels=...)`。最小合法合同必须产生：

```python
payload = audit_elementary_envelope_barrier(default_contract(), limit=12, dyadic_levels=2)
self.assertEqual(payload["finite_inequality_status"], "verified_finite")
self.assertEqual(payload["finite_growth_status"], "finite_growth_witnessed")
self.assertEqual(payload["nonuniformity_obligation_status"], "open")
self.assertEqual(payload["w1_to_w2_status"], "unproved")
self.assertFalse(payload["rh_proved"])
```

- [ ] **Step 2: 运行测试确认红灯**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.MFACW1W2ElementaryEnvelopeBarrierAuditTest.test_valid_contract_keeps_all_global_obligations_open -v
```

Expected: FAIL with `ModuleNotFoundError`，因为审计模块尚不存在。

### Task 2: 实现最小精确有限算术并使首个测试转绿

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py`

- [ ] **Step 1: 实现纯标准库数论和输入基础验证**

实现 `_require_limit()`、`mobius_value()`、`euler_phi()`、`_checked_string_tuple()` 与
`_validate_contract()`。所有算术保留为 `Fraction`；为每个新函数添加中文 docstring。合同使用
`finite_arithmetic`、`mobius_definition`、`coprimality_relation`、`triangle_inequality`、
`finite_sum_identity` 的允许集合，并拒绝规格列出的循环输入与结论提升。

- [ ] **Step 2: 实现有限包络模型和审计载荷**

实现 `finite_elementary_envelope_model(limit)`：返回直接尾和、分解式尾和、包络、逐项余量、
`E_D`、`A_D` 及全部精确残差的可 JSON 序列化表示。`audit_elementary_envelope_barrier()` 调用该模型，
固定写入五项状态，绝不根据数值改写解析义务。

- [ ] **Step 3: 运行 Task 1 测试确认转绿**

Run: Task 1 中的单测命令。

Expected: PASS；有限状态成立，但 `nonuniformity_obligation_status` 始终为 `open`。

### Task 3: 用红灯测试锁定精确不等式和 dyadic 增长边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.py`

- [ ] **Step 1: 添加有限恒等式与聚合不等式测试**

针对小截断（至少 `D=12`）断言：候选模数为 `range(2, D)`、每个直接尾和与互素分解残差为 `"0"`、
每项 `B_D(r)-abs(T_D(r))` 非负、聚合残差 `A_D-E_D` 非负，并且 `r=2` 项确为 `A_D` 的非负组成部分。
不要断言浮点近似或任何渐近趋势。

- [ ] **Step 2: 添加 dyadic 见证测试**

针对 `limit=32, dyadic_levels=3` 断言 dyadic 尺度为 `(8, 16, 32)`；每个相邻增量的精确奇数块恒等式残差为
`"0"`，且增量不小于预声明 `1/(2*(D-1))`，状态仅为 `finite_growth_witnessed`。再测试过多 levels、零、
`bool`、浮点数和字符串均被拒绝。

- [ ] **Step 3: 运行新增测试确认红灯**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.MFACW1W2ElementaryEnvelopeBarrierAuditTest.test_finite_model_verifies_exact_tail_and_envelope_inequalities \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.MFACW1W2ElementaryEnvelopeBarrierAuditTest.test_dyadic_witness_is_exact_and_finite_only -v
```

Expected: FAIL，因为最小实现尚未提供逐模数余量和 dyadic 见证载荷。

### Task 4: 实现见证、全面防火墙与状态不可升级规则

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.py`

- [ ] **Step 1: 实现 dyadic 见证函数**

实现 `dyadic_envelope_growth_witness(limit, dyadic_levels)`，返回尺度、各尺度 `B_D(2)^2`、相邻奇数块和、
精确增量与下界比较。使用整数二幂索引和 `Fraction`，禁止浮点 `log` 判断。对于无法组成所需连续尺度的
输入，抛出含字段名的 `ValueError`。

- [ ] **Step 2: 添加合同负向测试**

覆盖：非 `Mapping` 合同、裸字符串/非字符串来源、空或未声明 `claimed_uses`、每个禁止来源、
`uniform_l2_upper_proved=True`、`w1_to_w2_proved=True`、`w2_closed=True`、
`chebyshev_energy_bridge_proved=True`、`rh_proved=True` 与 `rh_consequence=True`。测试还应确认
`finite_growth_status` 或 `nonuniformity_obligation_status` 的伪造提升被拒绝，而不是被静默覆盖。

- [ ] **Step 3: 运行 Task 3 和合同负向测试确认转绿**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test -v
```

Expected: PASS；所有数值字段是有限证书，所有全局结论仍未证明。

### Task 5: 完成证书、CLI 与端到端回归

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-elementary-envelope-barrier-audit.md`

- [ ] **Step 1: 实现证书渲染与 CLI**

实现 `render_markdown()`、`write_certificate()` 和 `main()`；CLI 接受 `--limit`、`--dyadic-levels`、
`--json-out`、`--markdown-out`。JSON 将 `Fraction` 转为稳定字符串；Markdown 必须逐字展示：

```text
finite_inequality_status=verified_finite
finite_growth_status=finite_growth_witnessed
nonuniformity_obligation_status=open
w1_to_w2_status=unproved
rh_proved=false
```

并使用中文说明有限增长不是全局发散，且模块未证明统一 L² 上界、Chebyshev 桥或 RH。

- [ ] **Step 2: 添加写证书、模块 CLI 与脚本路径 CLI 测试**

在临时目录验证 JSON 可解析、Markdown 含上述五项状态与“不证明”边界；分别运行
`python3 -m unittest ...`、`python3 -m experiments...`（若目录行为支持）和规格要求的脚本路径调用。测试
不得依赖仓库中既有未提交证书文件。

- [ ] **Step 3: 生成默认证书并执行相关回归**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test -v
python3 experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py \
  --limit 512 --dyadic-levels 5
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test \
  experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test -v
git diff --check
```

Expected: 新模块测试和相关 W1→W2 回归全部 PASS；默认证书存在；`git diff --check` 无输出；既有未提交文件未被修改。

## 实施完成判据

- 只新增本计划列出的模块、测试和默认两份证书。
- `Fraction` 精确余量替代全部浮点判断；非法输入和错误状态提升均可由负向测试拒绝。
- 证书严格区分 `verified_finite`、`finite_growth_witnessed` 与 `open`，没有任何有限数据被表述为全局发散或统一性否定。
- 实施者必须在每个红灯步骤先观察预期失败，再写最小实现使其转绿。
