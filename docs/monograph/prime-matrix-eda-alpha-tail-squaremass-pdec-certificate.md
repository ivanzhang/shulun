# SquareMass-PDEC：平方一阶质量亏损证书

**状态：** `alpha_tail_squaremass_pdec_certificate_reduction_open`

本文把 `square mass bridge` 的第一个出口形式化。若粗筛幸存集 `R` 在小素平方剩余类上的一阶质量
显著低于完整 CRT 模型，则该亏损是一个有限低模 `PDEC`，不是新的随机性黑箱。

## 1. 平方质量函数

取平方 cutoff `A<=y`，令

\[
Q_A=\prod_{a\le A}a^2
\tag{SMP-1}
\]

其中乘积只取素数 `a`。对多点链长度 `m` 定义

\[
H_A(d)=
\sum_{\substack{a\le A\\ a\ {\rm prime}}}
\sum_{0\le j<m}1_{a^2\mid d+jr}.
\tag{SMP-2}
\]

它只依赖 `d mod Q_A`。完整 residue 系上的均值为

\[
W_A=m\sum_{a\le A}{1\over a^2}.
\tag{SMP-3}
\]

定义零均值测试函数

\[
F_A(d)=H_A(d)-W_A.
\tag{SMP-4}
\]

## 2. 低平方/高平方二分

总平方质量缺陷为

\[
\mathcal E_{\rm sq}=S_1-|R|W_y.
\tag{SMP-5}
\]

其中 `W_y=m sum_{a<=y}1/a^2`。拆成

\[
\mathcal E_{\rm sq}
=
\sum_{d\in R}F_A(d)
+
\left[
\sum_{d\in R}(H_y(d)-H_A(d))
-|R|(W_y-W_A)
\right].
\tag{SMP-6}
\]

若 `\mathcal E_sq<=-\Delta`，则对任意 `0<beta<1` 至少发生一项：

1. **低平方 SquareMass-PDEC。**

\[
\sum_{d\in R}F_A(d)\le-\beta\Delta;
\tag{SMP-7}
\]

2. **高平方尾质量亏损。**

\[
\sum_{d\in R}(H_y-H_A)-|R|(W_y-W_A)\le-(1-\beta)\Delta.
\tag{SMP-8}
\]

第一项是有限模 `Q_A` 的低模相位偏置；第二项进入 `SquareTail/Rankin/SAE`。

## 3. Fourier 证书

令

\[
g(t)=\#\{d\in R:d\equiv t\pmod {Q_A}\}.
\tag{SMP-9}
\]

则

\[
\sum_{d\in R}F_A(d)=
\sum_{t\bmod Q_A}g(t)F_A(t).
\tag{SMP-10}
\]

因为 `F_A` 在完整 residue 系上均值为零，若 `(SMP-7)` 成立，则由 H4-PDEC 模板存在非零频率 `h`
满足

\[
\left|\widehat g(h)\right|
\ge
{\beta\Delta\over \sum_{h\ne0}|\widehat F_A(h)|}.
\tag{SMP-11}
\]

这就是 `SquareMass-PDEC` 证书：坏集合 `R` 在平方模 `Q_A` 上的相位分布有非零 Fourier 尖峰。

## 4. 证书字段

一个 `SquareMass-PDEC-Cert` 必须给出：

```text
p, B, r, m;
rough set definition R;
A and Q_A;
phase counts g(t);
test function F_A(t)=H_A(t)-W_A;
defect lower bound Delta;
Fourier normalization and lower bound L_PDEC;
route for high-square tail if not using low branch.
```

这与 `h4-pdec-certificate-template.md` 兼容：`S=R`，`tau(d)=d mod Q_A`，`F=F_A`。

## 5. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_squaremass_pdec_audit.py
```

样本：

| p | block | shift | m | A | rough | low sum | low model | centered | total defect |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 31 | 1186 | 4343 | 2116.066846 | 2226.933154 | 2218.214138 |
| 997 | 4096 | -36 | 5 | 31 | 995 | 4996 | 2219.104671 | 2776.895329 | 2763.777895 |
| 5003 | 8192 | -36 | 4 | 31 | 4577 | 13312 | 8166.305190 | 5145.694810 | 5125.688214 |
| 5003 | 8192 | -36 | 5 | 31 | 4261 | 16403 | 9503.120607 | 6899.879393 | 6869.373738 |
| 10007 | 16384 | -900 | 4 | 31 | 8518 | 23537 | 15197.856153 | 8339.143847 | 8317.402433 |
| 10007 | 16384 | -900 | 5 | 31 | 7629 | 27373 | 17014.622650 | 10358.377350 | 10324.443701 |

## 6. 审稿边界

已证明：

```text
square-mass deficit
=> low-square finite PDEC
   or high-square tail deficit.
```

尚未证明：

```text
低平方 PDEC 不可能；
高平方尾质量亏损不可能。
```

下一步最小硬点是给 `SquareMass-PDEC` 提交 PDEC 上界证书，或证明高平方尾由 Rankin/SAE 吸收。
