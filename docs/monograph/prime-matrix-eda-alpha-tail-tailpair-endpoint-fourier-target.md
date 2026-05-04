# AlphaTail 端点持久键的 Fourier 目标频率账本

**状态：** `alpha_tail_endpoint_fourier_target_found_U_CRT_open`

本文接续端点相位测试函数。目标是核验 Fourier 归一化，并把每个持久键的责任频率
显式找出。该文件仍不排斥 PDEC；它把下一步上界证明的对象从“某个未知相位异常”
压缩为“下表中的具体频率必须被结构上界压住”。

## 1. 带权相位测度

固定 `Q`，令

\[
G_Q=(\mathbb Z/Q\mathbb Z)^2.
\]

对持久键 `K`，定义带权相位测度

\[
g_K(t)=
\sum_{\substack{e:\mathcal K(e)=K\\ \tau_Q(e)=t}}
\bigl(A_g(J_e)-C_{\rm local}B_g(J_e)\bigr)_+.
\tag{EFT-1}
\]

其总质量为

\[
M_K=\sum_{t\in G_Q}g_K(t).
\tag{EFT-2}
\]

采用未归一化 Fourier

\[
\widehat g_K(h)=
\sum_{t\in G_Q}
g_K(t)e^{-2\pi i\langle h,t\rangle/Q}.
\tag{EFT-3}
\]

正交归一化系数为

\[
\widehat g_K^{\,{\rm orth}}(h)
=Q^{-1}\widehat g_K(h),
\tag{EFT-4}
\]

因为 `|G_Q|=Q^2`。

## 2. 归一化核验

端点测试函数给出下界

\[
L_{\rm PDEC}^{\rm orth}(K,Q)
=
{ \kappa_{K,Q}M_K
\over
\sqrt{Q^2-1}\|F_{K,Q}\|_2}.
\tag{EFT-5}
\]

若计算得到

\[
\max_{h\ne0}|\widehat g_K^{\,{\rm orth}}(h)|
\ge L_{\rm PDEC}^{\rm orth}(K,Q),
\tag{EFT-6}
\]

则 Fourier 归一化与下界侧一致。注意 `(EFT-6)` 是下界核验，不是排斥；排斥需要上界

\[
U_{\rm CRT}(K,Q)
<
L_{\rm PDEC}^{\rm orth}(K,Q).
\tag{EFT-7}
\]

## 3. 样本责任频率

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本输出显示：

```text
所有持久键 normalization_pass=True；
最大键 g900:j1-0:u1:B 的
L_orth=0.09683839,
max_orth=0.13695172,
best_freq=(0,3)。
```

多数键的 `actual_over_lower≈1.414230`。这是因为当前样本中每个持久键只有两个观测端点相位，
观测相位指示函数的 Cauchy--Schwarz 下界损失约为 `sqrt(2)`。

## 4. 新的最窄硬点

经过本文，`Endpoint/PDEC` 分支不再缺：

```text
相位空间；
相位映射；
测试函数；
责任频率；
下界归一化。
```

唯一剩余是上界侧：

```text
对同一 S_K 和同一 best_freq，
由端点镜像、列残基、尾锚不可复用、Rankin 失败回流等约束
证明 max_h |g_hat_K^orth(h)| <= U_CRT(K,Q)
且 U_CRT(K,Q)<L_PDEC^orth(K,Q)。
```

若该上界失败，则不能口头吸收，必须把失败频率和相位主贡献回流到
`SAE / Rankin low-mod spike / Tail-anchor / ColumnCRT` 中的一个已定义出口。

## 5. 审稿边界

已完成：

```text
带权相位测度 g_K；
未归一化与正交归一化 Fourier 换算；
每个持久键的实际最大频率；
下界核验 normalization_pass。
```

未完成：

```text
结构上界 U_CRT(K,Q)；
同一坏窗集合上的对偶证书；
U_CRT<L_PDEC 的严格余量。
```

所以本文将硬点压缩为可计算、可引用的频率上界问题，但不宣称行命题闭合。
