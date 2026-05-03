# H3-DSB 高 lcm 出口的 Fourier 能量夹逼

**状态：** `hlc_fourier_energy_clamp_proved_endpoint_pdec_exclusion_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层已经把 `high-lcm clamp` 分支路由为：

```text
Persistent-HLC / Sparse-HLC.
```

本文继续压缩这个硬障碍：证明高 `lcm` 单点化不是“无结构逃逸”，而是必然产生
非零 Fourier 能量。该能量若跨行持久，就是 `PDEC/ColumnCRT`；若只在单行出现，
就是 `SAE/endpoint` 局部出口。

## 1. 同模相位块

固定一个 dyadic 同模块 `B`，其中所有夹逼单元有同一模数

\[
R=R(B)>R_0.
\tag{HLCF-1}
\]

令 `X_B` 为该块中实际激活的高 `lcm` 孤立尾点。对每个剩余类 `a mod R` 定义计数测度

\[
\mu_B(a)=\#\{x\in X_B:x\equiv a\pmod R\},
\qquad
U_B=\sum_{a\bmod R}\mu_B(a).
\tag{HLCF-2}
\]

这里的同模块可由 `(r_-,r_+)` 的 `lcm`、差值类型、dyadic 尾标签区间和平滑权共同细分得到。
细分只造成多对数损失，不改变以下恒等式。

## 2. 精确 Fourier 能量恒等式

定义有限 Fourier 变换

\[
\widehat\mu_B(h)=
\sum_{a\bmod R}\mu_B(a)e\!\left(\frac{ha}{R}\right).
\tag{HLCF-3}
\]

由有限群 Plancherel 恒等式，

\[
\sum_{1\le h<R}|\widehat\mu_B(h)|^2
=
R\sum_{a\bmod R}\mu_B(a)^2-U_B^2.
\tag{HLCF-4}
\]

这是完全确定性的 CRT 恒等式，不使用素数分布。

## 3. 高 lcm 单点化强制能量

若 `R>q+O(1)`，则同一 `c` 在一行中至多贡献一个点；更一般地，上一层给出

\[
\mu_B(a)\le 1+\left\lfloor\frac{q+O(1)}{R_0}\right\rfloor
\tag{HLCF-5}
\]

的物理容量。由于 `\mu_B(a)` 为非负整数，始终有

\[
\sum_a\mu_B(a)^2\ge U_B.
\tag{HLCF-6}
\]

代入 `(HLCF-4)` 得

\[
\sum_{1\le h<R}|\widehat\mu_B(h)|^2
\ge
U_B(R-U_B).
\tag{HLCF-7}
\]

特别地，若

\[
U_B\le \frac{R}{2},
\tag{HLCF-8}
\]

则

\[
\sum_{1\le h<R}|\widehat\mu_B(h)|^2
\ge
\frac12 R U_B.
\tag{HLCF-9}
\]

这就是关键夹逼：高 `lcm` 分支越稀疏，非零 Fourier 能量越不可避免。

## 4. 端点/PDEC 二分

`(HLCF-9)` 的能量只有两个合法解释。

1. **跨行持久。** 若同类高 `lcm` 能量在许多坏行或 CRT 周期位置复现，则坏行指示函数与
   高 `lcm` 相位的卷积具有非零 Fourier 质量，进入 `PDEC/ColumnCRT`。
2. **单窗局部。** 若能量只集中在少数行，则它不是 KLS-window 主估计的一部分，而是
   `SAE/endpoint` 局部 sawtooth 能量。此时必须由端点、镜像、列见证或 cofactor 约束逐窗排除。

因此对任意高 `lcm` 同模块，

```text
U_B>0 and U_B<=R/2
=> nonzero Fourier energy >= R*U_B/2
=> PDEC/ColumnCRT persistent exit or SAE/endpoint local exit.
```

## 5. 对当前硬障碍的实际压缩

本文证明了一个更强的事实：`Persistent-HLC/Sparse-HLC` 不是两个新的自由缺口。
它们共享同一个 Fourier 能量源 `(HLCF-4)`。

当前唯一仍未闭合的是出口排斥本身：

```text
证明 HLCF-9 产生的能量不能被 PDEC/ColumnCRT 持久出口吸收，
且不能被 SAE/endpoint 单窗出口吸收。
```

换言之，高 `lcm` 分支已经被压缩为已知最终出口的能量注入问题；它不再需要新的
有限模板或新的命题转换。

后续阈值桥接见 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md`。该文把
非零能量转为同一 formal unit 的 PDEC 下界
`L_HLC=((R sum_a g(a)^2-U^2)/(R-1))^(1/2)`，并证明 `U>R/2` 的稠密例外不是新出口，而是
`KLS-window`、`PDEC/ColumnCRT` 或 `SAE/endpoint` 的已有入口。
