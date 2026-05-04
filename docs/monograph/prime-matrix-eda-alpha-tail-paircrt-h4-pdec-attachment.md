# AlphaTail PairCRTDefect 到 H4-PDEC 的接入证书

**状态：** `alpha_tail_paircrt_h4_pdec_attachment_open`

本文把上一节的热尾素对 `PairCRTDefect` 接到现有 `H4-PDEC` 证书模板。结论是：
二阶尾素对正偏差已经不是新的出口；它可被写成同一坏窗集合上的低模零均值测试函数。
但本文仍不排斥该缺陷，排斥需要后续提交 `U_CRT<L_PDEC` 的上界证书。

## 1. 固定点位单残基证书

固定尾素对 `q_1<q_2` 与点位 `(j_1,j_2)`。令

\[
Q=q_1q_2.
\tag{PH4-1}
\]

CRT 给出唯一残基 `a=a(q_1,q_2,j_1,j_2)`：

\[
a\equiv -j_1r\pmod {q_1},\qquad
a\equiv -j_2r\pmod {q_2}.
\tag{PH4-2}
\]

令

\[
S_a=\{d\in L:\ d\equiv a\pmod Q\}.
\tag{PH4-3}
\]

若 `|S_a|` 显著大于 `|L|/Q`，则这是一个 `ColumnCRT` 尖峰。为了接入 H4-PDEC，
定义相位映射

\[
\tau(d)=d\bmod Q
\tag{PH4-4}
\]

和零均值测试函数

\[
F_a(t)=1_{t=a}-{1\over Q}.
\tag{PH4-5}
\]

对每个 `d in S_a`，

\[
F_a(\tau(d))=1-{1\over Q}=:\kappa_a>0.
\tag{PH4-6}
\]

因此 `S=S_a,F=F_a,kappa=kappa_a` 满足 `H4-PDEC` 模板的下界输入。

## 2. Fourier 下界常数

采用 H4 模板中的相位 `L^2` 范数：

\[
\|F_a\|_2^2=\sum_{t\bmod Q}|F_a(t)|^2=1-{1\over Q}.
\tag{PH4-7}
\]

于是

\[
L_{\rm PDEC}(a)
=
{\kappa_a |S_a|\over \sqrt{Q-1}\|F_a\|_2}
= {|S_a|\over\sqrt Q}.
\tag{PH4-8}
\]

这与直接 Fourier 计算一致：单残基支撑集合的非零 Fourier 系数模长为 `|S_a|`，
而 `(PH4-8)` 是 Cauchy 形式的保守下界。

## 3. 与二阶偏差的关系

尾素对合并事件的偏差为

\[
E(q_1,q_2)=
\sum_{j_1,j_2}
\left(|S_{a(j_1,j_2)}|-{|L|\over Q}\right).
\tag{PH4-9}
\]

因此若 `E(q_1,q_2)>0`，至少存在点位对满足

\[
|S_a|-{|L|\over Q}
\ge {E(q_1,q_2)\over b_{q_1}b_{q_2}}.
\tag{PH4-10}
\]

脚本直接输出最大点位残基，其偏差就是 `(PH4-10)` 的具体证书候选。持续出现时，
这些 `S_a` 形成 persistent `PairCRTDefect-PDEC`；孤立出现时，进入 `SAE`。

## 4. H4-PDEC 输入表

对每个热残基证书，提交给 H4 的数据为：

```text
Q        = q1*q2；
X        = 低大素幸存集 L 所在窗口；
tau(d)   = d mod Q；
S        = {d in L: tau(d)=a}；
g(t)     = #{d in S: tau(d)=t}；
F(t)     = 1_{t=a}-1/Q；
kappa    = 1-1/Q；
||F||_2  = sqrt(1-1/Q)；
L_PDEC   = |S|/sqrt(Q)。
```

该表与 `h4-pdec-certificate-template.md` 的输入对象逐项匹配。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_pair_h4_pdec_attachment_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_pair_h4_pdec_attachment_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出 `Q/support_count/model/deviation/kappa/l2/L_PDEC/max_hat`。其中 `max_hat=support_count`
是单残基显式 Fourier 系数；`L_PDEC` 是 H4 模板下界。

## 6. 审稿边界

已证明：

```text
热尾素对点位正偏差 => 单残基 ColumnCRT 尖峰；
该尖峰逐项满足 H4-PDEC 输入格式；
H4 下界常数为 L_PDEC=|S_a|/sqrt(Q)。
```

尚未证明：

```text
对该 S_a 的结构约束能给出 U_CRT<L_PDEC；
或所有此类尖峰都由 ColumnCRT/SAE 出口排斥。
```

下一步最小硬点是：为 `S_a` 补充来自低幸存集 `L` 的结构约束行。若约束不足，
失败项应回流为 `tail-anchor`、`low-mod spike` 或 `SAE`。
