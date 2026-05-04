# EDA 对角分割容量路线

**状态：** `diagonal_split_capacity_route_promising_open`

本文继续专攻对角最终硬核。核心观察：

```text
先用低标签 q<=alpha p 覆盖；
若剩余低骨架洞数超过高标签 q>alpha p 的精确固定相位容量，
则对角行必有幸存点，从而 (p^2,p^2+p) 中有素数。
```

这条路线比普通总容量更细，因为高标签容量不是粗略 `ceil(p/q)` 总和，而是使用固定相位
`k≡-p^2 mod q` 在 `[1,p-1]` 中实际出现的次数。

## 1. 定义

固定 `0<alpha<1`，令

\[
y=\lfloor \alpha p\rfloor.
\tag{DSC-1}
\]

低骨架洞集合定义为

\[
H_y(p)=
\{1\le k<p:\forall q\le y,\ q<p,\ q\nmid p^2+k\}.
\tag{DSC-2}
\]

高标签精确容量定义为

\[
C_y(p)=
\sum_{y<q<p}
\#\{1\le k<p:k\equiv -p^2\pmod q\}.
\tag{DSC-3}
\]

## 2. 分割容量判据

**定理 DSC-1（低洞大于高容量则对角闭合）。**  
若

\[
|H_y(p)|>C_y(p),
\tag{DSC-4}
\]

则 `U_p(p)>0`。

**证明。**  
若 `U_p(p)=0`，则每个低骨架洞 `k in H_y(p)` 必须被某个高标签 `q>y` 覆盖，即满足
`k≡-p^2 mod q`。高标签在 `[1,p-1]` 中的全部可覆盖位置总数正是 `C_y(p)`，所以必须有
`|H_y(p)|<=C_y(p)`。这与 `(DSC-4)` 矛盾。证毕。

该判据完全初等且不依赖概率模型。

## 3. 高标签精确容量公式

对 `q>p/2`，写

\[
p=q+r,\qquad 0<r<q.
\tag{DSC-5}
\]

由于

\[
p^2\equiv r^2\pmod q,
\tag{DSC-6}
\]

高标签覆盖列为

\[
k\equiv -r^2\pmod q.
\tag{DSC-7}
\]

在 `[1,p-1]=[1,q+r-1]` 中，该残基出现一次或两次；第二次出现当且仅当

\[
(-r^2\bmod q)+q\le q+r-1.
\tag{DSC-8}
\]

等价于

\[
r^2\bmod q\ge q-r+1.
\tag{DSC-9}
\]

因此当 `alpha>1/2` 时，高标签容量可精确写为

\[
C_y(p)=
\#\{y<q<p\}
+
\#\{y<q<p:r_q^2\bmod q\ge q-r_q+1\},
\quad r_q=p-q.
\tag{DSC-10}
\]

这比粗上界 `2(\pi(p)-\pi(y))` 更尖锐。

## 4. 样本审计

脚本：

```text
experiments/prime_matrix_diagonal_split_capacity_audit.py
```

样本显示 `alpha≈0.66` 起出现稳定正余量：

| p | alpha | low holes | exact high capacity | margin |
|---:|---:|---:|---:|---:|
| 101 | 0.66 | 11 | 10 | 1 |
| 499 | 0.66 | 45 | 33 | 12 |
| 997 | 0.66 | 84 | 58 | 26 |
| 2003 | 0.66 | 138 | 101 | 37 |
| 5003 | 0.66 | 307 | 254 | 53 |
| 10007 | 0.66 | 586 | 464 | 122 |

这说明对角分支不是随机“刚好有素数”，而是低洞数量与高标签精确相位容量之间存在可见余量。

## 5. 真正剩余

DSC 把对角硬核压成两个显式不等式：

1. **低骨架洞下界**
   \[
   |H_{\lfloor\alpha p\rfloor}(p)|\ge L_\alpha(p);
   \tag{DSC-11}
   \]
2. **高标签精确容量上界**
   \[
   C_{\lfloor\alpha p\rfloor}(p)\le R_\alpha(p);
   \tag{DSC-12}
   \]

并要求

\[
L_\alpha(p)>R_\alpha(p).
\tag{DSC-13}
\]

高标签容量上界因 `(DSC-10)` 已经非常具体；更难的是低骨架洞下界 `(DSC-11)`。它仍是
短区间粗剩余下界，但现在只需筛到 `alpha p`，并且右侧容量已经按固定相位削弱。

## 6. 下一步最小硬点

当前最优攻坚点是：

```text
DSC-LowHole(alpha=2/3):
prove |H_floor(2p/3)(p)| exceeds the exact high capacity C_floor(2p/3)(p).
```

若证明该不等式，则对角 `x=p` 分支闭合。再与内部 `x<p` 的 PDL/FactorDescent 分支合并，
才可能推进完整 EDA。

本文不宣称该不等式已全局证明；它给出了目前最具体、最可计算、最接近样本事实的对角闭合接口。
