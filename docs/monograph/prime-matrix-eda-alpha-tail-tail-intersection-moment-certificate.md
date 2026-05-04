# AlphaTail 条件尾交集矩证书

**状态：** `alpha_tail_tail_intersection_moment_reduction_open`

本文把 tail-overlap 分支继续压缩为有限阶交集矩。目标不是直接宣称尾盈余不可能，
而是把“重叠过强”转成可逐阶核验的 CRT 交集偏差。

## 1. 二阶矩支配重叠预算

沿用 `tail-overlap Rankin ledger` 的记号。令

\[
M_t=\sum_{d\in L}{h_T(d)\choose t}
=\sum_{\{q_1,\dots,q_t\}\subseteq\mathcal P_T}
\left|\mathcal A_{q_1}\cap\cdots\cap\mathcal A_{q_t}\right|.
\tag{TIM-1}
\]

特别地，

\[
\Omega_T=\sum_{d\in L}\max(h_T(d)-1,0).
\tag{TIM-2}
\]

对每个整数 `h>=0`，

\[
\max(h-1,0)\le {h\choose2}.
\tag{TIM-3}
\]

于是

\[
\Omega_T\le M_2.
\tag{TIM-4}
\]

这说明：条件尾删除不足若由重叠支付，必然在二阶尾素交集中留下可见质量。

## 2. 乘法模型交集矩

记

\[
c_q={b_q\over q},\qquad b_q=\#\{-jr\bmod q:0\le j<m\}.
\tag{TIM-5}
\]

若低幸存集 `L` 对尾 CRT 模数无偏，则 `t` 阶交集矩的乘法模型为

\[
B_t=|L|\,e_t(\{c_q:q\in\mathcal P_T\}),
\tag{TIM-6}
\]

其中 `e_t` 是 elementary symmetric sum。实际偏差为

\[
D_t=M_t-B_t.
\tag{TIM-7}
\]

由 `(TIM-1)`，`D_t` 是有限 CRT 交集偏差的总和。若 `D_t` 持续为正，则存在某个
尾素集合与点位向量使

\[
\left|\bigcap_{i=1}^t\mathcal A_{q_i}\right|
>
|L|\prod_{i=1}^t{b_{q_i}\over q_i}
\tag{TIM-8}
\]

超过可接受误差。这就是 `ColumnCRT/PDEC` 证书；若只在单窗出现，则进入 `SAE`。

## 3. 交集矩出口

设 `Xi_T>0` 且 tail-mass 不承担缺口。由前文得到 `Omega_T>=Xi_T-eta`。
再由 `(TIM-4)`：

\[
M_2\ge \Xi_T-\eta.
\tag{TIM-9}
\]

因此只有两种可能：

1. **模型交集矩足够大。**  
   `B_2` 本身足以解释 `Omega_T`。此时必须把 `B_2` 纳入 Rankin 常数账本，继续比较
   `M_2` 对删除缺口的可支付上限。
2. **实际交集矩超过模型。**  
   `D_2>0` 达到阈值，进入有限 `ColumnCRT/PDEC`。若二阶被模型吸收但高重数仍过强，
   则检查 `D_3,D_4,...`；点态乘积界保证阶数有限。

这把 tail-overlap 的剩余义务降成有限阶命题：

```text
证明所有 D_t 的正偏差被 ColumnCRT/PDEC/SAE 排斥；
或证明 B_t 的 Rankin 常数总账不能支付 Xi_T。
```

## 4. 审计样本

脚本：

```text
experiments/prime_matrix_alpha_tail_tail_intersection_moment_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tail_intersection_moment_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

关键输出：

| p | block | r | m | Omega | Xi tail | M2 | B2 | D2 | M3 | B3 | D3 | max hit | L bound |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 1997 | -132.977969 | 2547 | 2235.824023 | 311.175977 | 600 | 799.001724 | -199.001724 | 4 | 5 |
| 997 | 4096 | -36 | 5 | 2938 | 2.937460 | 4188 | 3440.229097 | 747.770903 | 1485 | 1536.765054 | -51.765054 | 5 | 6 |
| 5003 | 8192 | -36 | 4 | 2007 | -2.220340 | 2379 | 1266.233610 | 1112.766390 | 389 | 236.685104 | 152.314896 | 4 | 4 |
| 5003 | 8192 | -36 | 5 | 3069 | 304.875182 | 3941 | 1967.159022 | 1973.840978 | 947 | 459.628098 | 487.371902 | 4 | 5 |
| 10007 | 16384 | -900 | 4 | 3600 | 449.673028 | 4493 | 1876.171255 | 2616.828745 | 963 | 327.828066 | 635.171934 | 4 | 4 |
| 10007 | 16384 | -900 | 5 | 5063 | 1024.015281 | 6997 | 2736.312396 | 4260.687604 | 2243 | 597.653331 | 1645.346669 | 5 | 5 |

样本显示：`Omega<=M2` 恒成立；正 `Xi_tail` 样本同时伴随显著正 `D2`。
这支持当前路线：把条件尾盈余的真实承担者定位为二阶或三阶 CRT 交集偏差。

## 5. 审稿边界

已证明：

```text
tail-overlap 必满足 Omega_T<=M2；
M_t 等于 t 阶尾删除事件交集总量；
M_t-B_t>0 是有限 CRT 交集偏差；
持续偏差进入 ColumnCRT/PDEC，孤立偏差进入 SAE。
```

尚未证明：

```text
ColumnCRT/PDEC/SAE 出口全部排斥；
或 B_t 的 Rankin 常数总账在全局参数中无法支付 Xi_T。
```

下一步最小硬点是把 `(TIM-8)` 的二阶正偏差转成显式低模 Fourier/PDEC 下界。
