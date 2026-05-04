# EDA-BK：Bonferroni 下界失败到端点 CRT 缺陷的桥接

**状态：** `endpoint_defect_bridge_proved_exclusion_still_open`

本文继续攻击 `EDA-Dual` 的下一窄接口。核心目标不是直接证明 `S_K>0`，而是证明：
若某个变量阶 Bonferroni 下界不能给出正余量，则失败必须表现为一个显式的端点锯齿型
CRT 缺陷。这使后续可直接接入 `PDEC/SAE`。

## 1. 计数对象

固定奇素数 `p`，令

\[
H=p-1,\qquad I_{p,x}=\{px+1,\ldots,px+H\},\qquad 1\le x\le p.
\tag{EBK-1}
\]

令 `M_{<p}` 为所有 `<p` 素数之积。对 squarefree `d|M_{<p}`，定义

\[
A_d(x)=\#\{n\in I_{p,x}:d\mid n\}.
\tag{EBK-2}
\]

对奇数 `K`，Bonferroni 下界可写为

\[
S_K(p,x)=
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K}}
(-1)^{\omega(d)}A_d(x).
\tag{EBK-3}
\]

这是前文逐点形式的同一个量，因为每个 `n` 被它的 squarefree 小素因子子集计数。

## 2. 主项与端点锯齿项

对任意 `d`，有精确恒等式

\[
A_d(x)=
\left\lfloor {px+H\over d}\right\rfloor
-\left\lfloor {px\over d}\right\rfloor
={H\over d}+\varepsilon_d(x),
\tag{EBK-4}
\]

其中

\[
\varepsilon_d(x)=
\left\{ {px\over d}\right\}
-\left\{ {px+H\over d}\right\},
\qquad -1<\varepsilon_d(x)<1.
\tag{EBK-5}
\]

因此

\[
S_K(p,x)=H\,G_K(p)+E_K(p,x),
\tag{EBK-6}
\]

其中

\[
G_K(p)=
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K}}
{(-1)^{\omega(d)}\over d},
\tag{EBK-7}
\]

\[
E_K(p,x)=
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K}}
(-1)^{\omega(d)}\varepsilon_d(x).
\tag{EBK-8}
\]

`G_K` 只依赖于 `<p` 素数集合；`E_K` 是全部行相位信息，且完全由端点
`px` 与 `px+H` 在各个 squarefree 模 `d` 下的分数部分决定。

## 3. 桥接定理

**定理 EBK-Defect Bridge.**  
设 `K` 为奇数且 `G_K(p)>0`。若某个早期行满足

\[
S_K(p,x)\le0,
\tag{EBK-9}
\]

则必有

\[
E_K(p,x)\le -H\,G_K(p).
\tag{EBK-10}
\]

特别地，若早期对角避让失败，即 `U_p(x)=0`，则对每个奇数 `K` 都有
`S_K(p,x)\le0`，从而在任意满足 `G_K(p)>0` 的阶数上产生 `(EBK-10)` 的负端点
CRT 缺陷。

**证明。**  
由 `(EBK-6)`，

\[
E_K(p,x)=S_K(p,x)-H\,G_K(p).
\]

若 `S_K(p,x)<=0` 且 `G_K(p)>0`，则直接得到 `(EBK-10)`。早期避让失败时
`U_p(x)=0`，而奇数阶 Bonferroni 给出 `S_K(p,x)<=U_p(x)`，故同样适用。证毕。

## 4. 低模投影解释

写周期 Bernoulli 锯齿函数

\[
B_1(t)=\{t\}-{1\over2}.
\tag{EBK-11}
\]

则

\[
\varepsilon_d(x)=
B_1\!\left({px\over d}\right)
-B_1\!\left({px+H\over d}\right).
\tag{EBK-12}
\]

所以 `(EBK-10)` 不是普通平均失败，而是一个带符号端点投影：

```text
left endpoint px 与 right endpoint px+H
在大量 squarefree 小模 d 上出现同向负偏移。
```

这正是 `PDEC/SAE` 可利用的对象：若这种偏移在许多行持续出现，则形成 persistent
Fourier/CRT defect；若只在少数行出现，则进入 sparse local escape。

## 5. 当前剩余接口

本步已闭合的是：

```text
S_K<=0  =>  explicit negative endpoint defect.
```

尚未闭合的是：

```text
explicit negative endpoint defect cannot occur for all 1<=x<=p
```

下一步可攻目标有两条：

1. **变量阶正主项。** 选择 `K=K(p)`，保证 `G_K(p)` 为正且足够大；
2. **缺陷排斥。** 证明满足 `(EBK-10)` 的行集合若覆盖全部候选坏行，则必触发
   `PDEC/SAE`，而后者已进入既有证书体系。

因此 `EDA-BK` 的当前最小硬点被压缩为：

```text
G_K-positive ledger + endpoint defect exclusion.
```

