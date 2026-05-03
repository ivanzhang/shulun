# WSH-Hall 固定偏移/PDEC 吸收引理

**状态：** `proved_no_third_escape_and_pdec_absorption_target`

本文把 `SCB-1` 长块中出现的 `Fixed-offset-full-load` 从经验标签升级为一个可逐行审查的
吸收接口。已经证明的是“满载固定偏移没有第三逃逸”；尚未证明的是最终
`Endpoint/PDEC exclusion`。

## 1. 基本设置

固定相邻素数 `p<q`。取轮筛小素数集合

```text
W={2,3,5,7,11,13}
```

以及半径 `R=ceil(3 log^2 q)`。令 `B` 是同一 `q` 宽行中的连续平衡双尾半素数长块。
对非零偏移 `d` 定义固定偏移纤维

\[
  F_d(B)=\{b+d:b\in B,\ |d|\le R\}.
\]

称 `d` 对 `B` **轮筛满载**，如果对所有 `b in B` 和所有 `r in W` 都有

\[
  b+d\not\equiv0\pmod r。
\]

这正是证书中的 `Fixed-offset-full-load`。

## 2. 无第三逃逸引理

**引理 FO-1.**
设 `n` 是满足 `1<n<q^2` 的整数。若 `n` 不是素数，则 `n` 有一个不超过 `p` 的素因子。

**证明。**
若 `n` 合成而所有素因子均大于 `p`，由于 `q` 是大于 `p` 的下一素数，每个素因子都至少为
`q`。于是 `n` 至少是两个不小于 `q` 的素因子的乘积，故 `n>=q^2`，与 `n<q^2`
矛盾。证毕。

**推论 FO-2.**
若 `d` 对 `B` 轮筛满载，且 `b+d` 不是素数，则 `b+d` 有素因子

\[
  \ell\in (13,p]。
\]

**证明。**
由 FO-1，`b+d` 有某个 `ell<=p` 的素因子。轮筛满载排除了 `ell in W`。
因此 `ell in (13,p]`。证毕。

## 3. 吸收二分

对每个缺失候选 `n=b+d`，取一个解释因子

\[
  a(n)=\min\{\ell\in(13,p]:\ell\mid n\}.
\]

由 FO-2，该映射对所有缺失候选都有定义。于是固定偏移满载纤维满足二分：

```text
要么 F_d(B) 中已有足够素数，给出长块扩张；
要么缺失候选全部被 a(n) in (13,p] 解释。
```

第二种情形再分为：

1. 某个解释因子在同一局部块中重复出现，进入 `Tail-anchor / Tail-repeat`；
2. 解释因子没有局部重复，但在低模残基上持续偏斜，进入 `PDEC / low-mod CRTDefect`；
3. 偏斜不持久，只能作为稀疏端点逃逸进入 `SAE / Endpoint`。

这给出当前可用的正式路由：

```text
Fixed-offset-full-load
=> expansion
   or Tail-anchor
   or PDEC / low-mod CRTDefect
   or SAE / Endpoint.
```

## 4. 有限吸收账本

新增脚本：

```text
experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.md
docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.json
```

该账本读取 `SCB-1` 长块证书中的 `4` 个最紧长块，检查全部满载固定偏移。结果：

```text
full offset rows = 11
total candidates on full offsets = 47
prime candidates = 15
missing candidates = 32
missing without factor <=p = 0
max factor load in one offset row = 1
```

解释：

1. `missing_without_factor<=p=0` 是 FO-1/FO-2 的有限核验；
2. 单个偏移行最大解释因子负载为 `1`，说明这些最紧长块不是局部尾锚重复型，而是分散低模
   解释型；
3. 因此下一步必须攻 `PDEC / SAE / Endpoint`，而不是继续在同一长块内寻找局部重复因子。

## 5. 全局闭合仍需的唯一输入

要把本接口升级为全局无条件闭合，还必须证明以下命题。

**命题 FO-PDEC.**
对所有充分大相邻素数 `p<q`、所有 `SCB-1` 长块 `B` 和所有满载固定偏移 `d`，若
`F_d(B)` 中素数不足以给出 Hall 扩张，且没有 Tail-anchor，则由解释因子映射 `a(n)`
产生的低模残基偏斜必触发 `PDEC / low-mod CRTDefect`；若该偏斜不持久，则触发
`SAE / Endpoint`。

当前本文没有证明 `FO-PDEC` 的全局不等式。本文完成的是：

```text
Fixed-offset-full-load 不再是未命名逃逸；
它已被严格路由到 expansion / Tail-anchor / PDEC / SAE / Endpoint。
```

因此 `WSH-Hall/PDEC` 的下一真实硬点已经从长块内部结构转为最终出口排斥：

```text
Endpoint/PDEC exclusion
plus SAE local escape exclusion.
```
