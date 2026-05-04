# AlphaTail `C13` SparseSAE 的确定性 envelope 上界

**状态：** `c13_deterministic_envelope_bound_input_ready`

本文接续 SparseSAE 总量账本。目标是把 `sum Omega(E)` 从观测型账本改写为只依赖端点带宽、
窗口长度、步长 `u` 与残差 `epsilon` 的确定性上界。

## 1. 确定性槽数

对固定 group `(p,B,r,K,epsilon)`，其中 shape `K` 含步长 `u`。端点带条件为

\[
s=\epsilon+u h\le \beta |I_m|.
\tag{DEB-1}
\]

因此对所有允许 `m in M`，

\[
\Omega(E)
\le
1+
\left\lfloor
{\beta \max_{m\in M}|I_m|-\epsilon\over u}
\right\rfloor_+ .
\tag{DEB-2}
\]

这里 `floor_+` 表示若分子为负则该 group 槽数为 `0`。

**引理 DEB-1（确定性 envelope 上界）。**  
所有端点带 formal moving atoms 所属 group 的 envelope 总量满足

\[
\sum_E \Omega(E)
\le
\sum_E
\left(
1+
\left\lfloor
{\beta \max_{m\in M}|I_m|-\epsilon_E\over u_E}
\right\rfloor_+
\right).
\tag{DEB-3}
\]

**证明。**  
这是 `DBE-1` 对每个 group 的逐项应用。`h` 的允许范围只由 `(beta, |I_m|, u, epsilon)`
决定，与实际 witness 数无关。对 group 求和即得 `(DEB-3)`。□

结合 SparseSAE 总量付款：

\[
\sum_{E\in\mathcal E_{\rm sp}}\#\mathrm{atoms}(E)
\le
|M|\eta
\sum_E
\left(
1+
\left\lfloor
{\beta \max_m|I_m|-\epsilon_E\over u_E}
\right\rfloor_+
\right).
\tag{DEB-4}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_deterministic_envelope_bound.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_deterministic_envelope_bound.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --eta 0.04 \
  --slack-cut 40 --format table
```

输出摘要：

```text
observed_env=24029；
deterministic_env=24641；
slack=612；
deterministic_capacity=1971.28；
moving_over_capacity=0.113632。
```

按窗口拆分：

```text
p=997   : deterministic_env=3794；
p=5003  : deterministic_env=6472；
p=10007 : deterministic_env=14375。
```

因此当前压力样本中，即使用完全确定性的 envelope 上界替代观测 envelope，总付款容量仍为
`1971.28`，而实际 formal moving atoms 为 `224`。

## 3. 对主链的影响

SparseSAE 现在具有三层形式：

```text
逐组稀疏：S(E)<=eta Omega(E)
=> 总量付款：sum atoms<=|M| eta sum Omega(E)
=> 确定性上界：sum Omega(E)<=sum floor((beta max|I|-epsilon)/u)+1。
```

这减少了一个黑箱：后续全局证明不必依赖“观测 envelope 总量”，而只需证明目标反例族中
出现的 group 数与 `u` 分布满足确定性求和预算。
该 group 数与 `u` 分布的纯几何除数和上界见
`prime-matrix-eda-alpha-tail-tailpair-c13-group-u-distribution-bound.md`。

## 4. 审稿边界

已完成：

```text
确定性 envelope 槽数公式；
样本中 deterministic_env=24641 的复现账本；
SparseSAE 确定性付款容量 1971.28。
```

仍未完成：

```text
全局目标族中 group 数与 u 分布的上界；
确定性付款容量与主链最终预算的常数对接；
HighDensityEnvelope 的完整有限验证。
```

所以本文完成的是 `sum Omega(E)` 的确定性化，不是行命题最终闭合。
