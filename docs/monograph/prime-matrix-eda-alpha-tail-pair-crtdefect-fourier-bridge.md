# AlphaTail 二阶尾素对偏差到 Fourier/PDEC 桥

**状态：** `alpha_tail_pair_crtdefect_fourier_bridge_open`

本文承接 `tail intersection moments`：当 `D_2=M_2-B_2` 为正时，
必须把二阶尾素交集偏差落到某个显式 CRT 模数上。本文件给出无条件代数桥。

## 1. 尾素对交集偏差

固定两个不同尾素 `q_1,q_2 in P_T`。令

\[
Q=q_1q_2,\qquad
R(q_1,q_2)=
\{a\bmod Q:\exists j_1,j_2<m,\ a+j_ir\equiv0\pmod {q_i}\}.
\tag{PCF-1}
\]

设

\[
C_Q(a)=|\{d\in L:d\equiv a\pmod Q\}|.
\tag{PCF-2}
\]

该尾素对的实际交集为

\[
I(q_1,q_2)=\sum_{a\in R(q_1,q_2)}C_Q(a).
\tag{PCF-3}
\]

乘法模型为

\[
B(q_1,q_2)=|L|{b_{q_1}b_{q_2}\over q_1q_2}.
\tag{PCF-4}
\]

定义

\[
E(q_1,q_2)=I(q_1,q_2)-B(q_1,q_2).
\tag{PCF-5}
\]

则

\[
D_2=\sum_{q_1<q_2}E(q_1,q_2).
\tag{PCF-6}
\]

因此若 `D_2>0`，至少存在一个尾素对满足 `E(q_1,q_2)>0`；定量地，若所有
`E(q_1,q_2)<=tau(q_1,q_2)`，则 `D_2<=sum tau(q_1,q_2)`。

## 2. 零均值测试函数

定义 `Q` 上的显式零均值函数

\[
G_{q_1,q_2}(a)=1_{R(q_1,q_2)}(a)-{|R(q_1,q_2)|\over Q}.
\tag{PCF-7}
\]

因为 `q_1,q_2` 不同，CRT 给出

\[
|R(q_1,q_2)|=b_{q_1}b_{q_2}.
\tag{PCF-8}
\]

于是

\[
E(q_1,q_2)=\sum_{a\bmod Q}C_Q(a)G_{q_1,q_2}(a).
\tag{PCF-9}
\]

这已经是 PDEC 格式：低幸存集的残基计数 `C_Q` 与一个显式零均值测试函数相关。

## 3. Fourier 下界

采用非归一 Fourier 变换

\[
\widehat F(h)=\sum_{a\bmod Q}F(a)e^{-2\pi iha/Q}.
\tag{PCF-10}
\]

由 `(PCF-9)` 和 `\widehat G(0)=0`，

\[
E(q_1,q_2)
={1\over Q}\sum_{1\le h<Q}
\widehat C_Q(-h)\widehat G_{q_1,q_2}(h).
\tag{PCF-11}
\]

因此若 `E(q_1,q_2)>0`，则存在 `h!=0 mod Q` 使

\[
|\widehat C_Q(h)|
\ge
{E(q_1,q_2)Q\over
\sum_{1\le h<Q}|\widehat G_{q_1,q_2}(h)|}.
\tag{PCF-12}
\]

也可用 Cauchy 形式：

\[
\sum_{1\le h<Q}|\widehat C_Q(h)|^2
\ge
{E(q_1,q_2)^2Q^2\over
\sum_{1\le h<Q}|\widehat G_{q_1,q_2}(h)|^2}.
\tag{PCF-13}
\]

这把任意正尾素对偏差转成非零 Fourier/CRT 缺陷。持续出现时即 `PDEC`；
只在单个窗口出现时即 `SAE`。

## 4. 点位向量细化

若需要更尖锐的证书，可不合并全部 `R(q_1,q_2)`，而固定点位向量 `(j_1,j_2)`。
此时只有一个 CRT 残基

\[
a\equiv -j_1r\pmod {q_1},\qquad
a\equiv -j_2r\pmod {q_2}.
\tag{PCF-14}
\]

模型为 `|L|/(q_1q_2)`。若某个点位残基计数显著过大，则直接得到单残基
`ColumnCRT` 尖峰；它比合并事件版 `(PCF-12)` 更强。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_pair_crtdefect_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_pair_crtdefect_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

脚本输出每个样本中正偏差最大的尾素对及其最热点位向量。该输出是 `(PCF-12)` 的
候选证书入口：先锁定 `(q_1,q_2,j_1,j_2)`，再提交对应模 `Q=q_1q_2` 的 Fourier/PDEC 下界。

## 6. 审稿边界

已证明：

```text
D2>0 => 存在尾素对 E(q1,q2)>0；
E(q1,q2) 是低幸存集残基计数与显式零均值函数的相关；
E(q1,q2)>0 => 存在非零 Fourier/CRT 系数下界；
固定点位正偏差直接给出 ColumnCRT 尖峰。
```

尚未证明：

```text
这些 Fourier/CRT 缺陷全部被全局 PDEC/SAE 机制排斥；
或所有尾素对偏差总和不足以支付 Xi_T。
```

下一步最小硬点是把热尾素对脚本输出接到现有 H4-PDEC 模板，形成可验收的
`PairCRTDefect-PDEC` 证书行。
