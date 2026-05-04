# EDA-Dual-K：Bonferroni 对偶下界与高重合尾项

**状态：** `eda_dual_low_order_positive_in_samples_variable_order_needed`

本文继续直接攻击 `EDA-Dual`。本步把早期对角避让转成一个完全初等、只含整除计数的
Bonferroni 下界问题，并给出首轮实验事实。

## 1. 精确对象

固定奇素数 `p` 与 `1<=x<=p`。令

\[
I_{p,x}=\{px+1,\ldots,px+p-1\}.
\tag{EDB-1}
\]

对 `n in I_{p,x}`，记

\[
\omega_p(n)=\#\{q<p:\ q\ {\rm prime},\ q\mid n\}.
\tag{EDB-2}
\]

则早期幸存数为

\[
U_p(x)=\#\{n\in I_{p,x}:\omega_p(n)=0\}.
\tag{EDB-3}
\]

上一文件已证明在早期区段中 `\omega_p(n)=0` 等价于 `n` 为大于 `p` 的素数。

## 2. 奇数阶 Bonferroni 下界

对奇数 `K`，定义

\[
S_K(p,x)=
\sum_{n\in I_{p,x}}
\sum_{j=0}^{\min(K,\omega_p(n))}
(-1)^j{\omega_p(n)\choose j}.
\tag{EDB-4}
\]

逐点 Bonferroni 恒等式给出：

\[
S_K(p,x)\le U_p(x)\qquad(K\ {\rm odd}).
\tag{EDB-5}
\]

因此只要证明

\[
\min_{1\le x\le p}S_K(p,x)>0,
\tag{EDB-6}
\]

就能证明 `EDA(p)`。

同时 `(EDB-4)` 可改写为纯 CRT 整除计数：

\[
S_K(p,x)=
\sum_{j=0}^K(-1)^j
\sum_{\substack{d\mid M_p\\ \omega(d)=j}}
\#\{n\in I_{p,x}:d\mid n\}.
\tag{EDB-7}
\]

这正是 `EDA-Dual-K` 的无黑箱形式。

## 3. 五阶的结构含义

当 `K=5` 时，逐点权重为

\[
w_5(t)=\sum_{j=0}^{\min(5,t)}(-1)^j{t\choose j}.
\tag{EDB-8}
\]

于是

\[
w_5(0)=1,\qquad
w_5(t)=0\quad(1\le t\le5),
\tag{EDB-9}
\]

且对 `t>=6`，

\[
w_5(t)=-{t-1\choose5}.
\tag{EDB-10}
\]

所以

\[
S_5(p,x)=
U_p(x)
-
\sum_{\substack{n\in I_{p,x}\\ \omega_p(n)\ge6}}
{\omega_p(n)-1\choose5}.
\tag{EDB-11}
\]

这条身份解释了五阶为何有效：它不再被一到五重小素因子污染，只剩真实素数余量减去
`>=6` 重小素因子的高重合惩罚。

因此五阶路线的真正硬点是：

```text
EDA-Core6:
the sixth-and-higher small-prime overlap penalty cannot exceed the prime survivor margin.
```

若直接用 `(EDB-7)` 证明 `S_5>0`，则不需要先知道素数在哪里；但 `(EDB-11)` 给出其结构意义。

## 4. 实验审计

脚本：

```text
experiments/prime_matrix_eda_bonferroni_audit.py
```

选点输出：

| p | min U_p(x) | min S_1 | min S_3 | min S_5 | min S_7 |
|---:|---:|---:|---:|---:|---:|
| 23 | 2 | -11 | 1 | 2 | 2 |
| 101 | 7 | -85 | -8 | 7 | 7 |
| 199 | 12 | -195 | -26 | 12 | 12 |
| 499 | 29 | -557 | -124 | 28 | 29 |
| 997 | 54 | -1209 | -322 | 51 | 54 |
| 1999 | 110 | -2605 | -836 | 94 | 110 |
| 5003 | 260 | -7067 | -2720 | 177 | 260 |

结论：

1. 一阶和三阶不足，余量明显为负；
2. 五阶在这些样本中全部为正；
3. 七阶以后通常恢复到精确幸存数，因为样本行内 `\omega_p(n)` 很少超过 `7`；
4. 五阶的正性不是平凡事实，它正好在控制 `>=6` 重合尾项。

## 5. 固定阶风险

固定五阶不应直接宣称全局闭合。随机筛模型中，`\omega_p(n)` 的均值约为

\[
\mu\sim\sum_{q<p}{1\over q}\sim\log\log p.
\tag{EDB-12}
\]

固定奇数阶 `K` 的主项近似为

\[
p\sum_{j=0}^{K}{(-\mu)^j\over j!}.
\tag{EDB-13}
\]

当 `p` 极大而 `K` 固定时，最后一项会主导并变负。因此固定阶 Bonferroni 与前面 `BPN-B5`
一样，只能作为低范围证据和结构定位工具；全局路线需要变量阶 `K=K(p)` 或 Selberg/Brun
非负权重。

## 6. 下一步严格目标

当前最窄硬点升级为：

```text
EDA-BK/Selberg:
construct variable-order Bonferroni/Brun/Selberg weights proving S_K(p,x)>0
for every 1<=x<=p, or route failure to PDEC/SAE.
```

具体拆分：

1. **Core6-tail bound.** 先证明五阶高重合惩罚满足显式上界，解释样本正余量；
2. **Variable K ledger.** 把固定 `K=5` 替换为 `K≈c log log p` 的可变阶账本；
3. **Selberg nonnegative majorant.** 用非负二次型替代振荡尾项，避免固定阶变号；
4. **Defect routing.** 若某行 `S_K<=0`，则高重合数过密，导出低模端点 CRT defect 或 SAE。

本步没有闭合 `EDA`，但给出一个实际可攻的新压缩：

```text
EDA-Dual
=> EDA-BK/Selberg
=> Core6-tail or PDEC/SAE.
```

这比直接面对短区间素数命题更适合继续利用 CRT 与互质结构刚性。

## 7. 审稿边界

本文件只完成三件可审稿事项：

1. 把 `EDA` 的早期幸存量 `U_p(x)` 写成完全初等的整除计数对象；
2. 证明奇数阶 Bonferroni 截断给出严格下界 `S_K(p,x)<=U_p(x)`；
3. 用五阶身份定位真实尾项，即 `>=6` 个 `<p` 小素因子的高重合惩罚。

尚未完成的全局证明事项是：

```text
prove min_{1<=x<=p} S_{K(p)}(p,x)>0 for all odd primes p
```

其中 `K(p)` 不能固定为 `5`；否则在 `log log p` 尺度上会有模型性变号风险。下一步若要
真正推进无条件闭合，必须在 `K≈c log log p` 的变量阶账本、Selberg/Brun 非负权重，
或 `CoreK-Density => PDEC/SAE` 路由中闭合至少一条。
