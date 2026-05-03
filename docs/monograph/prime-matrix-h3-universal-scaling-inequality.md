# H3 通用尺度不等式与缺陷版公式

**状态：** `candidate_universal_inequality_with_defect_routes_not_global_proof`

本文给出当前与数据最吻合、且能接入证明链的通用公式。它不是单纯拟合，而是由三层结构推导：

1. 六轮候选规模 `#A_s=q/3+O(1)`；
2. Mertens/Buchstab 自然粗剩余尺度 `~q/log q`；
3. 若实际余量低于该尺度，则 first-factor partition 必产生小骨架过载、多标签能量或端点相位缺陷。

## 1. 定义

设 `p<q` 为相邻奇素数，`2<=s<=q`。令 `A_s` 为第 `s` 个 `q` 行窗口中完整 3 行的六轮候选集合。定义 H3 余量

\[
M_{H3}(p,s)=\#\{n\in A_s:P^-(n)>p\}.
\]

在 `q^2` 之前，该余量就是 H3 证明链所需的素数幸存数。若 `M_H3(p,s)>0`，则反设的旧 `p`-筛零窗被排除。

## 2. 自然尺度公式

局部筛密度给出

\[
E_{H3}(p,s)
=\#A_s\prod_{5\le \ell\le p}\left(1-\frac1\ell\right).
\]

由 Mertens 乘积，

\[
\prod_{\ell\le p}\left(1-\frac1\ell\right)
\sim {e^{-\gamma}\over \log p}.
\]

去掉 `2,3` 后，

\[
\prod_{5\le \ell\le p}\left(1-\frac1\ell\right)
\sim {3e^{-\gamma}\over \log p}.
\]

又 `#A_s=q/3+O(1)`，故

\[
E_{H3}(p,s)
\sim e^{-\gamma}{q\over \log p}
\sim e^{-\gamma}{q\over \log q}.
\tag{H3-Scale}
\]

这解释了数据中平均余量与 `q/log q` 同阶，且常数约在 `0.5` 量级。

## 3. 数据匹配公式

审计文件：

```text
experiments/prime_matrix_h3_scaling_formula_audit.py
docs/monograph/prime-matrix-h3-scaling-formula-audit.md/json
```

在 `p<=5000` 的全量账本中：

```text
min margin/(q/log q) over all rows = 0.154970... at p=17
c=0.25 eventually holds from p=59
c=0.30 eventually holds from p=113
c=0.33 eventually holds from p=607
c=0.35 eventually holds from p=809
c=0.40 eventually holds from p=2011
tail min ratio p>=331 = 0.300139...
tail min ratio p>=1000 = 0.353739...
tail min ratio p>=2000 = 0.397151...
```

因此当前最稳妥的有限数据候选为：

\[
M_{H3}(p,s)\ge 0.30{q\over \log q}
\qquad(p\ge 113),
\tag{H3-0.30}
\]

更强的尾部候选为：

\[
M_{H3}(p,s)\ge 0.40{q\over \log q}
\qquad(p\ge 2011).
\tag{H3-0.40}
\]

## 4. 为什么该公式不能直接当作证明

`(H3-0.30)` 是平方根长度窗口中的素数下界型陈述。单靠普通无条件短区间素数定理不能推出它；线性筛在 `u=2` 临界也没有正下界。因此正式稿不能写成“由 Mertens 乘积推出”。

正确的理论命题应是缺陷版：

```text
H3 Scaling Defect Inequality.
For some absolute c>0, either
  M_H3(p,s) >= c*q/log q,
or
  SmallSkeletonOverload fires,
or
  ManyLabel-PDEC fires,
or
  Endpoint-SAE/ColumnCRT fires.
```

## 5. 缺陷版的理论推导

若 `M_H3(p,s)<c q/log q`，则 first-factor partition

\[
A_s\setminus \{P^->p\}
=\bigsqcup_{5\le \ell\le p}A_{s,\ell}
\]

覆盖了几乎全部 `A_s`。取 cutoff `y=p^\theta`。

### 5.1 小骨架分支

若

\[
C_y=\#\{n\in A_s:5\le P^-(n)\le y\}
\]

接近 `#A_s`，则有限小首因子在同一 `q` 行窗口中承担接近全覆盖的固定相位负载。这就是

```text
SmallSkeletonOverload(y,K) => Tail/PDEC.
```

### 5.2 多标签分支

若小骨架不过载，则剩余

\[
R_y=\#A_s-C_y
\]

必须由 `ell>y` 覆盖。单个 `ell>y` 至多贡献 `floor(q/ell_+(y))+1` 个点，因此活跃标签数至少为

\[
K_y=\left\lceil {R_y\over \lfloor q/\ell_+(y)\rfloor+1}\right\rceil.
\]

在自然尺度下 `R_y` 约为 `q/log y`，故 `K_y` 至少为 `y/log y` 量级。大量中尾标签同步覆盖同一短窗口，必须表现为低模能量或 ColumnCRT 位移集中。

### 5.3 端点分支

若低模能量估计只因端点取整失败而无法闭合，则失败相位是有限端点相位。稀疏发生归入 `SAE`；持久发生归入 `ColumnCRT`。

## 6. 当前最窄理论义务

要把 `(H3-0.30)` 从数据公式升级为证明，下一步必须补：

1. `SmallSkeletonOverload(y,K)=>Tail/PDEC` 的正式阈值；
2. `K_y\gtrsim y/log y=>ManyLabel-PDEC` 的低模能量下界；
3. 端点损失 `=>SAE/ColumnCRT`；
4. 三分支同一阻断点口径下的不重不漏。

这就是当前最窄硬点的理论层公式：不是直接证明所有短区间有素数，而是证明低于 `c q/log q` 的异常必定触发已命名缺陷场。

## 7. 已证明的全局缺陷二分

新增：

```text
docs/monograph/prime-matrix-h3-global-tail-energy-lemma.md
```

该文件证明一个完全确定性的全局不等式。对任意 cutoff `y`、目标尺度 `B`、能量阈值 `L` 和任意
`d>=2(floor(q/ell_+(y))+1)`，若

\[
M_{H3}(p,s)<B,
\]

则必有

\[
C_y>\#A_s-B-2L
\]

或

\[
E_y(d)>L.
\]

取 `B=c q/log q`、`L=lambda q/log q`，得到：

```text
M_H3 below c q/log q
=> small skeleton overload at level c+2lambda
   or tail-label low-mod energy >= lambda q/log q.
```

这是全局无限通用的缺陷公式。剩余不是组合推导，而是排除这两个缺陷出口。
