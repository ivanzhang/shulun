# WSS 过剩到双线性 Fourier 证书

**状态：** `alpha_tail_wss_bilinear_fourier_certificate_reduction_open`

本文把 `WSS short-interval excess` 继续压成明确的 Fourier/PDEC 证书。核心是：短区间条件

\[
p^2<md\le p^2+H
\]

是一条乘法双线性双曲线带。若这条带中的低素平方自由数异常过多，则必有非零频率上的双线性
指数和异常。

## 1. 有限双曲线带

固定高块 `I=(B,2B]` 与互补因子带

\[
J_I=\left({p^2+1\over2B},{p^2+H\over B}\right].
\tag{BFC-1}
\]

取有限集合 `M subset J_I` 与 `D subset I`，其中 `D` 是低素 squarefree 数集合，例如
`D=D_I^-`。令

\[
S(M,D)=
\#\{(m,d)\in M\times D:1\le md-p^2\le H\}.
\tag{BFC-2}
\]

取整数 `Q>4p^2`，在 `Z/QZ` 上定义

\[
K_H(r)=\mathbf 1_{1\le r\le H}.
\tag{BFC-3}
\]

由于 `m in J_I`、`d in I` 蕴含

\[
{p^2\over2}+O(1)<md<2p^2+O(p),
\tag{BFC-4}
\]

所有参与的 `md-p^2` 都在绝对值小于 `Q/2` 的范围内，模 `Q` 不发生绕回误判，因此

\[
S(M,D)=\sum_{m\in M}\sum_{d\in D}K_H(md-p^2).
\tag{BFC-5}
\]

## 2. Fourier 展开

采用

\[
\widehat K_H(h)=\sum_{r\bmod Q}K_H(r)e^{-2\pi ihr/Q}.
\tag{BFC-6}
\]

则

\[
K_H(r)={1\over Q}\sum_{h\bmod Q}\widehat K_H(h)e^{2\pi ihr/Q}.
\tag{BFC-7}
\]

代入 `(BFC-5)` 得

\[
S(M,D)=
{H\over Q}|M||D|
+
{1\over Q}
\sum_{1\le h<Q}
\widehat K_H(h)e^{-2\pi ihp^2/Q}
B_h(M,D),
\tag{BFC-8}
\]

其中

\[
B_h(M,D)=
\sum_{m\in M}\sum_{d\in D}e^{2\pi ihmd/Q}.
\tag{BFC-9}
\]

这就是双线性 Fourier 证书对象。

## 3. 异常推出非零频率

设

\[
\Delta=
\left|S(M,D)-{H\over Q}|M||D|\right|.
\tag{BFC-10}
\]

由 `(BFC-8)`，

\[
\Delta\le {1\over Q}
\left(\sum_{1\le h<Q}|\widehat K_H(h)|\right)
\max_{1\le h<Q}|B_h(M,D)|.
\tag{BFC-11}
\]

而区间核满足标准估计

\[
\sum_{1\le h<Q}|\widehat K_H(h)|\le C Q\log Q
\tag{BFC-12}
\]

其中 `C` 为绝对常数。因此若 `Delta>0`，存在非零频率 `h` 使

\[
|B_h(M,D)|\ge {\Delta\over C\log Q}.
\tag{BFC-13}
\]

**证明。**  
`(BFC-8)` 给出 `(BFC-11)`。对区间指数和使用
`|Khat(h)|<=min(H,Q/(2 min(h,Q-h)))`，两侧调和求和得到 `(BFC-12)`。
整理即得 `(BFC-13)`。证毕。

## 4. 接入 WSS 出口

在 `CIN` 中，`WSS short-interval excess` 给出一批互补因子 `M` 与奇符号低素平方自由集合
`D_I^-`，使 `S(M,D_I^-)` 超过局部模型。若该过剩不能由 local/global model mismatch 吸收，
则 `(BFC-13)` 给出非零频率证书：

```text
存在 h!=0，使 sum_{m in M} sum_{d in D_I^-} exp(2π i h m d / Q)
达到异常大尺度。
```

这是标准的 `PDEC/ColumnCRT` 入口：

1. `m` 来自低互补因子带；
2. `d` 来自低素 squarefree 高块；
3. 相位是乘法 `md`；
4. 非零频率异常表示双曲线带在模 `Q` 上出现持久相位集中。

## 5. 审稿边界

已证明：

```text
WSS distributed excess + model mismatch 未吸收
=> 非零双线性 Fourier/PDEC 证书。
```

尚未证明：

```text
所有这种双线性 Fourier 证书不可能。
```

下一步真正硬点是证明 `B_h(M,D)` 在本文结构化集合上满足足够的平均抵消，或证明抵消失败强制
进入已有 `ColumnCRT/SAE` 证书并被有限排斥。
