# BPN-BK/Selberg 路线严攻稿

**状态：** `strict_reduction_not_closed`

本文把边界相位非覆盖 `BPN(P)` 的最新硬点从固定五阶 `BPN-B5` 升级为
可变阶 `BPN-BK`，并明确普通 Selberg/Brun 权重不能单独证明边界行非空。

## 1. 目标行与符号

令 `P` 为奇素数，边界帽行

\[
I_r=\{(r-1)P+c:1\le c<P\},\qquad 2\le r\le P.
\]

令 `M_{<P}` 为所有 `<P` 素数的乘积，`\omega_P(n)` 为 `n` 的不同 `<P`
素因子个数。`BPN(P)` 等价于

\[
\#\{n\in I_r:\gcd(n,M_{<P})=1\}>0\qquad(2\le r\le P).
\]

由于 `n<P^2`，上式中的幸存数必为素数。因此 `BPN(P)` 本质上是网格短区间素数存在命题。

## 2. 任意奇阶 BK 恒等式

对奇数 `K>=1` 定义

\[
S_K(I_r)=\sum_{n\in I_r}\sum_{j=0}^{K}(-1)^j\binom{\omega_P(n)}j.
\]

组合恒等式

\[
\sum_{j=0}^{K}(-1)^j\binom{m}{j}
=
\begin{cases}
1,&m=0,\\
0,&1\le m\le K,\\
-\binom{m-1}{K},&m\ge K+1
\end{cases}
\]

给出精确公式

\[
S_K(I_r)
=\pi(I_r)
-\sum_{\substack{n\in I_r\\ \omega_P(n)\ge K+1}}
\binom{\omega_P(n)-1}{K}.
\tag{BK-id}
\]

因此奇阶 Bonferroni 下界的本质不是避开素数存在性，而是把问题压缩为：

```text
边界短窗内的素数数目
是否严格压过 CoreK 高重小素因子惩罚。
```

固定五阶是 `K=5` 的特例；可变阶 `K≈c log log P` 只是把 `Core6` 升级为
`CoreK+1`。

## 3. Selberg/Brun 下界筛的边界障碍

边界行长度为 `H=P`，需要筛到 `z=P`。若只用普通区间分布

\[
A_d(I_r)=\frac{H}{d}+O(1),
\]

则总误差要求 level 至多 `D\lesssim H=P`，于是

\[
s=\frac{\log D}{\log z}\le 1.
\]

一维下界筛的正性区间需要 `s>2`。因此标准 Selberg/Brun 非负筛权在该尺度只能给
上界或条件预算，不能单独推出 `I_r` 中存在素数。

这就是当前必须保留的审稿边界：

```text
Selberg upper sieve / nonnegative weights
≠ 边界行非空证明。
```

若要无条件闭合，必须额外证明方阵/CRT 专用的端点缺陷排斥或 CoreK 过密排斥。

## 4. BK 端点缺陷形式

对 squarefree `d|M_{<P}` 记

\[
A_d(r)=\#\{n\in I_r:d\mid n\}
=\left\lfloor\frac{rP-1}{d}\right\rfloor
-\left\lfloor\frac{(r-1)P}{d}\right\rfloor.
\]

于是

\[
A_d(r)=\frac{P-1}{d}
\left\{\frac{(r-1)P}{d}\right\}
-\left\{\frac{rP-1}{d}\right\}.
\]

对截断 level `D` 定义低阶 BK 主项和端点项

\[
V_{K,D}=\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d\le D}}\frac{\mu(d)}d,
\]

\[
E_{K,D}(r)=
\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d\le D}}
\mu(d)\left(
\left\{\frac{(r-1)P}{d}\right\}
-\left\{\frac{rP-1}{d}\right\}
\right).
\]

低阶贡献为

\[
S_{K,\le D}(r)=(P-1)V_{K,D}+E_{K,D}(r).
\]

若 `S_K(r)<=0`，则至少发生一项：

1. `E_{K,D}(r)` 产生异常负端点投影；
2. `d>D` 的高阶乘积尾部吞掉主项；
3. `CoreK+1` 高重桶过密。

第一项就是 `BK-DEC`：

```text
BK-DEC(K,D,r): E_{K,D}(r) < -(P-1)V_{K,D}+budget_tail.
```

它应接入已有的 `Directed Endpoint CRTDefect/Tail-anchor` 桥。

## 5. CoreK 过密出口

对 `\omega_P(n)\ge K+1` 的数，取最小 `K+1` 个 `<P` 素因子的乘积

\[
core_{K+1}(n)=q_1q_2\cdots q_{K+1}.
\]

若高重惩罚

\[
T_K(r)=
\sum_{\omega_P(n)\ge K+1}\binom{\omega_P(n)-1}{K}
\]

压过低阶主项，则按 `core_{K+1}` 分桶后必有一个桶过密。该桶只有两种形态：

```text
小/中 core_{K+1}: 固定核心倍数在长度 P 窗口中过密；
大 core_{K+1}≈n: n 被端点尾锚强制，形成 Tail-anchor。
```

因此 `CoreK-Density-or-TailAnchor` 是 `BPN-BK` 的必要失败出口。

## 6. 当前最小闭合链

严格闭合 `BPN(P)` 需要证明下面的二分链：

```text
假设边界帽存在零行
=> 对选定奇阶 K≈c log log P 有 S_K(r)<=0
=> BK-DEC(K,D,r) 或 CoreK-Density/TailAnchor
=> Directed CRTDefect / Tail-anchor / PDEC-or-SAE
=> 与方阵+CRT 已证刚性排斥矛盾。
```

当前已经完成的是前两步的严格代数化与模型审计；尚未完成的是最后的缺陷出口排斥。

## 7. 审稿结论

`BPN-BK/Selberg` 是比固定五阶更正确的全局路线，但还不是无条件证明。它把剩余硬点
精确压缩为：

```text
BK-DEC 端点缺陷排斥
+ CoreK 高重桶过密排斥。
```

后续不应再把普通 Selberg 上界筛写成存在性证明；必须专攻上述两个缺陷出口。

## 8. BK-DEC 桥接已闭合

补充文档 `prime-matrix-bpn-bk-dec-bridge-proof.md` 已证明确定桥：

```text
边界零行
+ |R_{K,>D}|<=T_{K,D}
+ (P-1)V_{K,D}>T_{K,D}
=> E_{K,D}(r)<=-((P-1)V_{K,D}-T_{K,D})
=> 某个低模块块投影异常
=> Directed Endpoint CRTDefect。
```

证明只用奇阶 Bonferroni 逐点符号、精确端点分解和鸽巢不等式。该桥接现在可视为
严格闭合。剩余硬点随之变窄为两项：

```text
1. 给出可审查的尾项预算 |R_{K,>D}|<=T_{K,D} 且 (P-1)V_{K,D}>T_{K,D}；
2. 排斥由 BK-DEC 触发的 Directed Endpoint CRTDefect，即证明 PDEC-or-SAE。
```

## 9. 尾项预算已改写为尾核心桶二分

补充文档 `prime-matrix-bpn-bk-tail-core-dichotomy.md` 进一步证明：

```text
边界零行
=> BK-DEC
   或 U_{K,D}(r)>T。
```

其中

\[
U_{K,D}(r)=
\#\{(n,d):n\in I_r,\ d|n,\ d|M_{<P},\ \omega(d)\le K,\ d>D\}.
\]

若 `U_{K,D}(r)>T`，任意 dyadic/相位分块都会给出某个
`TailCoreBucket/CoreK-Density` 过密块。因此尾项预算的失败已经不是自由误差，而是
可定位的结构缺陷：

```text
大端点项  -> Directed Endpoint CRTDefect；
大尾项    -> TailCoreBucket/CoreK-Density。
```

当前剩余出口精确为：

```text
Directed Endpoint CRTDefect 排斥；
TailCoreBucket/CoreK-Density 排斥。
```

补充文档 `prime-matrix-bpn-tailcore-corridor-reduction.md` 又把第二项严格几何化：

```text
TailCoreBucket/CoreK-Density
=> Tail-anchor concentration
   或 Distributed corridor saturation。
```

因此当前最小剩余清单更新为：

```text
1. Directed Endpoint CRTDefect 的 PDEC-or-SAE 排斥；
2. Tail-anchor concentration 排斥；
3. Distributed corridor saturation 的 Selberg/CRTDefect 排斥。
```

补充文档 `prime-matrix-bpn-tailanchor-persistence-dichotomy.md` 已将第 2 项并回
`PDEC-or-SAE`：

```text
Tail-anchor concentration
=> SAE-anchor
   或 Persistent Tail-anchor defect
=> SAE 或 Directed CRTDefect。
```

因此当前剩余最小硬点进一步压成：

```text
1. PDEC-or-SAE 排斥；
2. Distributed corridor saturation 的 Selberg/CRTDefect 排斥。
```

补充文档 `prime-matrix-bpn-distributed-corridor-saturation-reduction.md` 已把第 2 项继续拆开：

```text
Distributed corridor saturation
=> High-overlap fixed-core defect
   或 Colored disjoint-corridor budget violation。
```

其中高重叠固定核心缺陷并入 `PDEC-or-SAE`；低重叠部分经区间图着色变成不相交走廊
预算问题。因此当前最小剩余为：

```text
1. PDEC-or-SAE 排斥；
2. Colored disjoint-corridor core-sieve budget / low-mod CRTDefect。
```

补充文档 `prime-matrix-bpn-colored-corridor-core-sieve-budget.md` 已将第 2 项严写为：

```text
Colored corridor violation
=> finite Rankin smooth-core ledger obstruction
   或 low-mod core CRTDefect。
```

这里必须使用 smooth-core Rankin 账本，而不是 rough-number Selberg 下界。于是当前最小剩余
再压缩为：

```text
1. PDEC-or-SAE 排斥；
2. finite Rankin smooth-core ledger 常数闭合；
3. low-mod core CRTDefect 排斥。
```

新增 `prime-matrix-bpn-rankin-ledger-certificate-audit.md` 后，第 2 项已有可执行证书格式。
脚本对给定走廊列表精确计算 smooth-core 数、Rankin 账本和低模相位尖峰。若走廊跨多个
dyadic 尺度，账本使用逐走廊右端 `B_j`：

```text
sum_{d in [A_j,B_j]} sigma(d) (B_j/d)^s。
```

因此下一步攻坚不再是定义账本，而是把正式反例诱导出的走廊列表输入证书，寻找可闭合
常数或明确的 low-mod core CRTDefect。

补充文档 `prime-matrix-bpn-lowmod-core-crtdefect-bridge.md` 已把第 3 项并回
`PDEC-or-SAE`：低模 core residue 尖峰经有限 Fourier 反演给出非零 CRT 模式；
持续出现为 `PDEC`，孤立出现为 `SAE-core`。所以当前独立剩余只剩：

```text
1. PDEC-or-SAE 排斥；
2. finite Rankin smooth-core ledger 常数闭合。
```

补充文档 `prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 已将 `PDEC-or-SAE`
统一成 endpoint/core 共用的低模测试函数二分：

```text
named low-mod defect
=> Persistent Fourier defect
   或 Sparse single-window escape。
```

因此最终剩余可以写得更精确：

```text
1. PDEC exclusion；
2. SAE local escape exclusion；
3. finite Rankin smooth-core ledger constants。
```

补充文档 `prime-matrix-bpn-rankin-ledger-acceptance-theorem.md` 已将第 3 项改成证书验收义务：

```text
每个颜色类证书若满足 Rankin ledger <= allowed budget，
则该颜色类闭合；
不通过者必须触发 low-mod core CRTDefect 或继续细分。
```

因此最终剩余更准确地写为：

```text
1. PDEC exclusion；
2. SAE local escape exclusion；
3. 全部正式着色走廊 Rankin certificates 通过，或失败者进入 PDEC/SAE。
```

## 10. 最终出口验收合约接入

补充文档 `prime-matrix-bpn-final-exit-acceptance-contract.md` 已把上一节三项剩余改写为
明确证书义务：

```text
PDEC-Cert:
  对 persistent 低模缺陷块证明非零 Fourier 上界 U_CRT<L_PDEC；

SAE-Cert:
  对每个 sparse bad window 给出 survivor / lift / higher-defect 三类证书之一；

Rankin certificates:
  对正式着色走廊逐类给出 rankin_budget_pass=true，
  或把失败者登记为 low-mod core CRTDefect 后送入 PDEC/SAE。
```

因此 `BPN-BK/Selberg` 主链当前的精确状态是：

```text
严格归约完成到最终证书层；
最终证书尚未全集提交；
不能标为 BPN(P) 无条件证明。
```

下一步不应再新增等价命名。真正要攻的单点硬核是构造

\[
\mathcal U_{\rm CRT}<\mathcal L_{\rm PDEC}
\]

的非循环上界，或逐个给出孤立坏窗的 `SAE-Cert`。这也是本文与审稿状态表应采用的
最终边界。
