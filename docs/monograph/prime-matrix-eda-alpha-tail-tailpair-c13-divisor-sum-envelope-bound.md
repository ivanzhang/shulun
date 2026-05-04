# AlphaTail `C13` 几何 envelope 的除数和闭式上界

**状态：** `c13_divisor_sum_envelope_bound_input_ready`

本文接续 `group/u` 分布确定性上界。目标是把

\[
\sum_{E\in\mathcal G_{\rm geo}}\Omega(E)
\]

压成可在全局窗口族上求和的闭式除数函数表达。

## 1. 闭式上界

记 `R=|r|`，`L=max_{m in M}|I_m|`。对每个点位差 `Delta` 与除数 `u|Delta R`，
几何关系为

\[
\Delta R=gu.
\tag{DSE-1}
\]

若保留偶 gap 条件，则记录级 envelope 上界为

\[
\mathcal D_{\rm even}(B,r)
=
\sum_{m\in M}\sum_{\Delta=1}^{m-1}
(m-\Delta)
\sum_{\substack{u\mid \Delta R\\ \Delta R/u\ {\rm even}}}
\left(1+\left\lfloor{\beta L\over u}\right\rfloor\right).
\tag{DSE-2}
\]

若进一步去掉偶性和取整，得到更粗但更闭式的

\[
\mathcal D_{\tau\sigma}(B,r)
=
\sum_{m\in M}\sum_{\Delta=1}^{m-1}
(m-\Delta)
\left(
\tau(\Delta R)+\beta L\,\sigma_{-1}(\Delta R)
\right),
\tag{DSE-3}
\]

其中

\[
\sigma_{-1}(n)=\sum_{d\mid n}{1\over d}.
\tag{DSE-4}
\]

**引理 DSE-1（除数和 envelope 上界）。**  
对任意目标窗口，

\[
\sum_{E\in\mathcal G_{\rm fail}}\Omega(E)
\le
\sum_{E\in\mathcal G_{\rm geo}}\Omega(E)
\le
\mathcal D_{\rm even}(B,r)
\le
\mathcal D_{\tau\sigma}(B,r).
\tag{DSE-5}
\]

**证明。**  
第一步是 `C13Failure subset GeometricCandidate`。第二步中每个几何记录由唯一三元组
`(m,Delta,u)` 支配，去重只会降低 group 数，因此记录级和支配去重 group 和。第三步去掉偶
gap 限制，并用 `floor(x)<=x`，得到 `(DSE-3)`。□

结合 SparseSAE 付款，得到完全闭式的充分条件：

\[
|M|\eta\sum_{(B,r)}\mathcal D_{\tau\sigma}(B,r)
\le
\mathrm{Budget}_{\rm C13}.
\tag{DSE-6}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --eta 0.04 --format table
```

输出摘要：

```text
geometric_dedup_env = 68241；
exact_even_bound    = 108342；
tau_sigma_bound     = 122294.169；
capacity_dedup      = 5459.28；
capacity_exact      = 8667.36；
capacity_tau_sigma  = 9783.53352。
```

窗口级比较：

```text
p=997   : dedup= 9387, exact_even=14890, tau_sigma=16848.825；
p=5003  : dedup=18999, exact_even=30111, tau_sigma=33975.225；
p=10007 : dedup=39855, exact_even=63341, tau_sigma=71470.119。
```

闭式 `tau/sigma` 外壳约为去重几何 envelope 的 `1.792` 倍；这是可接受的审稿损耗，因为它
完全摆脱了实际 witness 和 group 去重细节。

## 3. 对主链的影响

C13 SparseSAE 的全局付款接口现在变为：

```text
实际 failure atoms
<= |M| eta * sum Omega(failure groups)
<= |M| eta * sum D_even(B,r)
<= |M| eta * sum D_tau_sigma(B,r)。
```

因此下一步真正剩余是单一常数接口：

```text
C13-DivisorBudget:
  在目标窗口族上证明
  |M| eta sum D_tau_sigma(B,r)
  小于 C13 主链允许预算。
```

这比前一版更严格：不再需要观测 group 数、实际 positive/narrow/failure 记录数，也不需要
实际尾素对分布。

## 4. 审稿边界

已完成：

```text
D_even 与 D_tau_sigma 闭式除数和上界；
样本中闭式外壳与去重外壳的常数比较；
SparseSAE 付款完全写成 tau/sigma 除数函数接口。
```

仍未完成：

```text
目标窗口族上 sum D_tau_sigma 的全局求和；
C13 主链 Budget_C13 的正式数值接口；
HighDensityEnvelope 有限验证清单的全覆盖。
```

所以本文完成的是 C13 几何 envelope 的闭式求和化，不是行命题最终闭合。
