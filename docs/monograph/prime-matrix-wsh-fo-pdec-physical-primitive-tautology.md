# FO-PDEC physical/primitive 二点 Fourier tautology

**状态：** `physical_primitive_pdec_threshold_degenerate_routed_to_sae`

本文承接：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-dominance.md
docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.md
```

目标是处理上一轮留下的最后 PDEC 数值路线：

```text
physical/primitive PDEC threshold U_CRT < 1.9997507790353146。
```

结论是：当前 physical/primitive 前沿只有两个物理原子，该 Fourier 阈值不是结构缺陷，而是二点
支撑在素模数上的恒等现象。因此这条 PDEC 数值路线退化，不能作为闭合证明继续硬攻；当前分支应
转入 `SAE/Endpoint`。

## 1. 二点 Fourier 恒等式

设 `ell` 为素数，`a != b mod ell`。因为 `b-a` 可逆，取

\[
h\equiv (b-a)^{-1}\pmod \ell.
\]

则

\[
h b-h a\equiv 1\pmod \ell.
\]

所以两个对偶相位相邻，得到

\[
\max_{h\ne0}
\left|
e(ha/\ell)+e(hb/\ell)
\right|
=2\cos(\pi/\ell).
\tag{PPT-1}
\]

这说明任意两个不同残基都会在某个频率下形成几乎满质量 Fourier 信号。它不是 PDEC 异常。

## 2. 当前 `ell=199` 的应用

物理去重后的 `factor=199` 前沿只有两个候选：

```text
250541 = 199*1259, residues {61,126}, semiprime=250517, offset=24；
1664237 = 199*8363, residue {40}, semiprime=1664207, offset=30。
```

对任一残基选择，审计都得到：

```text
Fourier = 2*cos(pi/199) = 1.9997507790353146。
```

其中 `250541` 还有相位歧义：它的两个残基来自同一物理整数在两个重叠 `q` 坐标图中的表示，
并非同一 formal unit 的两个独立相位。

## 3. 退化判据

**引理 PPT-1（primitive 二点阈值退化）。**  
若 primitive PDEC 前沿在某个素模 `ell` 上只有两个物理残基，且没有额外 formal-unit 约束固定
频率或禁止相邻对偶相位，则目标

\[
U_{\rm CRT}<2\cos(\pi/\ell)
\]

不是可用 PDEC 排斥目标。它等价于要求排除所有二点支撑，而这已经超出 Fourier/PDEC 自身提供的
信息。

**证明。**  
由 `(PPT-1)`，任意二点支撑都能达到该阈值。因此该阈值不区分坏窗缺陷与普通二点集合。若要排除，
必须使用额外局部几何、端点、列位移、尾锚或 witness 证书；这正是 `SAE/Endpoint` 或更强命名出口，
不是 PDEC 数值阈值本身。证毕。

## 4. 前沿更新

此前三层强信号已经逐层被压下：

```text
raw library 3.959247567099438:
  被嵌套重复与 weighted-Hall 支配阻断；

coordinate-cap 2.9698366905785227:
  被 cross-q 坐标图重叠支配阻断；

physical/primitive 1.9997507790353146:
  是二点 Fourier tautology，不能作为 PDEC 排斥阈值。
```

因此当前 FO-PDEC 前沿不再是 `U_CRT` 常数优化，而是：

```text
SAE/Endpoint absorption for the two physical primitive atoms。
```

## 5. 边界

本文不排除未来出现的三点或更多点 primitive PDEC 家族。如果未来某个同一 formal unit 中有至少
三个非退化 physical atoms，且频率不能自由适配成二点相邻相位，则可以重新提交 primitive PDEC
阈值。当前 `factor=199` 前沿没有这种结构。
