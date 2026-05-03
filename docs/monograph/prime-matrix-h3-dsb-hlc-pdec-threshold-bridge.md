# H3-DSB 高 lcm 持久出口到 PDEC 阈值的桥接

**状态：** `hlc_persistent_pdec_threshold_bridge_proved_certificate_upper_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层已经证明：同模高 `lcm` 块若存在质量 `U`，其非零 Fourier 能量为
`R sum mu(a)^2-U^2`。本文把这个能量改写成可直接接入 `PDEC-Cert` 的阈值，
并处理唯一的稠密例外 `U>R/2`。

## 1. 同一 formal unit

固定一个高 `lcm` 同模块 `B`。所有对象必须使用同一 formal unit：

```text
Q=R(B)；
S_B = 该模块内的高 lcm 激活事件多重集合；
tau(x)=x mod R(B)；
g_B(a)=#{x in S_B: tau(x)=a}；
U_B=sum_a g_B(a)。
```

不能把不同 `R`、不同 dyadic 尾标签块、不同窗口宽度或不同坏行集合的事件混成一个
PDEC 向量。这一点与 `h4-pdec-certificate-template.md` 的 formal-unit 口径一致。

## 2. 非零频率阈值

令

\[
\widehat g_B(h)=
\sum_{a\bmod R}g_B(a)e\!\left(\frac{ha}{R}\right).
\tag{HPT-1}
\]

由 Plancherel，

\[
\sum_{1\le h<R}|\widehat g_B(h)|^2
=
R\sum_{a\bmod R}g_B(a)^2-U_B^2.
\tag{HPT-2}
\]

因此必存在非零频率满足

\[
\max_{1\le h<R}|\widehat g_B(h)|
\ge
L_{\rm HLC}(B)
:=
\left(
\frac{R\sum_a g_B(a)^2-U_B^2}{R-1}
\right)^{1/2}.
\tag{HPT-3}
\]

这是 `HLC` persistent 分支进入 PDEC 证书的显式下界。

## 3. 稀疏区的统一下界

若

\[
U_B\le \frac{R}{2},
\tag{HPT-4}
\]

则由 `sum_a g_B(a)^2>=U_B` 得

\[
L_{\rm HLC}(B)
\ge
\left(\frac{RU_B}{2(R-1)}\right)^{1/2}.
\tag{HPT-5}
\]

若还知道支持大小 `A_B=#\{a:g_B(a)>0\}`，则有更精细的支持版

\[
L_{\rm HLC}(B)
\ge
U_B\left(\frac{R/A_B-1}{R-1}\right)^{1/2}.
\tag{HPT-6}
\]

`(HPT-5)` 是无条件稀疏下界；`(HPT-6)` 只在支持压缩时更强。

## 4. 稠密例外不是新出口

若 `(HPT-4)` 失败，即

\[
U_B>\frac{R}{2},
\tag{HPT-7}
\]

则该块在模 `R` 上已经达到正密度。因为 `B` 是高 `lcm` 同模块，这意味着：

```text
同一个 R(B) 相位层承载超过一半剩余类规模的高 lcm 事件。
```

这不属于分散高 `lcm` 逃逸，而是 `Clamp low-mod concentration / PDEC` 入口：

1. 若 `R` 仍在 KLS 可控模数范围，则回到 `KLS-window` 主分支；
2. 若 `R` 超出 KLS 范围，则它给出一个持久高模相位高负载，进入 `PDEC/ColumnCRT`；
3. 若只在单行发生，则进入 `SAE/endpoint`。

因此 `U_B>R/2` 不是新的第五分支；它是稠密低有效模集中，必须按已有出口处理。

## 5. 可提交的 PDEC 检验式

对每个 formal unit `B`，persistent 高 `lcm` 出口的 PDEC 检验式为：

```text
输入：R, S_B, tau, g_B；
下界：L_HLC(B) from (HPT-3)，稀疏时可用 (HPT-5)；
上界：同一 formal unit 的 CRT 约束证书给出 U_CRT(B)；
验收：U_CRT(B)<L_HLC(B)。
```

若验收失败，必须输出失败频率、方向、主贡献相位和缺失约束行；失败只能回流到
`SAE/endpoint`、`ColumnCRT` 或新的同口径 PDEC 约束，不能回到 KLS 主估计。

## 6. 当前实际闭合度

本文完成：

1. `Persistent-HLC` 到 PDEC 非零频率阈值 `(HPT-3)`；
2. 稀疏区统一阈值 `(HPT-5)`；
3. 稠密例外 `U_B>R/2` 的合法路由；
4. formal-unit 口径，防止跨模数、跨窗口、跨行族混合。

本文仍未完成：

```text
对所有 formal unit 证明 U_CRT(B)<L_HLC(B)。
```

这就是当前剩余硬障碍的精确形式。它不再是“高 lcm 是否有结构”，而是同一 formal unit
中的 PDEC 上界证书是否足以压过显式下界。

