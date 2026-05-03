# H3-DSB 高 lcm 夹逼分支路由

**状态：** `high_lcm_clamp_persistent_sparse_dichotomy_proved_exclusion_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把最终频率缺陷拆成四个分支：

```text
KLS-window / high-lcm clamp / high-frequency endpoint / coefficient concentration.
```

本文专攻其中 `high-lcm clamp`。目标不是换命题，而是证明该分支不能混在 KLS 主项里处理；
它必须被路由成一个明确的稀疏夹逼缺陷或单窗逃逸义务。

## 1. 高 lcm 分裂

对夹逼单元

\[
c=(\delta_-,\delta_+,r_-,r_+),\qquad r_\pm\le y,
\]

记

\[
R(c)=\operatorname{lcm}(r_-,r_+).
\tag{HLC-1}
\]

给定阈值 `R_0`，把活跃夹逼单元分裂为

\[
C_{\le R_0}=\{c:R(c)\le R_0\},
\qquad
C_{>R_0}=\{c:R(c)>R_0\}.
\tag{HLC-2}
\]

`C_{\le R_0}` 是 KLS-window 候选输入；`C_{>R_0}` 是本文处理的高 lcm 分支。

## 2. 单元容量恒等式

固定 `c`。左右小骨架夹逼给出唯一类

\[
a\equiv \rho(c)\pmod{R(c)}.
\tag{HLC-3}
\]

在一条 H3 行窗口 `I` 中，长度 `H<=q+O(1)`，属于该夹逼单元的候选点数满足

\[
N(c)\le 1+\left\lfloor \frac{H}{R(c)}\right\rfloor.
\tag{HLC-4}
\]

因此若 `R(c)>R_0`，

\[
N(c)\le 1+\left\lfloor \frac{q+O(1)}{R_0}\right\rfloor.
\tag{HLC-5}
\]

这是确定性容量，不依赖素数分布。

## 3. 高 lcm 质量的稀疏化

令

\[
U_{>R_0}=\sum_{c\in C_{>R_0}}N(c)
\tag{HLC-6}
\]

为高 lcm 夹逼承载的孤立尾点数，令

\[
A_{>R_0}=\#\{c\in C_{>R_0}:N(c)>0\}
\tag{HLC-7}
\]

为活跃高 lcm 单元数。由 `(HLC-5)` 得

\[
U_{>R_0}
\le
A_{>R_0}\left(1+\left\lfloor \frac{q+O(1)}{R_0}\right\rfloor\right).
\tag{HLC-8}
\]

等价地，若高 lcm 分支承载自然量级质量

\[
U_{>R_0}\ge \eta \frac{q}{\log y},
\tag{HLC-9}
\]

则必须有

\[
A_{>R_0}
\ge
\frac{\eta q/\log y}{1+\lfloor(q+O(1))/R_0\rfloor}.
\tag{HLC-10}
\]

取

\[
R_0=\frac{q}{(\log q)^B},
\tag{HLC-11}
\]

得到

\[
A_{>R_0}\gg_{\eta,B}\frac{q}{(\log y)(\log q)^B}.
\tag{HLC-12}
\]

也就是说，高 lcm 分支若仍很大，它不是少数夹逼相位高负载，而是大量几乎单点的高 lcm 夹逼单元。

## 4. 为什么这不是 KLS 主分支

KLS-window 需要在可控模数范围内平均逆元相位

\[
e\!\left(-\frac{h\rho(c)\bar\ell}{R(c)}\right).
\]

当 `R(c)>R_0` 且甚至可能 `R(c)>q` 时，一行内每个 `c` 通常只给一个物理点。此时：

1. 没有足够的同模样本供 KLS 在该行内平均；
2. 精确 Fourier 展开需要 `1<=h<R(c)` 的长频率族；
3. 单个物理点可由极多高频表示，普通频率截断会把端点误差放大；
4. 因此高 lcm 分支不能并入低模 KLS 主估计。

这证明 `high-lcm clamp` 必须单独路由。

## 5. 高 lcm 分支的缺陷定义

定义 `HighLCM-Clamp` 缺陷为：

```text
存在一条 H3 行和阈值 R0，使
U_{>R0} >= eta*q/log y，
且没有 tail-label concentration、没有 clamp low-mod concentration，
但 A_{>R0} 满足 (HLC-10) 的大量稀疏高 lcm 单元激活。
```

该缺陷的含义是：反例不再表现为少数同余类过密，而表现为大量高 lcm 单点相位逃逸。

这类逃逸只能有两个后续出口：

1. **Persistent high-lcm defect**：若这种逃逸在许多行或周期位置持续，坏行指示函数在高 lcm
   夹逼坐标上产生非零 Fourier/CRT 缺陷；
2. **Sparse single-window escape**：若只在孤立行发生，则必须用端点、镜像、列见证或互补商
   结构逐窗排除。

## 6. Persistent/Sparse 二分路由

把所有坏行组成集合 `S`，记

\[
U_{>R_0}(S)=\sum_{s\in S}U_{>R_0}(s).
\tag{HLC-13}
\]

给定行阈值 `sigma`，必有确定性二分：

```text
Persistent-HLC:
  U_{>R0}(S) >= sigma*|S|*q/log y；

Sparse-HLC:
  Persistent-HLC 失败，全部 q/log y 级质量只能集中在少量孤立行。
```

在 persistent 分支中，令 `1_s` 为坏行指示函数。若高 lcm 质量不是低频常数项，
则对某个 `R(c)>R_0` 与某个非零频率 `h`，有限 CRT Fourier 展开给出

\[
\left|
\sum_{s\in S}
1_s
e\!\left(\frac{h\,\rho_s(c)}{R(c)}\right)
\right|
\gg
\frac{U_{>R_0}(S)}{\mathcal L},
\tag{HLC-14}
\]

其中 `mathcal L` 只记录 dyadic 分块、平滑截断和 gcd 层的多对数损失。于是 persistent
高 lcm 逃逸不是自由逃逸，而是 `PDEC/ColumnCRT` 型非零频率缺陷。

在 sparse 分支中，`(HLC-10)` 逐行给出大量几乎单点的高 lcm 单元。若这些行不能形成
`PDEC/ColumnCRT` 持久频率，则每个坏行必须作为 `SAE` 单窗逃逸处理；其可用约束为：

1. 单元容量 `(HLC-5)`；
2. 左右夹逼唯一相位 `(HLC-3)`；
3. 尾标签 `ell` 与互补商 `m` 的唯一分解；
4. 端点、镜像、列见证或 cofactor 低模投影。

因此高 `R(c)` 分支已经被压成严格二分：

```text
HighLCM mass
=> Persistent-HLC nonzero CRT/Fourier defect
   or Sparse-HLC single-window escape.
```

这一步仍不证明两个出口不可能；它证明的是高 `lcm` 分支不能再作为 KLS-window
参数漏洞存在，必须进入已有最终出口体系。

## 7. 当前闭合状态

本文实际证明：

1. 高 lcm 单元在一行内的容量 `(HLC-5)`；
2. 高 lcm 大质量必转化为大量稀疏激活单元 `(HLC-10)`；
3. 该分支不能被低模 KLS-window 主估计自动覆盖；
4. 大质量高 `lcm` 逃逸必进入 `Persistent-HLC` 或 `Sparse-HLC` 二分；
5. 因而必须作为 `PDEC/ColumnCRT` 非零频率缺陷或 `SAE` 单窗逃逸列入最终审稿义务。

本文尚未证明：

```text
Persistent-HLC 与 Sparse-HLC 两个出口都不可能发生。
```

下一步若继续攻该分支，应证明大量稀疏高 lcm 单元必产生端点/ColumnCRT/cofactor 结构矛盾，
或建立 persistent/sparse 二分的最终排斥定理。
