# DLS13 低模出口的大尺度自动排除

**状态：** `dls13_lowmod_fixed_D_exclusion_conditional_on_main_gap`

本文继续专攻 `DLT-LowMod`。核心观察：

```text
固定 D 时，E_{<=D}(p) 是有界端点函数；
若主量与高标签容量之间有 c p/log p 级正间隙，
则 LowMod-Bad 不可能在大 p 发生。
```

这把低模出口压成一个明确的主量间隙条件。

## 1. 固定低模端点的绝对界

由

\[
E_{\le D}(p)=
\sum_{\substack{d\mid M_y\\d\le D}}\mu(d)
\left(N_d(p)-{p-1\over d}\right),
\tag{LAX-1}
\]

且任意残基在长度 `p-1` 区间中的计数满足

\[
\left|N_d(p)-{p-1\over d}\right|<1,
\tag{LAX-2}
\]

得到

\[
|E_{\le D}(p)|\le A(D),
\qquad
A(D):=\#\{d\le D:d\ \text{squarefree}\}.
\tag{LAX-3}
\]

更精确地，可只数 `d|M_y`，但 `(LAX-3)` 已足够说明量级。

## 2. 主量间隙条件

令

\[
G_y(p):=(p-1)V_y-C_y(p).
\tag{LAX-4}
\]

失败阈值为

\[
T_y(p)=C_y(p)-(p-1)V_y=-G_y(p).
\tag{LAX-5}
\]

若存在常数 `c>0` 和阈值 `p_0(D,theta,c)`，使

\[
G_y(p)\ge c{p\over\log p}
\quad(p\ge p_0),
\tag{LAX-6}
\]

并且

\[
A(D)<\theta c{p\over\log p},
\tag{LAX-7}
\]

则

\[
E_{\le D}(p)>-\theta G_y(p)=\theta T_y(p),
\tag{LAX-8}
\]

所以 `LowMod-Bad(D,theta)` 不发生。

**证明。**  
由 `(LAX-3)` 得 `E_{<=D}(p)>=-A(D)`。结合 `(LAX-7)` 得
`E_{<=D}(p)>-\theta c p/log p`。再由 `(LAX-6)` 得
`-\theta c p/log p >= -\theta G_y(p)=theta T_y(p)`。证毕。

## 3. 含义

低模出口不是无限硬点。对任何固定 `D`，只要证明主量间隙

\[
(p-1)V_y-C_y(p)\gg {p\over\log p},
\tag{LAX-9}
\]

则低模坏相位在充分大 `p` 自动消失；小 `p` 可有限验证。

因此 `DLT-LowMod` 的真正剩余不是低模端点本身，而是：

```text
MainGap(2/3):
prove (p-1)V_floor(2p/3) - C_floor(2p/3)(p)
has a positive p/log p lower bound.
```

## 4. 为什么这仍非终局

`MainGap(2/3)` 需要高标签精确容量 `C_y(p)` 的尖锐上界。粗估计

\[
C_y(p)\le 2(\pi(p)-\pi(y))
\tag{LAX-10}
\]

常数太弱，不能保证 `(LAX-9)`。必须使用 `DSC-10` 的第二命中条件：

\[
C_y(p)=\#\{y<q<p\}
+\#\{y<q<p:r_q^2\bmod q\ge q-r_q+1\}.
\tag{LAX-11}
\]

也就是说，下一步应专攻高标签容量的第二命中上界，而不是继续低模端点本身。

## 5. 新最小硬点

当前低模分支已压成：

```text
HCap-2Hit:
bound the number of q in (2p/3,p) for which the fixed phase hits twice.
```

若能证明

\[
C_y(p)\le (1-\eta)(p-1)V_y
\tag{LAX-12}
\]

对某个固定 `eta>0` 成立，则固定 `D` 的 LowMod-Bad 在大尺度自动排除。

本文证明的是条件性排除机制；尚未证明 `HCap-2Hit`。
