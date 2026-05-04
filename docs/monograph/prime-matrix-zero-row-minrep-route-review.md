# CRT 最小解 `x>p`：历史路径复盘与闭合路线评审

**状态：** `route_review_minrep_equivalence_closed_exits_open`

本文复盘围绕命题

```text
若 px+1,...,px+p 都被 <=p 的素数覆盖，则最小这样的 x 必大于 p
```

已经取得的结构成果、被排除的误路、最接近闭合的历史路线，以及下一步最优攻坚顺序。

## 1. 已经严格闭合的核心等价链

当前最重要的成果不是一个启发，而是已经严写为可审稿的等价链：

```text
零行乘数 x
<=> 存在完整覆盖 CRT 证书 tau
<=> x 属于 tau 给出的 CRT 残基类
```

具体地，若

\[
Z_p=\{x\ge1:\forall 1\le k<p,\exists q<p,\ q\mid px+k\},
\]

则

\[
Z_p=\bigcup_\tau \{x\ge1:x\equiv r_\tau\pmod {D_\tau}\},
\qquad
X_0(p)=\min_\tau r_\tau^+.
\]

同标签相容条件也已经精确闭合：

\[
\tau(a)=\tau(b)=q\quad\Longleftrightarrow\quad a\equiv b\pmod q.
\]

因此目标 `X_0(p)>p` 等价于：

```text
每个完整覆盖证书 tau 的最小正代表 r_tau^+ 都大于 p。
```

另一方面，在 `1<=x<=p` 时，若某个 `px+k` 没有 `<=p` 的素因子，则它必为素数。因此

\[
X_0(p)>p
\Longleftrightarrow
\forall 1\le x\le p,\quad
\pi(px+p-1)-\pi(px)>0.
\]

这说明首零行对角屏障同时是：

1. CRT 证书最小代表屏障；
2. `p` 对齐短区间素数屏障；
3. 精确筛余正性命题 `U_p(x)>0`。

## 2. 已经排除或校正的误路

### 2.1 不是连续 `p`-光滑数问题

零行只要求每个 `px+k` 至少有一个 `<=p` 的素因子，不要求所有素因子都 `<=p`。
因此不能用 Størmer--Lehmer、Pell 型连续光滑数下界直接证明 `x>p`。

### 2.2 不是完整 CRT 周期无零行

完整周期中零行大量存在；例如 `p=23` 的首个零行乘数是 `x=58`，一编号行为 `59`。
正确命题是：

```text
零行存在，但其首个 CRT 正代表不落入 1<=x<=p。
```

### 2.3 镜像刚性不能直接推出短周期复现

CRT 周期中零行有严格镜像，但镜像只给两端帽约束，不推出行号 `r`、`2r` 或 `2r-1`
的短周期复现。该路线可增强 PDEC/SAE，但不能单独闭合 `X_0(p)>p`。

### 2.4 普通短区间素数定理不足

`x=p` 已要求

\[
\pi(p^2+p-1)-\pi(p^2)>0.
\]

任何一般素数间隔输入若只给 `N^\theta` 且 `theta>1/2`，都不能覆盖长度约 `p=sqrt N`
的窗口。因此必须利用特殊 CRT 对角结构，不能只调用粗短区间定理。

## 3. 已积累的刚性约束

### 3.1 同标签列差刚性

若同一 `q` 覆盖两列 `a,b`，则 `q|b-a`。所以：

```text
q>p/2  => q 至多覆盖 1 列；
q>p/3  => q 至多覆盖 2 列；
q>p/m  => q 至多覆盖 m-1 列。
```

高标签不是自由容量，而是几乎单列补洞。

### 3.2 早期残洞必为素数

在 `1<=x<=p` 的对角区段，未被 `<p` 素数覆盖的数不能是双粗合数，只能是素数。
这消除了“粗数补洞自由度”，也是 EDA 比一般边界零行更硬、更干净的地方。

### 3.3 端点锯齿缺陷刚性

Bonferroni 下界有精确分解

\[
S_K(p,x)=H G_K(p)+E_K(p,x),\qquad H=p-1,
\]

其中 `E_K` 是端点分数部分锯齿和。若某个正主项阶 `K` 下 `S_K<=0`，则必有

\[
E_K(p,x)\le -H G_K(p).
\]

也就是说，反例不是普通覆盖事件，而必须制造强负端点 CRT 缺陷。

### 3.4 正主项阶数存在

已经证明总能选奇数阶 `K_*(p)` 使 `G_{K_*}(p)>0`。因此任何 EDA 反例都进入：

```text
LowMod endpoint CRTDefect
或
Tail/Core concentration。
```

这是目前最强的非循环压缩。

## 4. 历史路径评审

### 路线 A：直接 MinRep 屏障

目标：

```text
对每个完整覆盖证书 tau，证明 r_tau^+>p。
```

优势：

- 完全贴合 CRT 方程组；
- 不直接数素数；
- 能使用高标签单列刚性、低骨架残洞、同余相容性。

主要缺口：

- 证书数量巨大；
- 低骨架可留下很少洞，高标签可通过 CRT 偶然补齐；
- 需要证明“小代表 `x<=p` 无法同时承载所有高标签同余”，目前还缺一个全局可求和的不等式。

当前评价：

```text
概念最本质，但还缺核心全局不等式。
```

### 路线 B：EDA-Dual / Bonferroni-BK

目标：

\[
U_p(x)=\#\{1\le k<p:(px+k,M_p)=1\}>0.
\]

已经完成：

- 精确 Möbius/Bonferroni 计数；
- 五阶身份
  \[
  S_5=U_p-\sum_{\omega_p(n)\ge6}{\omega_p(n)-1\choose5};
  \]
- 样本中 `S_5` 一直正；
- 固定阶风险已识别；
- 变量阶正主项和端点缺陷二分已证明。

主要缺口：

```text
LowMod endpoint CRTDefect 排斥
+ Tail/Core concentration 吸收。
```

当前评价：

```text
这是最接近闭合的主线。
```

原因是它已经把反例压成两个命名出口，而不是面对原始短区间素数存在性。

### 路线 C：PDEC/SAE 出口排斥

目标：

```text
证明所有 persistent 低模缺陷与 sparse 单窗逃逸都不可能。
```

已有基础：

- `PDEC-Cert` 验收形式；
- `SAE-Cert` 验收形式；
- endpoint/core 低模缺陷已统一进 `PDEC-or-SAE`；
- BPN 路线积累了大量相位容量、列残基、Rankin smooth-core 证书经验。

主要缺口：

- EDA 的 LowMod 缺陷需要专门的低模测试函数和上界；
- Tail/Core 分支需要把高模尾项转成已证 Rankin 或 Tail-anchor 预算；
- 现有 PDEC/SAE 体系是验收框架，仍需填 EDA 专用证书。

当前评价：

```text
这是 EDA-BK 的最自然下游，也是最可工程化的闭合接口。
```

### 路线 D：递归剥离 / 壳层下降

目标：

```text
若高阶 q 方阵有零行，则降阶到 p 方阵零行或 seam zero window，
再递归到小阶矛盾。
```

已经完成：

- 相邻壳层中新增非冗余点几乎只剩 `q^2`；
- `q` 零行可降为旧 `p`-筛零窗；
- 零窗二分为完整下层零行或缝合 seam；
- seam guard 吸收可路由到 `SAE/PDEC/ColumnCRT`。

主要缺口：

- seam 通常是主分支，不能直接推出下层方阵内零行；
- 镜像落点变成非零类覆盖，不是原命题零行；
- 仍要排斥 SAE/PDEC/ColumnCRT 出口。

当前评价：

```text
很有结构洞察，但闭合仍回流到 PDEC/SAE。
```

### 路线 E：标准 Selberg/Brun 下界筛

结论：

```text
不能单独闭合。
```

原因是窗口长度 `H≈p`，筛到 `z≈p`，筛维参数 `s=log D/log z` 至多约 `1`，
而一维下界筛正性通常需要 `s>2`。因此 Selberg/Brun 可做上界、尾项、证书预算，
不能直接当作“存在未筛掉数”的证明。

## 5. 最接近闭合的历史路径排序

### 第一优先：`EDA-BK => LowMod/Tail` 出口闭合

当前链条：

```text
EDA 反例
=> U_p(x)=0
=> 奇阶 BK 下界失败
=> 正主项端点缺陷
=> LowMod endpoint CRTDefect 或 Tail/Core concentration
=> PDEC/SAE
```

最小剩余：

1. 对 LowMod 分支构造 EDA 专用 Fourier/PDEC 上界；
2. 对 Tail/Core 分支构造 Rankin smooth-core 或 Tail-anchor 吸收；
3. 把失败者统一回流到 PDEC/SAE。

这是目前最接近“证明闭合”的链条。

### 第二优先：低骨架缺陷 + 高标签 MinRep

策略：

1. 固定低素数骨架 `Q0={2,3,5,...,L}`；
2. 研究早期 `x<=p` 下低骨架残洞 `H_L(x)`；
3. 若残洞太少，说明低模相位异常，进入 PDEC；
4. 若残洞仍多，高标签因单列刚性无法全部补齐；
5. 若高标签强行补齐，则产生大量同余约束，推出 `r_tau^+>p`。

优势是直接攻 MinRep；劣势是还缺统一容量-相位不等式。

### 第三优先：递归剥离作为反例传播辅助

适合用来证明：

```text
若 EDA/MinRep 反例存在，则它不能孤立；
它必须在壳层下降中制造 seam/PDEC/SAE 压力。
```

不宜单独作为主闭合路线，但可增强 SAE 排斥。

## 6. 当前最优攻坚结论

如果目标是证明 `X_0(p)>p`，最有效路线不是继续寻找新等价命题，而是直接补两项：

```text
H1. LowMod endpoint CRTDefect exclusion.
H2. Tail/Core concentration absorption.
```

具体下一步建议：

1. 选定 cutoff `D`，把 `E_{\le D}(p,x)` 写成有限低模相位函数；
2. 证明若 `E_{\le D}` 在某个早期反例行达到阈值，则该行的 `x mod Q` 落入小相位坏集；
3. 对坏集建立 PDEC Fourier 上界，或证明其孤立性进入 SAE；
4. 对 `E_{>D}` 用 Rankin/smooth-core 账本做显式尾界；
5. 若尾界失败，证明失败给出 Tail-anchor 或 core residue 尖峰，再回流 PDEC/SAE。

因此，历史上最接近闭合的路径是：

```text
Full CRT MinRep equivalence
=> EDA-Dual
=> EDA-BK positive-main defect
=> LowMod/Tail dichotomy
=> PDEC/SAE exclusion.
```

该路径保留了 CRT 方程组的本质，又避开了把一般短区间素数猜想当作黑箱的风险。

