# AlphaTail `C13` SparseSAE 总 envelope 可求和账本

**状态：** `c13_sparse_summability_input_ready`

本文接续 `Band Sparse Acceptance`。目标是把逐组稀疏条件
`S(E)<=eta Omega(E)` 汇总成一个可审稿的总量付款不等式。

## 1. 总量引理

设 `\mathcal E_sp` 为所有进入 `SparseSAE` 的 envelope group。每个 group 有 observed slots
`S(E)` 与 envelope slots `Omega(E)`。若每个深度槽最多来自 `L=|M|` 个 `m` 层，则

\[
\sum_{E\in\mathcal E_{\rm sp}} \#\mathrm{atoms}(E)
\le
L\sum_E S(E)
\le
L\eta\sum_E \Omega(E).
\tag{SSL-1}
\]

**引理 SSL-1（SparseSAE 总量付款）。**  
只要

\[
L\eta\sum_{E\in\mathcal E_{\rm sp}}\Omega(E)
\tag{SSL-2}
\]

低于主链给 SparseSAE 分支的可支付预算，则全部 SparseSAE group 可同时吸收；无需逐个
group 再进入 ColumnCRT 或高密度分支。

**证明。**  
对每个 `SparseSAE` group，`S(E)<=eta Omega(E)`。同一深度槽在 `m` 层投影中最多贡献 `L`
个 formal atoms，故 `atoms(E)<=L S(E)`。对所有 group 求和即得 `(SSL-1)`。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_sparse_summability.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_sparse_summability.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --eta 0.04 \
  --slack-cut 40 --format table
```

输出摘要：

```text
moving=224；
groups=38；
accepted=38；
high=0；
accepted_slots=215；
accepted_env=24029；
accepted_capacity=1922.32；
slot_density=0.008948；
moving_over_capacity=0.116526。
```

按窗口拆分：

```text
p=997   : accepted_env=3779,  capacity=302.32；
p=5003  : accepted_env=6460,  capacity=516.80；
p=10007 : accepted_env=13790, capacity=1103.20。
```

这说明当前压力样本中，`eta=1/25` 给出的总 envelope 付款远大于实际 moving atoms；
SparseSAE 总量在样本层面已可同时吸收。

进一步的确定性 envelope 上界见
`prime-matrix-eda-alpha-tail-tailpair-c13-deterministic-envelope-bound.md`：把
`sum Omega(E)` 改写为
`sum (1+floor((beta max_m |I_m|-epsilon_E)/u_E))`，当前样本给出
`deterministic_env=24641` 与 `deterministic_capacity=1971.28`。

## 3. 对主链的影响

`C13` 的 moving 分支现在变成：

```text
Moving atoms
=> BandEnvelope
=> SparseSAE total payment
   or HighDensityEnvelope finite/ColumnCRT exit.
```

其中 `HighDensityEnvelope` 已进一步接入：

```text
Layer interval reduction
=> density ceiling
=> low q finite threshold / overlap certificate。
```

因此当前 C13 压力链条的剩余不是逐组 SparseSAE，而是全局证明：

```text
sum Omega(E) 的确定性上界；
该上界乘 L*eta 小于主链预算；
HighDensityEnvelope 的低阈值有限验证覆盖完整目标族。
```

## 4. 审稿边界

已完成：

```text
SparseSAE 总量付款不等式；
样本中 accepted_capacity=1922.32 与 moving=224 的付款账本；
按窗口拆分的 envelope 容量审计。
```

仍未完成：

```text
全局目标族的 sum Omega(E) 确定性上界；
SparseSAE 付款与主链最终预算的常数对接；
完整目标族 HighDensityEnvelope 的有限验证或排斥。
```

所以本文完成的是 SparseSAE 的总量账本接口，不是行命题最终闭合。
