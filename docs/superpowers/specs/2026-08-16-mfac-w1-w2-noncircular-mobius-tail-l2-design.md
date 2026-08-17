# MFAC W1→W2 非循环 Möbius 尾和 L² 桥审计设计

**日期：**2026-08-16
**状态：**已实施、已验证，待提交

## 目标

为 MFAC 主链的 W1→W2 缺口增加一个可审计的非循环桥登记器。该登记器把
互素限制 Möbius 尾和、Euler--φ L² 聚合与 Chebyshev 能量传递拆成独立义务，
并用严格输入边界和有限可证伪模型阻止将条件、数值或目标结论伪装为证明。

本工作只改进缺口定位、有限恒等式核验和依赖透明度；不证明 W1→W2、W2、
Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。

## 非目标

- 不接受全 ε Mertens 界、PNT、RH、零点信息、显式公式或 Mellin 论证作为桥输入。
- 不把有限截断数值、有限残差或测试通过提升为统一解析 L² 上界。
- 不修改既有 Möbius 尾和、W1→W2 解析桥、Chebyshev 能量桥或 W2→W3 审计器接口。
- 不改动仓库中已经存在的未提交文件。

## 方案比较

### 方案 A：单一大合同

一次登记全部引理，工作量最小，但无法清楚区分每个量词、常数依赖和循环来源，
会退化为已有条件链登记的重复。

### 方案 B：分层账本、反循环测试与有限可证伪模型（采用）

将三个解析缺口分别注册，逐层检查输入和结论边界；有限层只验证可直接计算的
Möbius 尾和、互素筛选与 Euler--φ 重排残差。该方案不能制造解析证明，但能让
潜在反例、量词遗漏、常数依赖缺失与循环引用可被测试直接拒绝。

### 方案 C：纯数值扫描

只能发现有限尺度异常，不能描述证明依赖或禁止循环，故不采用。

## 架构

新增 `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`，提供：

1. **合同验证器**：验证三条义务、统一变量、常数依赖以及声明来源。
2. **依赖防火墙**：拒绝禁止的输入、目标结论循环字段和未声明的推导依赖。
3. **有限模型**：以模块内的精确有限 Möbius 与 Euler--φ 算术，在正整数截断上计算
   Möbius 尾和及互素限制尾和，并以 Euler--φ 加权平方和核验有限重排残差。模块不依赖
   当前工作树的未提交审计文件。
4. **证书写出器与 CLI**：输出 JSON、Markdown 和清晰的未证明状态。

配套新增 `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`，
覆盖合法合同、非法输入、量词/常数依赖缺失、循环升级、有限模型恒等式和证书边界。

新增的默认 Markdown/JSON 证书写入 `docs/monograph/`；如外部定理索引存在匹配的
W1→W2 缺口条目，仅新增到该条目的交叉引用，不改变其定理状态。

## 合同与状态

合同必须明确声明：

- `obligations`：
  `coprime_restricted_tail_bound`、`euler_phi_l2_aggregation`、
  `chebyshev_energy_transfer`；
- `uniformity_variable`：`truncation`；
- `constant_dependency`：`fixed_test_function`；
- `uses` 与每项 `claimed_uses`：只允许基础有限算术、Möbius 定义、互素关系和
  有限求和恒等式；
- 每条解析义务的状态：`open`。

禁止来源至少包括：`RH`、`Mertens`、`PNT`、`zeta_zero`、`zero_free_region`、
`explicit_formula`、`Mellin`、`Chebyshev_error`、`target_energy_bridge`、
`chebyshev_energy_bridge`、`finite_profile`、`numerical_experiment`。

禁止结论提升字段至少包括：`w1_to_w2_proved`、`w2_closed`、
`chebyshev_energy_bridge_proved`、`rh_proved`、`rh_consequence`。

无论有限模型读数如何，证书必须保持：

```text
w1_to_w2_status=unproved
coprime_restricted_tail_bound_status=open
euler_phi_l2_aggregation_status=open
chebyshev_energy_transfer_status=open
rh_proved=false
```

## 有限模型

有限模型接受正整数 `limit`。它计算每个候选模数的互素限制 Möbius 尾和，并以
Euler--φ 权重形成有限平方和；直接枚举和分解式之间的残差必须以精确 `Fraction`
核验为零。模型只报告：

- 输入尺度和候选索引范围；
- 直接有限能量、Euler--φ 分解能量与残差；
- `finite_model_status=verified_finite` 或失败状态。

模型不得报告任何 `L²--Upper`、渐近界、常数独立性或 Chebyshev 推论。

## 测试策略

1. 合法最小合同只产生三个 `open` 义务和 `unproved` 主链状态。
2. 对每个禁止来源、未声明依赖、错误统一变量、错误常数依赖和非内建布尔值均拒绝。
3. 对任何桥已证明、W2 闭合或 RH 提升字段均拒绝。
4. 小截断有限模型验证直接能量和 Euler--φ 分解的残差。
5. CLI/证书测试断言所有解析状态仍为 `open`，且 `rh_proved=false`。

## 使用示例

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test -v

python3 experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py \
  --limit 512
```

## 验收条件

- 所有新测试通过，且已有 W1→W2、Möbius 尾和与 LCM 相关测试不受影响。
- 禁止输入和结论循环都有负向测试。
- 有限重排残差被显式报告，但不改变任何解析义务为已证明。
- 默认 JSON/Markdown 证书清楚区分 `verified_finite` 与 `open`。
- 工作树中已有未提交文件未被本任务修改。
