# MFAC W1→W2 最小无条件 Chebyshev 能量桥合同设计

**日期：** 2026-08-13

**状态：** 已确认设计，待用户审阅书面规格

## 1. 目的

本阶段只定义并审计 W1 到 W2 所需的最小、无条件、非循环桥接合同。它不计算
\(\psi\)，不估计 Chebyshev 误差，不证明任何桥接不等式，也不把现有 Gram、LCM 或
Möbius 尾和有限能量认定为实际 Chebyshev 能量桥。

目标对象固定为 dyadic 原尺度二次能量

\[
\mathcal E(X)=\int_X^{2X}|\psi(t)-t|^2\,dt.
\]

本阶段的唯一作用是使未来声称 W2 时必须提供可审查的实际 Gram 能量、全称量词、
独立误差控制与无循环输入来源。

## 2. 预注册的桥接命题

候选必须预注册一个抽象实际 Gram 能量 \(\mathcal G(X)\ge0\)，并声明如下量词：

\[
\exists A>0,\ \exists X_0\ge1,\ \forall X\ge X_0:\quad
\mathcal E(X)\le A\,\mathcal G(X)+B(X).
\]

其中 \(A\) 是绝对常数：不得依赖 \(X\)、系数族、Gram 核、截断、候选构造或
任何待控误差。\(X_0\) 是固定阈值；有限扫描、预注册 dyadic 子列或依赖 \(X\) 的
常数均不能满足本合同。

这是一条待证明的全称不等式。合同审计器只验证其描述是否完整，绝不输出
`proved`、`bridge_established`、`w2_closed` 或等价状态。

## 3. Gram 能量注册合同

每个候选的 `gram_contract` 必须是 Mapping，并完整声明：

```text
coefficient_family: 非空字符串
kernel: 非空字符串
interval_correspondence: 非空字符串
constant_projection: 非空字符串
nonnegative: true
uses: 非裸字符串的字符串序列
```

字段分别表示：系数族、Gram 核、与连续尺度 \(X\) 的实际对应、去常数投影以及
非负性声明。它们是接口声明，不是数学证明。任一字段缺失、为空、类型错误、
`nonnegative` 不为内建 `True`，或 `uses` 是裸字符串/含非字符串元素时必须拒绝。

本合同不允许将 `actual_lcm_gram_energy`、`mobius_tail_l2` 或其他现有模块自动
视为候选；未来候选必须显式提供上述五项语义字段与独立证明。

## 4. 误差项义务

\(B(X)\) 是独立义务，不能默认取零、非正或可忽略。候选必须预注册
`error_contract`：

```text
source: 非空字符串
eta: 有限内建实数，且 0 <= eta < 1
absorption_target: "B(X)<=eta*G(X)"
uses: 非裸字符串的字符串序列
```

其目标是未来独立证明

\[
0\le B(X)\le\eta\,\mathcal G(X),\qquad 0\le\eta<1.
\]

`eta` 不能由 \(\psi(X)-X\)、`Chebyshev_error`、Mellin、零点、RH 或后继结论
反向选取。即使合同字段合法，误差状态也固定为 `absorption_obligation_open`。

## 5. 禁止输入与非循环性

`bridge_contract.uses`、`gram_contract.uses` 和 `error_contract.uses` 的并集一律
拒绝下列任一项：

```text
Chebyshev_error
psi(X)-X
target_energy
Mellin
zero_free_region
zeta_zero
explicit_formula
RH
PNT
Mertens_cancellation
```

这些项目分别会把待控 Chebyshev 对象、后继 Mellin/零点结论、RH 或外部素数分布
输入回灌到 W1→W2。发现任何一个即拒绝合同，而不是降级为条件性桥接。

此外，`claimed_bound_uses` 若出现，必须是三个 `uses` 的子集；未声明来源必须拒绝。
合同不得含 `w2_actual_chebyshev_energy_bridge`、`w2_closed`、`rh_proved`、
`target_energy_bound` 等目标结论循环字段。

## 6. 审计结果与证书

审计器的有效输出固定包括：

```text
bridge_structure_status=registered_unproved_contract
absolute_constant_status=registered_unproved
large_scale_quantifier_status=registered_unproved
gram_nonnegativity_status=declared_not_proved
error_absorption_status=absorption_obligation_open
w2_actual_chebyshev_energy_bridge_status=unproved
rh_proved=false
```

默认 CLI 写出 JSON 和 Markdown 证书。证书必须逐项列出：桥接量词、Gram 注册字段、
误差来源与 \(\eta\)、禁止输入检查、未声明来源检查和明确的非证明结论。它必须写明：
本合同不证明 \(\mathcal E(X)\) 的界、不证明 \(\mathcal G(X)\) 的实际构造或非负性、
不证明误差吸收、不证明 W2、Mellin、零自由区或 RH。

## 7. 测试与验收

单元测试至少覆盖：

1. 合法最小合同注册后仍为 `registered_unproved_contract` 与 `rh_proved=false`；
2. 缺失/空的 Gram 语义字段、非布尔 `nonnegative`、裸字符串/非字符串 `uses` 被拒绝；
3. 非有限、布尔、负值或不小于 1 的 `eta` 被拒绝；
4. 禁止输入在三个合同任一 `uses` 中出现均被拒绝；
5. 未声明 `claimed_bound_uses` 和目标结论循环字段被拒绝；
6. JSON/Markdown 与脚本路径 CLI 始终保持 W2 未证明和 RH 未证明；
7. 全量 MFAC 回归测试通过。

阶段实现完成后，只暂存本规格、本计划、新桥接审计器、新测试与两种证书；运行
`git diff --check` 和全量 MFAC 测试后创建独立提交。不得混入既有未提交文件。

## 8. 非目标

- 不计算 \(\psi\)、\(\mathcal E(X)\)、\(\mathcal G(X)\) 或 \(B(X)\)；
- 不选择、比较或认证具体 Gram 系数族/核；
- 不允许 PNT、Mertens、显式公式、Mellin、零点信息或 RH 作为条件输入；
- 不从 W1 的有限诊断、库存状态或图谱角色推断 W2；
- 不修改 W0--W5 主链图谱、不生成 W3 及后续义务的实现；
- 不输出 RH、W2 或桥接不等式已证明的任何形式。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py \
  --json-out /tmp/mfac-w1-w2-bridge.json \
  --markdown-out /tmp/mfac-w1-w2-bridge.md
```

该命令只能登记一个无条件桥接合同，不会执行候选模块、计算 \(\psi\) 或证明 RH。
