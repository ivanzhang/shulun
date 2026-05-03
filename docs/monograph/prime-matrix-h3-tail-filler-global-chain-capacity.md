# H3 尾补洞全局链容量硬攻

**状态：** `global_chain_capacity_reduction_proved_final_edge_capacity_open`

本文不转换命题，只继续攻击 H3/行命题当前唯一闭合目标的尾补洞全局拼接硬障碍：

```text
局部 2/4/6 rough 短差值互质单元能否沿一个坏行的 H3 候选链全局拼满？
```

上一篇 `prime-matrix-h3-tail-filler-rigidity-hardcore.md` 已证明局部刚性。本文把这些局部刚性
压成全局链容量公式：若尾补洞真的拼满，则必须产生足够多的相邻边证书和三连端点证书。
因此最后硬点不再是模糊的“尾部很多”，而是下面两个显式容量不等式。

## 1. 链图模型

令

\[
A=\{a_1<a_2<\cdots<a_N\}
\]

为固定 `q` 行窗口中的 H3 六轮候选链。相邻差值满足

\[
a_{j+1}-a_j=\delta_j\in\{2,4\},
\qquad
a_{j+2}-a_j=6 .
\tag{GCC-1}
\]

给定 cutoff `y<p`，称 `a_j` 被尾补洞解释，是指

\[
a_j=\ell_j m_j,\qquad
y<\ell_j=P^-(a_j)\le p,\qquad P^-(m_j)\ge \ell_j .
\tag{GCC-2}
\]

尾补洞全局拼接假设是 `(GCC-2)` 对某个连续子链

\[
B=\{a_u,a_{u+1},\ldots,a_v\},\qquad K=v-u+1,
\]

逐点成立。整行尾补洞是 `B=A` 的特殊情形；小骨架剥离后的尾补洞，则对每个连续剩余洞块分别应用。

## 2. 相邻边证书

对 `delta in {2,4}` 定义相邻边证书集合

\[
\mathcal E_\delta(B;y)=
\{(j,\ell,r):
u\le j<v,\ a_{j+1}-a_j=\delta,\ 
\ell=P^-(a_j)>y,\ r=P^-(a_{j+1})>y\}.
\tag{GCC-3}
\]

若 `B` 被尾补洞拼满，则每条相邻边给出一个证书，因此

\[
|\mathcal E_2(B;y)|+|\mathcal E_4(B;y)|=K-1 .
\tag{GCC-4}
\]

更重要的是，局部互质刚性给出标签层面的注入约束。若两条边使用同一个有序标签对
`(ell,r)` 和同一个差值 `delta`，则对应起点 `n` 同时满足

\[
n\equiv0\pmod{\ell},\qquad n\equiv-\delta\pmod r .
\tag{GCC-5}
\]

由于 `gcd(ell,r)=1`，起点落在模 `ell r` 的唯一剩余类中。所以在任意长度不超过 `q+4`
的行窗口中，

\[
\#\{n\in B:n\equiv0\pmod{\ell},\ n+\delta\equiv0\pmod r\}
\le
1+\left\lfloor {q+4\over \ell r}\right\rfloor .
\tag{GCC-6}
\]

特别地，若

\[
y>\sqrt{q+4},
\tag{GCC-7}
\]

则每个有序标签对 `(ell,r,delta)` 在该行内最多贡献一条相邻边。

## 3. 三连端点证书

对任意三连 `a_j,a_{j+1},a_{j+2}`，端点差恒为 `6`。定义

\[
\mathcal T(B;y)=
\{(j,\ell,r):
u\le j\le v-2,\ 
\ell=P^-(a_j)>y,\ r=P^-(a_{j+2})>y\}.
\tag{GCC-8}
\]

若 `B` 被尾补洞拼满，则

\[
|\mathcal T(B;y)|=K-2 .
\tag{GCC-9}
\]

同理，固定有序端点标签对 `(ell,r)` 时，三连起点满足

\[
n\equiv0\pmod{\ell},\qquad n\equiv-6\pmod r ,
\tag{GCC-10}
\]

从而

\[
\#\{n\in B:n\equiv0\pmod{\ell},\ n+6\equiv0\pmod r\}
\le
1+\left\lfloor {q+6\over \ell r}\right\rfloor .
\tag{GCC-11}
\]

若 `y>sqrt(q+6)`，每个有序端点标签对在该行内最多贡献一个三连端点证书。

这把“连续拼接”变成了比单点尾标签计数更强的二阶容量问题：不仅要有足够多的尾点，还要有
足够多的兼容相邻边和兼容三连端点。

## 4. 高 cutoff 下的半素数化

若

\[
y>q^{2/3},
\tag{GCC-12}
\]

则每个满足 `(GCC-2)` 的 `a_j<q^2` 必为双粗半素数

\[
a_j=\ell_j r_j,
\qquad
y<\ell_j\le r_j<q^2/\ell_j .
\tag{GCC-13}
\]

证明很短：若 `m_j` 不是素数，则 `m_j` 至少含两个不小于 `ell_j` 的素因子，于是
`a_j>=ell_j^3>y^3>q^2`，矛盾。故 `m_j` 为素数。

因此在 `y>q^{2/3}` 的层面，尾补洞全局拼接等价于把一个六轮候选连续链全部写成平衡双粗半素数链：

\[
\ell_{j+1}r_{j+1}-\ell_jr_j\in\{2,4\},\qquad
\ell_{j+2}r_{j+2}-\ell_jr_j=6 .
\tag{GCC-14}
\]

这是当前真正的硬核，不再含“小因子可重复覆盖”的退路。

## 5. 全局容量判据

定义实际兼容边容量

\[
\mathrm{EdgeCap}(B;y)=
\sum_{\delta\in\{2,4\}}
\#\{j:u\le j<v,\ a_j,a_{j+1}\ \text{均满足 }(GCC\text{-}2)\},
\tag{GCC-15}
\]

以及实际兼容三连容量

\[
\mathrm{TriCap}(B;y)=
\#\{j:u\le j\le v-2,\ a_j,a_{j+1},a_{j+2}\ \text{均满足 }(GCC\text{-}2)\}.
\tag{GCC-16}
\]

若 `B` 被尾补洞拼满，则必有

\[
\mathrm{EdgeCap}(B;y)=K-1,\qquad
\mathrm{TriCap}(B;y)=K-2 .
\tag{GCC-17}
\]

所以任一严格上界

\[
\mathrm{EdgeCap}(B;y)<K-1
\tag{GCC-18}
\]

或

\[
\mathrm{TriCap}(B;y)<K-2
\tag{GCC-19}
\]

都直接排除尾补洞全局拼接。

这就是当前唯一闭合目标的最窄形式。它仍然是原 `Square-root Defect Exclusion` 的内部命题：
不是改证另一个命题，而是把“尾标签/双粗点不能整行补洞”写成相邻边和三连容量不等式。

## 6. 为什么普通单点容量还不够

单点尾容量只估计

\[
\#\{a_j\in B: P^-(a_j)>y,\ P^-(a_j)\le p\}.
\]

在平方根短区间尺度，这正落在线性筛 `u=2` 的奇偶障碍边界：素数与双粗半素数无法由普通一维筛
分开。因此单点容量可以接近需要的量级，不能直接闭合。

边容量和三连容量加入了额外结构：

1. 相邻差必须是 `2/4`；
2. 二步差必须是 `6`；
3. 相邻和二步端点的大因子族两两互斥；
4. 同一有序标签对在 `y>sqrt(q+6)` 时不能在一行内复用；
5. 在 `y>q^{2/3}` 时，所有尾点退化为双粗半素数点。

这些条件不是平均筛法条件，而是方阵斜线覆盖和 CRT 相位的真实结构约束。

## 7. 当前剩余的单点硬核

本文实际闭合了从局部刚性到全局容量判据的推导。剩余的唯一硬核已经压成：

```text
H3 Tail Edge/Triple Capacity Inequality.
For every adjacent p<q, every H3 row window and an admissible high cutoff y,
every tail-filled continuous block B satisfies
EdgeCap(B;y)<|B|-1 or TriCap(B;y)<|B|-2,
unless the row produces a named PDEC/ColumnCRT/endpoint/cofactor defect.
```

若该不等式被证明，则尾补洞全局拼接被排除，进而补齐 `Square-root Defect Exclusion` 的尾分支。
若无法证明，则主稿仍必须保持条件闭合状态。

## 8. 下一步最小攻坚面

下一步不应再回到平均尺度或有限模板，而应直接证明下列三出口之一：

1. **Edge capacity upper bound**：相邻 `2/4` 双粗半素数边数严格少于连续洞块所需边数；
2. **Triple capacity upper bound**：`2/4/6` 三连双粗半素数单元严格少于连续洞块所需三连数；
3. **Defect forcing**：若上述边/三连容量达到满链量级，则兼容边的标签对、互补商或端点相位产生
   非零 Fourier/CRT 缺陷，从而进入既有 `PDEC/ColumnCRT/endpoint/cofactor` 出口。

这三项是同一个硬障碍的不同投影，不能再拆成新的证明目标来替代原命题。
