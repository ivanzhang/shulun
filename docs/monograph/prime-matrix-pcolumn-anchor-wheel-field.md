# 第P列锚点层叠轮矛盾场

**状态：** `structural_identity_and_audit_not_a_proof`

本文分析用户提出的新思路：不只对 `P^2±k` 做层叠轮筛，而是把第 `P` 列的每个点都作为锚点，对整行建立层叠轮筛；再与第一行的同余斜线覆盖合成一个全行全列矛盾场。

结论是：这个方向可以严格形式化，而且给出一个全局方程。但第 `P` 列本身全是 `P` 的倍数，不能直接提供素数洞；它提供的是锚点相位 `P(x+1) mod W`，由此决定整行的轮筛骨架。

## 1. 行列锚点坐标

固定奇素数 `P`。第 `x` 行非平凡列为

\[
n_{x,c}=xP+c,\qquad 1\le c<P.
\]

令

\[
y=x+1,\qquad d=P-c.
\]

则

\[
n_{x,c}=P(x+1)-(P-c)=Py-d,\qquad 1\le d<P.
\tag{PAW-1}
\]

这里 `Py` 正是第 `P` 列点：

\[
xP+P=Py.
\tag{PAW-2}
\]

所以每一行都可看成第 `P` 列锚点 `Py` 左侧长度 `P-1` 的短区间。

## 2. 层叠轮骨架恒等式

令

\[
W=\prod_{\ell\in \mathcal L}\ell,\qquad U_W=(\mathbb Z/W\mathbb Z)^\times.
\]

第 `y` 个锚点行在轮 `W` 下的距离骨架为

\[
S_W(P,y)=
\{1\le d<P:\ Py-d\bmod W\in U_W\}.
\tag{PAW-3}
\]

等价地，

\[
d\bmod W\in Py-U_W.
\tag{PAW-4}
\]

第一行是 `x=1,y=2`。因此

\[
S_W(P,y)\equiv S_W(P,2)+P(y-2)\pmod W.
\tag{PAW-5}
\]

这就是“第一行所有数的同余斜线覆盖”与“第 `P` 列每个锚点”的精确连接：所有行的低模骨架，都是第一行骨架沿圆柱方向的平移。

## 3. 第P列互补因子的作用

若某个 `q|W` 且 `q|y`，则 `Py≡0 mod q`。由 `(PAW-1)`，

\[
q\mid Py-d\quad\Longleftrightarrow\quad d\equiv0\pmod q.
\tag{PAW-6}
\]

这说明第 `P` 列互补因子 `y=x+1` 的小素因子，会在本行变成“距离第 `P` 列为 `q` 的倍数”的锚定斜线。

若 `q∤y`，则覆盖距离类为

\[
d\equiv Py\pmod q.
\tag{PAW-7}
\]

所以完整行覆盖可统一写成：

```text
锚因子层 q|y:       d ≡ 0 mod q；
非锚因子层 q∤y:     d ≡ Py mod q。
```

这就是第 `P` 列层叠轮筛与圆柱斜线覆盖的合流点。

## 4. 全局矛盾场方程

对轮 `W`，剩余高素斜线集合为

\[
\mathcal Q_W(P)=\{q<P:\ q\ {\rm prime},\ q\nmid W\}.
\]

在骨架 `S_W(P,y)` 上，剩余高素 `q` 的补洞集合是

\[
C_q(P,y)=
\{d\in S_W(P,y): d\equiv Py\pmod q\}.
\tag{PAW-8}
\]

最终素数洞为

\[
H_W(P,y)=
S_W(P,y)\setminus\bigcup_{q\in\mathcal Q_W(P)}C_q(P,y).
\tag{PAW-9}
\]

若 `d in H_W(P,y)`，则 `Py-d` 没有任何 `<P` 素因子。对 `2<=y<=P+1` 有

\[
P<Py-d<P^2+P,
\]

且 `Py-d` 不被 `P` 整除。因此 `Py-d` 必为素数。于是行命题可写成统一方程：

\[
\boxed{
|S_W(P,y)|
>
\left|\bigcup_{q\in\mathcal Q_W(P)}C_q(P,y)\right|
}
\qquad 2\le y\le P+1.
\tag{PAW-10}
\]

若 `(PAW-10)` 失败，则剩余高素斜线完全覆盖了一个由第一行平移而来的轮骨架。这种失败不再是普通覆盖问题，而是：

```text
一个第一行轮骨架平移块
被高素单残基斜线完全覆盖。
```

这正是可送入 `PDEC/SAE/ColumnCRT` 的全局矛盾场对象。

## 5. 审计结果

新增脚本：

```text
experiments/prime_matrix_pcolumn_anchor_wheel_field_audit.py
```

生成：

```text
docs/pcolumn_anchor_wheel_field_audit_20260506.md
docs/pcolumn_anchor_wheel_field_audit_20260506.json
```

样本 `P=101,499,997,2003,5003` 与 `W=30,210,2310,30030` 的结果：

| P | W=30030 shift failures | W=30030 min skeleton | W=30030 min prime holes | W=30030 max filler ratio |
|---:|---:|---:|---:|---:|
| `101` | `0` | `16` | `7` | `0.588235` |
| `499` | `0` | `92` | `29` | `0.691489` |
| `997` | `0` | `187` | `54` | `0.720207` |
| `2003` | `0` | `379` | `113` | `0.706494` |
| `5003` | `0` | `955` | `260` | `0.729448` |

对全部测试行与轮，`shift_identity_failures=0`。这核验了 `(PAW-5)` 的圆柱平移恒等式。

同时最薄素数洞行仍保留大量素数洞。例如 `P=5003,W=30030` 的最薄行：

```text
x=4980, y=4981,
skeleton=961,
prime holes=260,
filler=701,
filler ratio=0.729448。
```

注意该行在 `W=30030` 的第 `P` 列互补因子没有小锚因子。这说明“第 `P` 列互补因子富含小素因子”不是全局证明所必需；真正全局适用的是锚残基 `Py mod W` 的平移方程。

## 6. 动态提升轮升级

固定轮只证明了圆柱平移刚性。进一步把轮提升到

\[
Y=P^{0.43},\qquad \mathcal P_Y=\prod_{\ell\le Y}\ell
\]

后，定义

\[
S_Y(P,y)=\{1\le d<P:(Py-d,\mathcal P_Y)=1\},
\]

以及剩余高素命中总量

\[
T_Y(P,y)=
\sum_{P^{0.43}<q<P}
\#\{d\in S_Y(P,y):d\equiv Py\pmod q\}.
\]

若

\[
T_Y(P,y)<|S_Y(P,y)|,
\tag{PAW-11}
\]

则该行必有素数洞。严格原因是：未被低素和剩余高素命中的 `Py-d` 没有任何 `<P` 素因子，且不被 `P` 整除；又有 `P<Py-d<P^2+P`，若合成则最小素因子小于 `P+1`，矛盾。

新增文件：

```text
docs/monograph/prime-matrix-pcolumn-anchor-dynamic-capacity.md
experiments/prime_matrix_pcolumn_anchor_dynamic_capacity_audit.py
```

样本结果：

| P | cutoff | min margin | max T/S | min model/sqrt | max D+/sqrt | min prime holes |
|---:|---:|---:|---:|---:|---:|---:|
| 5003 | 38 | 46 | 0.937922 | 5.066922 | 3.415103 | 260 |
| 10007 | 52 | 98 | 0.929446 | 6.602875 | 4.026284 | 498 |
| 20011 | 70 | 112 | 0.956857 | 8.802969 | 6.659539 | 929 |

这里 `D+=max(0,T-HS)`，`H=sum_{P^0.43<q<P}1/q`。第 `P` 列版本的最紧容量行出现了新的“近截止锚峰”：`y` 接近 cutoff 后第一批高素，例如 `P=20011,y=71` 的 top labels 为 `71,73,79`。但这些行仍有大量真实素数洞，说明近截止高命中同时带来强重叠；若反例要利用它，必须进入 `NearCutoff Anchor Spike / PDEC / SAE / ColumnCRT` 出口。

## 7. 对闭合目标的意义

这条路线把前面的平方端点模型推广为：

```text
P^2-k:       y=P,   anchor=P^2；
P^2+k:       y=P+1, anchor=P(P+1)；
任意第 x 行: y=x+1, anchor=Py。
```

因此 `P^2±k mod 30/210/2310/...` 不是孤立现象，而是 `Py-d mod W` 的全行全列锚点筛的两个端点切片。

当前可攻硬点更新为：

```text
PColumn Anchor-Wheel Field:
  所有行的低模骨架都是第一行骨架的圆柱平移；
  动态提升到 Y=P^0.43 后，若某个平移骨架被剩余高素斜线完全覆盖，
  则必须产生以下至少一种缺陷：
    1. 高素补洞容量超预算；
    2. 近截止锚峰低重叠同步；
    3. 新增轮层 Fourier 低维集中，即 new-layer PDEC；
    4. 单窗逃逸 SAE；
    5. 第 P 列锚点位移/ColumnCRT 缺陷。
```

这还不是最终闭合证明，但它给出了用户要的“全局矛盾场方程”：`(PAW-10)` 是统一覆盖-筛除夹击方程，`(PAW-5)` 是它与第一行的圆柱平移连接。
