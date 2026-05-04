# AlphaTail PairCRTDefect 的相关型 PDEC 下界

**状态：** `alpha_tail_paircrt_correlation_pdec_lower_bound_open`

上一节把热尾素对拆成单残基 `H4-PDEC` 输入。样本显示单残基证书常数很小，
因为最热点位通常只命中 `1` 个点。真正有用的对象不是单残基，而是合并尾素对事件
`R(q_1,q_2)` 与低幸存集 `L` 的零均值相关。

## 1. 合并尾素对测试函数

固定尾素对 `q_1<q_2`，令

\[
Q=q_1q_2,\qquad
R=R(q_1,q_2)\subset\mathbb Z/Q\mathbb Z,
\tag{PCL-1}
\]

其中 `R` 是所有点位向量 `(j_1,j_2)` 给出的 CRT 残基并集。记

\[
\beta={|R|\over Q},\qquad
G_R(t)=1_R(t)-\beta.
\tag{PCL-2}
\]

令 `C(t)=#{d in L:d=t mod Q}`。尾素对偏差为

\[
E(q_1,q_2)=\sum_{t\bmod Q}C(t)G_R(t).
\tag{PCL-3}
\]

这是比单残基更强的 PDEC 对象：它保留了全部 `m^2` 个点位残基的合并偏差。

## 2. Fourier 下界

采用非归一 Fourier 变换

\[
\widehat F(h)=\sum_{t\bmod Q}F(t)e^{-2\pi iht/Q}.
\tag{PCL-4}
\]

由于 `G_R` 零均值，

\[
E(q_1,q_2)
={1\over Q}\sum_{1\le h<Q}\widehat C(-h)\widehat G_R(h).
\tag{PCL-5}
\]

又由 Parseval，

\[
\sum_{h\bmod Q}|\widehat G_R(h)|^2
=Q\sum_{t\bmod Q}|G_R(t)|^2
=Q\,|R|(1-\beta).
\tag{PCL-6}
\]

因此若 `E(q_1,q_2)>0`，存在非零频率满足

\[
\max_{h\ne0}|\widehat C(h)|
\ge
L_{\rm corr}(q_1,q_2)
:=
{E(q_1,q_2)\sqrt Q\over
\sqrt{Q-1}\sqrt{|R|(1-\beta)}}.
\tag{PCL-7}
\]

当 `q_i` 远大于 `m` 且点位不碰撞时，`|R|=b_{q_1}b_{q_2}=m^2`，于是

\[
L_{\rm corr}\approx {E(q_1,q_2)\over m}.
\tag{PCL-8}
\]

这解释了样本中“最热单残基很弱，但合并二阶偏差稳定可见”的现象。

## 3. Persistent 放大与 SAE 二分

单窗中的 `L_corr` 常为常数级，不能单独排斥。真正的用法是 persistent 聚合：
若同类 `(q_1,q_2)` 或同一归一化点位形状在许多窗口中持续给出同号 `E>0`，
则 `(PCL-5)` 的非零 Fourier 系数可线性累积，进入 `PDEC`。
若这些正偏差只在少数窗口出现，则它们不是全局缺陷，而是 `SAE` 局部逃逸义务。

因此二阶尾素对出口进一步变成：

```text
PairCRTDefect persistent => correlation-PDEC；
non-persistent => SAE；
若两者都排斥，则 tail-overlap 分支关闭。
```

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_pair_correlation_pdec_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_pair_correlation_pdec_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出 `E_pair/|R|/L_corr`。该脚本用于确认二阶偏差是否足以进入 persistent 相关型
PDEC，而不是退回单残基弱证书。

## 5. 审稿边界

已证明：

```text
E(q1,q2)>0 => 低幸存集 L 在模 Q=q1q2 上存在非零 Fourier 系数；
显式下界为 L_corr；
persistent 正相关进入 PDEC，非 persistent 进入 SAE。
```

尚未证明：

```text
所有 persistent correlation-PDEC 均可由 H4 上界证书排斥；
或所有正二阶偏差都只能孤立出现并由 SAE 吸收。
```

下一步最小硬点是定义跨窗口 persistent 聚合账本，核验热尾素对相位是否同向累积。
