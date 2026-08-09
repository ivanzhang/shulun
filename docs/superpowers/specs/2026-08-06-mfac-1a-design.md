# MFAC-1A：粗辅因子 Möbius 带符号传输（推前前）设计

## 1. 目标与边界

本设计只处理 MFAC 的第一原子，不宣称短区间素数定理、平方根误差、零点排除或 RH。

目标是在任何 `Phi`、payment、zero-row、PDEC、Rankin 或终端反例恢复之前，把全局
Möbius--von Mangoldt 质量非循环地写入项目的 LPF/Phi primitive formal units。

固定一个非负、紧支撑的平滑权重 `W` 及尺度 `X`。基础精确恒等式为

```text
sum_n Lambda(n) W(n/X)
  = - sum_{d,m >= 1} mu(d) log(d) W(dm/X).
```

这里的目标不是以 LPF 局部无符号计数取代右侧，而是为每个 source pair `(d,m)` 给出可
追溯、不可重复的带符号来源与传输记录。

## 2. MFAC-1A 的候选定理

```text
RoughCofactorMobiusSignedTransportBeforePushforward
```

设 `q` 是 source pair 的一个粗辅因子步骤，且 `d = q*d0` 或 `m = q*m0`，具体分支由
预先声明的 factor-orientation 规则决定。需构造一个 pre-pushforward transport record：

```text
T = (source_key, orientation, q, predecessor_key, target_unit,
     signed_coefficient, local_factor, branch_tag, return_tag).
```

它必须满足：

1. `source_key` 唯一表示一个原始 `(d,m)`，并保留 `-mu(d) log(d)` 的来源；
2. `orientation` 在乘入/剥离 `q` 前确定，不能由下游零行或支付结果反推；
3. `signed_coefficient` 与 `local_factor` 的乘积逐项恢复该 source 的 Möbius 权重；
4. 每个 source 恰进入一个 primitive unit 或一个显式 remainder；
5. remainder 只可属于 `boundary`、`prime-power`、`balanced-Type-II` 三类，且三类互不相交；
6. 对全部 records 求和时，精确恢复原 Möbius--von Mangoldt 和；
7. 构造不得调用 Phi/payment、zero-row、PDEC、Rankin、终端矛盾或它们的反向恢复。

## 3. 证明义务分层

### 3.1 源域与唯一键

定义 source domain `S_X={(d,m): W(dm/X) != 0}`。必须先指定 source key 的全部字段，至少
包括 `d,m`、squarefree 状态、粗辅因子选择、方向及所属尺度块。

验收：source key 到 `(d,m)` 为单射；任何两个 record 不得代表同一 Möbius 项。

### 3.2 粗辅因子传输

传输只能使用 source key 中已有的算术数据。若 `d=q*d0`，则符号更新必须显式记录：

```text
mu(d) = -mu(d0)  (q 不整除 d0 且 d0 squarefree),
mu(d) = 0        (q 整除 d0 或 d 非 squarefree).
```

`log(d)` 的加法分解 `log(d0)+log(q)` 也必须进入 record；不能只传播 Möbius 符号而忽略
von Mangoldt 权重。

验收：逐 record 的系数恒等式可由整数分解直接复算。

### 3.3 LPF/Phi primitive unit 适配

目标 unit 只能接收其预先声明的 source records。若 LPF 信息不足以决定唯一 target，必须将
该项送入 `balanced-Type-II` remainder，而不是任意选择 bucket。

验收：不存在“同一 source 在两个 unit 计入”或“由下游结论指定 target”的路径。

### 3.4 全局守恒与无循环防火墙

定义 unit 总和 `A(U)` 和三类 remainder 总和 `R_boundary`、`R_pp`、`R_II`。要求恒等式：

```text
sum_U A(U) + R_boundary + R_pp + R_II
  = - sum_(d,m in S_X) mu(d) log(d) W(dm/X).
```

验收：依赖图从左至右仅为 `source -> record -> unit/remainder -> sum identity`；禁止
`unit/payment/zero-row -> source coefficient` 的回边。

## 4. 核心矛盾与失败证书

本设计预先允许两种结果：

1. **构造成功：** 产生完整 noncircular transport law，作为 MFAC-2 的合法 signed family 输入；
2. **构造不可能：** 找到两个 source pairs 在所有允许的 LPF-local 状态下不可区分，却需要不同的
   Möbius 或 logarithmic 系数 / target。此时得到 `LPF-local state insufficient` 反例证书，迫使
   source state 扩展为完整 divisor-history 或等价 trace state。

第二种结果不是失败，而是排除“只靠 LPF 局部状态即可承载 Lambda”的伪路线。

## 5. 三阶段执行顺序

1. **审计：** 读取现有 signed transport、source-key、rough-cofactor、von Mangoldt lift 工件，提取
   已定义字段、依赖图和所有下游回边。
2. **有限一致性：** 对有限 `X` 枚举 source pairs，测试候选 local state 是否区分必需的符号、对数
   权重和 target；输出构造表或最小碰撞证书。
3. **一般构造：** 只有有限审计支持可行时，写出一般 source-key 和 exact transport identity；否则将
   最小碰撞提升为正式 no-go 引理。

## 6. 非目标

- 不从 MFAC-1A 直接推出 `psi(x)=x+O(X^(1/2+epsilon))`；
- 不将有限计算当作一般定理；
- 不引用尚未构成 admissible signed family 的外部 Type-II 结果；
- 不把既有无符号 LPF/Phi ownership 误写为 Möbius--von Mangoldt signed transport。

## 7. 进入 MFAC-2 的门槛

只有同时满足下列条件，才允许进入平方根级平滑误差桥：

```text
exact_global_conservation = true
source_uniqueness = true
no_downstream_recovery = true
remainder_partition_disjoint = true
balanced_type_ii_remainder_explicit = true
```

届时 MFAC-2 才能研究 `balanced-Type-II` remainder 的相位抵消，并尝试得到平方根级界。
