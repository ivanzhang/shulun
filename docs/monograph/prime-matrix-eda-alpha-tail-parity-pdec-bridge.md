# 对称差奇偶偏置到 Parity-PDEC

**状态：** `alpha_tail_parity_pdec_bridge_reduction_open`

本文把 `Möbius parity lock` 的剩余偏置写成显式低模奇偶测试函数。这样，若未锁单边素因子的奇偶
长期偏偶，就不再是模糊的 Möbius 随机性问题，而是一个命名的 `Parity-PDEC`。

## 1. 局部奇偶函数

固定位移 `r`。对素数 `q<=y` 定义

\[
\psi_{q,r}(d)=
\begin{cases}
-1,& q\nmid r,\ d\equiv0\ {\rm or}\ -r\pmod q,\\
+1,& \text{otherwise}.
\end{cases}
\tag{PPB-1}
\]

在 `d,d+r` 均 squarefree 的支撑上，若 `q|r`，则 `q` 只能共同出现或共同不出现，不影响
Möbius 乘积；若 `q\nmid r`，单边出现正好让 `psi_{q,r}` 取 `-1`。

因此

\[
\mu(d)\mu(d+r)=
\prod_{q\le y}\psi_{q,r}(d)
\tag{PPB-2}
\]

在 `A_r` 上成立。

## 2. 低模截断

取 cutoff `R<=y`，写

\[
\Psi_{R,r}(d)=\prod_{q\le R}\psi_{q,r}(d),
\qquad
\Theta_{R,y,r}(d)=\prod_{R<q\le y}\psi_{q,r}(d).
\tag{PPB-3}
\]

则

\[
K(r)=\sum_{d\in A_r}\Psi_{R,r}(d)\Theta_{R,y,r}(d).
\tag{PPB-4}
\]

## 3. 二分

对任意 `0<beta<1`，若

\[
K(r)\ge\kappa |A_r|,
\tag{PPB-5}
\]

则至少发生一项：

1. **低模 Parity-PDEC。**

\[
\left|\sum_{d\in A_r}\Psi_{R,r}(d)\right|
\ge \beta\kappa |A_r|;
\tag{PPB-6}
\]

2. **高尾奇偶偏置。**

\[
\left|
\sum_{d\in A_r}\Psi_{R,r}(d)(\Theta_{R,y,r}(d)-1)
\right|
\ge (1-\beta)\kappa |A_r|.
\tag{PPB-7}
\]

这是由 `(PPB-4)` 加减 `sum_A Psi_R` 得到的确定性二分。

## 4. 出口解释

`(PPB-6)` 是有限低模测试函数偏置。因为 `Psi_{R,r}` 只依赖

\[
d\bmod \prod_{q\le R}q,
\tag{PPB-8}
\]

它就是 `Parity-PDEC`：坏窗口在一个显式低模符号函数上有非零均值。

`(PPB-7)` 是高素尾奇偶偏置。它说明大于 `R` 的单边素因子奇偶仍无法平均掉；该分支进入
`TailParity/Rankin/SAE`。

## 5. 当前最小硬点

经过本文，`K(r)` 的最终剩余不再是抽象 Möbius 相关，而是：

```text
Parity-PDEC：排斥有限低模奇偶测试函数偏置；
TailParity：证明高素尾奇偶平均，或失败进入 SAE/ColumnCRT。
```

本文只完成二分与证书化，不排斥两个出口。
