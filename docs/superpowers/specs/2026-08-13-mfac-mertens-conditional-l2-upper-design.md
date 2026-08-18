# MFAC 全 ε Mertens 条件化 L²--Upper 审计设计

**日期：** 2026-08-13

**状态：** 已确认设计，待用户审阅书面规格

## 1. 目的

本规格为既有 Möbius 尾和整体 L² 有限审计补充一个**条件化证明义务审计器**。它不证明 Mertens 型消去、不证明零点结论、更不证明 RH；它只精确登记下列蕴含链是否在量词、常数依赖与禁止输入方面自洽：

\[
\forall\varepsilon>0,\quad
\bigl(\exists C_\varepsilon>0\ \forall x\ge1:\ |M(x)|\le
C_\varepsilon x^{1/2+\varepsilon}\bigr)
\Longrightarrow \operatorname{L2Upper}(\varepsilon).
\]

其中 \(M(x)=\sum_{n\le x}\mu(n)\)。审计对象仅是固定的线性截断 Möbius--log 系数族及其 Euler--\(\varphi\) 平方和分解；它不对任意 MFAC 系数族、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH 作结论。

## 2. 前置的已验证有限层

复用 `prime_matrix_mfac_mobius_tail_l2_audit.py` 中已经单独验证的有限事实：

\[
E_D=\sum_{2\le r<D}\varphi(r)|T_D(r)|^2,
\]

以及固定系数

\[
a_D(d)=-\mu(d)\log d\left(1-\frac{\log d}{\log D}\right),
\qquad 2\le d<D.
\]

这些有限恒等式不使用 Mertens、PNT、零点、显式公式、Mellin 或 RH。新模块不得改变现有有限审计器的接口，也不得把有限截断数值读数写成全局上界证明。

## 3. 条件命题与量词

### 3.1 外部条件：全 ε Mertens 型界

合同必须表示为下列全称模式，而不是一个未经绑定的字符串：

```text
for_every_epsilon: true
epsilon_domain: "positive_real"
assumption: "M(x)=O_epsilon(x^(1/2+epsilon))"
constant_dependency: "C_epsilon_depends_on_epsilon_only"
uniform_in_epsilon: false
```

其语义是：对每个实数 \(\varepsilon>0\)，允许存在仅依赖于该 \(\varepsilon\) 的有限正常数 \(C_\varepsilon\)，使界对所有 \(x\ge1\) 成立。不得将 \(C_\varepsilon\) 伪装为对 \(\varepsilon\) 一致，也不得由有限样本、`M(x)` 计算或数值拟合来“验证”该假设。

### 3.2 目标：条件化 L²--Upper

输出的目标为带参数的**条件性状态**：对每个 \(\varepsilon>0\)，若第 3.1 节假设成立，则产生一个仅允许依赖于 \(\varepsilon\) 与 \(C_\varepsilon\) 的上界常数记录。审计器必须将其表述为

```text
conditional_l2_upper_status=assumption_chain_registered
unconditional_l2_upper_status=unproved
mertens_assumption_status=externally_assumed
rh_proved=false
```

该状态表示“条件链被准确登记”，不表示分析不等式已经由程序证明，也不表示 Mertens 假设已被项目证明。

## 4. 可审计依赖链

审计器把下列节点分开登记，避免跳过从部分和到整体平方和的实际分析步骤：

1. `MertensAllEpsilonHypothesis`：第 3.1 节的唯一外部解析输入；
2. `CoprimeRestrictedPartialSummation`：从 \(M(x)\) 到带 \((m,r)=1\) 限制的 Möbius 对数权尾和所需的分部求和/容斥步骤；
3. `TailBoundWithParameterDependence`：对每个固定 \(\varepsilon\) 明确记录指数损失以及常数可依赖于 \(\varepsilon,C_\varepsilon\)；
4. `EulerPhiL2Aggregation`：将逐尾和或双线性估计汇总到 \(\sum_r\varphi(r)|T_D(r)|^2\) 的独立步骤；
5. `ConditionalL2UpperConclusion`：仅当 1--4 全部声明时，才输出条件链已登记。

节点 2--4 初始均为 `proof_obligation_open`，除非未来提供可逐步核查的解析引理与适用范围。审计器不得把“有 Mertens 假设”自动升级为实际 `proved` 的 L²--Upper；它只验证依赖声明的完整性和非循环性。

## 5. 合同与输入验证

新模块接受一个 `Mapping` 形式的条件合同，并执行以下防御性验证：

- `uses` 必须是非裸字符串的字符串 iterable；
- `epsilon` 必须是有限、非布尔、严格正的内建 `int` 或 `float`，仅用于单个实例化诊断；全 ε 命题仍由显式量词字段表示；
- 若提供 `mertens_constant`，它必须是有限、严格正的内建数值，且标签必须说明它只对应当前 `epsilon`；
- 禁止 `RH`、`zeta_zero`、`zero_free_region`、`explicit_formula`、`Mellin`、`target_l2_upper`、`unconditional_l2_upper` 作为未声明来源或结论循环输入；
- 任何 `claimed_bound_uses` 都必须包含于已声明 `uses`；
- 缺少 `Mertens_cancellation`、缺少全 ε 量词、或错误声称 ε 一致常数时必须拒绝，而非静默降级。

允许 `finite_divisor_identity`、`euler_phi_identity`、`partial_summation`、`coprimality_inclusion_exclusion` 与 `Mertens_cancellation` 等命名依赖，但它们必须被分类为有限事实、外部假设或开放证明义务。

## 6. 证书与数学说明

### 6.1 JSON/Markdown 条件证书

默认 CLI 产物应包含：

- 全 ε Mertens 假设的精确量词和常数依赖；
- 当前单个 \(\varepsilon\) 的有限合法性检查（不是假设的数值验证）；
- 每个依赖节点的状态、禁止输入检查结果和未闭合节点；
- `conditional_l2_upper_status`、`unconditional_l2_upper_status`、`mertens_assumption_status`、`rh_proved`；
- 明确的 `not_a_proof_of` 列表，至少含 Mertens 假设、无条件 L²--Upper、Mass--Lower、Chebyshev 能量桥、Mellin 收缩、零自由区域与 RH。

### 6.2 数学说明文档

说明文档独立写出：

1. 全 ε 假设的量词顺序；
2. `C_epsilon` 可依赖于 \(\varepsilon\)，但不得依赖于截断 \(D\)；
3. 从 \(M(x)\) 到互素限制、对数权尾和的额外引理义务；
4. 从尾和估计到 Euler--\(\varphi\) 加权 L² 聚合的额外引理义务；
5. 为什么条件链登记不等于证明这些引理，更不等于证明 RH。

文档不得引用未提供的外部定理来填补节点 2--4；若未来加入外部定理，必须列出定理名、精确陈述、常数依赖、适用区间与来源。

## 7. 测试与验收

测试至少覆盖：

- 合法的全 ε Mertens 合同被分类为 `externally_assumed`，且不产生无条件结论；
- 非正、布尔、非有限或非内建 `epsilon`/常数被拒绝；
- 裸字符串 `uses`、非字符串元素、非 `Mapping` 合同被拒绝；
- 缺失全 ε 量词、错误 ε 一致性声明、未声明的 `claimed_bound_uses` 被拒绝；
- RH/零点/目标结论循环依赖被拒绝或标记为循环；
- JSON/Markdown 证书始终包含 `unconditional_l2_upper_status=unproved` 与 `rh_proved=false`；
- CLI 可从脚本路径运行并写出两种产物；
- 既有 Möbius 尾和 L² 审计测试与全量 MFAC 测试保持通过。

## 8. 非目标与停止条件

- 不实现或声称 `M(x)=O_\varepsilon(x^{1/2+\varepsilon})` 的证明；
- 不以有限 \(D\) 或有限 \(x\) 扫描替代全称量词；
- 不把未展开的 `partial_summation` 名称当作已完成的解析引理；
- 不合并 `Mass--Lower`，它仍是独立的未闭合义务；
- 若节点 2--4 没有逐步证明，条件结论只能是 `assumption_chain_registered`，而不是 `proved_under_mertens`；
- 无论任何有限检查是否通过，`rh_proved=false` 保持不变。

## 使用示例

计划中的 CLI 形式如下：

```bash
python3 experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py \
  --epsilon 0.1 \
  --json-out /tmp/mfac-mertens-conditional-l2-upper.json \
  --markdown-out /tmp/mfac-mertens-conditional-l2-upper.md
```

该命令只能生成条件链审计证书；它不会计算或验证 Mertens 假设，也不会输出无条件 L²--Upper 或 RH 证明。
