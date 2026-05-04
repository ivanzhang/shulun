# EDA-LowMod：端点 CRT 缺陷的低模证书路线

**状态：** `lowmod_certificate_formalized_global_exclusion_open`

本文专攻 `EDA-BK` 二分后的第一出口：

```text
LowMod endpoint CRTDefect.
```

目标是把它从“命名出口”升级为可计算、可审稿的证书对象。结论是：低模出口已经可以精确写成
有限相位坏集命题；若坏集不命中早期对角段，则该出口被排除。全局剩余是给出统一的坏集排斥
或 Fourier/PDEC 上界。

## 1. 低模端点函数

固定奇素数 `p`，令 `H=p-1`。取一个 squarefree cutoff `D`，并考虑

\[
\mathcal D_{p,D}=\{d:\ d\mid M_{<p},\ d\le D\}.
\tag{LM-1}
\]

定义低模端点锯齿函数

\[
F_{p,D}(x)=
\sum_{d\in\mathcal D_{p,D}}
\mu(d)
\left(
\left\{ {px\over d}\right\}
-
\left\{ {px+H\over d}\right\}
\right).
\tag{LM-2}
\]

这是 `EDA-BK` 中 `E_{\le D}` 的全阶低模版本；若变量阶 `K_*(p)` 大于所有
`\omega(d)`，则它与 `E_{\le D}` 完全一致。对实际 `D<p`，该条件自动满足，只要
`K_*(p)` 不小于 `max_{d<=D}\omega(d)`。

## 2. 阈值坏集

令

\[
\Lambda_p=(p-1)G_{K_*}(p)>0
\tag{LM-3}
\]

为上一节 `EDA-BK` 的正主项阈值。给定尾预算 `0\le T<\Lambda_p`，定义

\[
A_p(T)=\Lambda_p-T.
\tag{LM-4}
\]

低模坏行集合为

\[
\mathcal B_{p,D,T}=
\{1\le x\le p:\ F_{p,D}(x)\le -A_p(T)\}.
\tag{LM-5}
\]

由 `EDA-BK` 二分，若 `EDA(p)` 失败且尾项满足 `|E_{>D}(p,x)|\le T`，则

\[
x\in \mathcal B_{p,D,T}.
\tag{LM-6}
\]

因此：

**定理 LM-Cert.**  
若存在 `D,T` 使

\[
\mathcal B_{p,D,T}=\varnothing,
\tag{LM-7}
\]

则任何 `EDA(p)` 反例都必须进入 `Tail/Core concentration` 分支。

**证明。**  
这是 `EDA-BK` 低模/尾项二分的直接逆否命题。若反例不进入 Tail，则必须满足
`F_{p,D}(x)\le -A_p(T)`，即落入 `\mathcal B_{p,D,T}`。若坏集为空，矛盾。证毕。

## 3. 相位形式

令

\[
Q_{p,D}={\rm lcm}\{d:\ d\in\mathcal D_{p,D}\}.
\tag{LM-8}
\]

由于 `p` 与 `Q_{p,D}` 互素，`x\mapsto px mod Q_{p,D}` 是单位旋转。函数
`F_{p,D}(x)` 只依赖于 `x mod Q_{p,D}`。因此可定义相位坏集

\[
B_{p,D,T}=
\{a\in\mathbb Z/Q_{p,D}\mathbb Z:\ F_{p,D}(a)\le -A_p(T)\}.
\tag{LM-9}
\]

低模出口等价于：

\[
\{1,\ldots,p\}\cap B_{p,D,T}\ne\varnothing
\tag{LM-10}
\]

其中交集通过 `x mod Q_{p,D}` 理解。

这就是 `PDEC` 可作用的位置：坏集若在很多相邻素数或许多窗口上持续出现，则其指示函数必须
在某个低模非零频率上产生可检测偏差；若只孤立出现，则转入 `SAE`。

## 4. 固定低模的量级排除

低模函数还有一个直接量级界。对 `d>1`，

\[
-1<
\left\{ {px\over d}\right\}
-
\left\{ {px+H\over d}\right\}
<1.
\tag{LM-11}
\]

因此

\[
|F_{p,D}(x)|
\le
|\mathcal D_{p,D}|-1.
\tag{LM-12}
\]

记

\[
N_D(p)=|\mathcal D_{p,D}|.
\tag{LM-13}
\]

**定理 LM-FixedD.**  
若

\[
N_D(p)-1<\Lambda_p-T,
\tag{LM-14}
\]

则 `\mathcal B_{p,D,T}` 为空，低模出口被排除。

**证明。**  
若 `x` 落入低模坏集，则 `F_{p,D}(x)<=-(\Lambda_p-T)`，故
`|F_{p,D}(x)|>=\Lambda_p-T`。这与 `(LM-12)` 和 `(LM-14)` 矛盾。证毕。

该定理给出关键量级差：

```text
固定或缓慢增长的低模端点项 = O(N_D)
正主项阈值 Lambda_p ≈ p/log p。
```

所以 `LowMod` 真正危险只可能来自 `D` 随 `p` 增长过快，或来自尾项预算 `T` 过接近
`\Lambda_p`。这把主压力自然推向 Tail/Core 分支。

## 5. Fourier/PDEC 证书形式

设

\[
1_{B}(a)
\]

是坏相位指示函数，`Q=Q_{p,D}`。若早期对角段命中坏集，则

\[
\sum_{x=1}^{p}1_B(x)>0.
\tag{LM-15}
\]

把 `1_B` 展开为有限 Fourier 级数：

\[
1_B(x)=\beta+\sum_{0<h<Q}\widehat B(h)e^{2\pi i h x/Q},
\qquad
\beta={|B|\over Q}.
\tag{LM-16}
\]

若 `\beta p<1` 且所有非零频率满足

\[
\left|\sum_{0<h<Q}\widehat B(h)
\sum_{x=1}^{p}e^{2\pi i h x/Q}\right|
<1-\beta p,
\tag{LM-17}
\]

则 `(LM-15)` 不可能成立，低模出口被排斥。

这给出一个完全有限的 `PDEC-Cert`：

```text
输入：Q, B, p；
验证：密度项 beta p 与非零 Fourier 项总和严格小于 1。
```

若 `(LM-17)` 失败，则失败本身就是 `PDEC`：坏相位集在非零频率上与早期对角段发生强相关。

## 6. 当前硬点

本步闭合的是：

```text
LowMod branch
=> finite bad phase set B_{p,D,T}
=> either LM-Cert excludes it, or Fourier/PDEC defect is explicit.
```

尚未闭合的是：

1. 找到全局可用的 `D,T`，使 `Tail/Core` 可吸收且 `B_{p,D,T}` 可排斥；
2. 对无限素数族证明 Fourier/PDEC 排斥 `(LM-17)`，或把失败统一送入现有 `PDEC/SAE` 证书体系；
3. 与 Tail/Core 分支同步分配预算，避免低模证明与尾项证明各自消耗同一份余量。

因此下一步最窄任务是：

```text
LowMod-PDEC-Audit:
measure B_{p,D,T}, its early hits, and its low-frequency mass.
```

## 7. 首轮审计事实

脚本：

```text
experiments/prime_matrix_eda_lowmod_pdec_audit.py
```

命令：

```text
python3 experiments/prime_matrix_eda_lowmod_pdec_audit.py --selected 23,101,499,997 --D 60 --tail-frac 0.5
```

输出摘要：

| p | D | `Lambda` | threshold | min `F_{p,D}` | bad rows |
|---:|---:|---:|---:|---:|---:|
| 23 | 60 | 3.762526 | -1.881263 | -2.823566 | 1 |
| 101 | 60 | 12.031729 | -6.015865 | -4.624765 | 0 |
| 499 | 60 | 44.715259 | -22.357629 | -7.091332 | 0 |
| 997 | 60 | 80.722368 | -40.361184 | -8.182664 | 0 |

命令：

```text
python3 experiments/prime_matrix_eda_lowmod_pdec_audit.py --selected 23,101,499,997 --D 100 --tail-frac 0.5
```

输出摘要：

| p | D | `Lambda` | threshold | min `F_{p,D}` | bad rows |
|---:|---:|---:|---:|---:|---:|
| 23 | 100 | 3.762526 | -1.881263 | -3.250232 | 1 |
| 101 | 100 | 12.031729 | -6.015865 | -7.113153 | 2 |
| 499 | 100 | 44.715259 | -22.357629 | -7.503504 | 0 |
| 997 | 100 | 80.722368 | -40.361184 | -6.007007 | 0 |

审计含义：

1. 对中大样本，在 `T=Lambda/2` 的预算下，低模坏集通常不命中早期对角段；
2. 这说明若反例存在，主要压力更可能在 `Tail/Core concentration`，而不是小 `D` 低模端点；
3. 小素数 `p=23,101` 的低模坏行存在，但这些行并非真实零行，说明低模负异常只是必要压力之一，
   还必须结合 Tail/Core 或精确 `U_p(x)`；
4. 固定低模的形式上界已经由 `LM-FixedD` 给出：
   \[
   |F_{p,D}(x)|\ll_D 1
   \tag{LM-18}
   \]
   并与
   \[
   \Lambda_p\asymp {p\over \log p}
   \tag{LM-19}
   \]
   比较。若 `D` 固定或缓慢增长，则 LowMod 分支对充分大 `p` 自动排除，剩余完全压到
   Tail/Core 吸收与有限小 `p` 证书。
