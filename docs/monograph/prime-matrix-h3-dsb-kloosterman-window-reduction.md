# H3-DSB 非零频率到 Kloosterman 窗口的归约

**状态：** `kloosterman_window_reduction_proved_external_parameter_check_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把大有符号双线性误差推出为非主角色频率缺陷。本文进一步把同一缺陷改写为加性
Kloosterman 窗口和，明确外部 DI/BFI/KLS-window 能否覆盖时必须逐项核验的参数。

## 1. 从乘法角色回到加性逆元相位

固定夹逼单元 `c`，记

\[
R=R(c),\qquad \rho=\rho(c).
\]

互补商条件为

\[
m\equiv \ell^{-1}\rho\pmod R,
\qquad (\ell,R)=1.
\tag{KWR-1}
\]

等价地，

\[
\ell m\equiv\rho\pmod R.
\tag{KWR-2}
\]

在单位条件下，剩余类指示函数有加性展开

\[
1_{\ell m\equiv\rho\pmod R}
-
{1\over R}1_{(\ell m,R)=1}
=
{1\over R}\sum_{1\le h<R}
e\!\left({h(\ell m-\rho)\over R}\right)
+\operatorname{UnitErr}.
\tag{KWR-3}
\]

若先对 `m` 的同余类写成 `m≡rho bar(ell) mod R`，则等价展开为

\[
1_{m\equiv \rho\bar\ell\pmod R}
-
{1\over R}1_{(m,R)=1}
=
{1\over R}\sum_{1\le h<R}
e\!\left({h(m-\rho\bar\ell)\over R}\right)
+\operatorname{UnitErr}.
\tag{KWR-4}
\]

这里 `bar(ell)` 是 `ell mod R` 的逆元。`UnitErr` 只来自非单位或小素冲突；这些点已被夹逼低模
缺陷或小骨架出口吸收。

`(KWR-4)` 是关键：非零频率含有

\[
e\!\left(-{h\rho\bar\ell\over R}\right),
\tag{KWR-5}
\]

这正是 Kloosterman 型逆元相位。

## 2. 窗口化互补商和

令 `I` 为 H3 行窗口，长度 `H<=q+O(1)`。对每个 `ell`，互补商窗口为

\[
J_\ell=\{m:\ell m\in I\},
\qquad |J_\ell|\le {q+O(1)\over \ell}.
\tag{KWR-6}
\]

在 `y>q^{2/3}` 下，

\[
|J_\ell|\ll q^{1/3}.
\tag{KWR-7}
\]

将素数指示替换为 von Mangoldt 权重并用局部部分求和恢复，非零频率主对象可写为

\[
\mathcal K(C_*)
=
\sum_{c\in C_*}
\sum_{1\le h<R(c)}
\beta_{c,h}
\sum_{y<\ell\le p}
\alpha_\ell
e\!\left(-{h\rho(c)\bar\ell\over R(c)}\right)
\sum_{m}
\Lambda(m)W_{\ell,c}(m)
e\!\left({hm\over R(c)}\right),
\tag{KWR-8}
\]

其中：

- `alpha_ell` 是素数 `ell` 的平滑/分块权；
- `W_{ell,c}` 是支持在 `J_ell` 上的平滑窗口；
- `beta_{c,h}` 含 `1/R(c)`、夹逼权和符号；
- 端点、非单位、孤立删除误差已进入前层命名缺陷或 `O(q/log^2 y)` 账本。

若 `H3-DSB` 反例仍无命名缺陷，则上一层的非零频率缺陷等价于

\[
|\mathcal K(C_*)|
\gg {q\over \log y\,\mathcal M}
\tag{KWR-9}
\]

对某个频率族成立。

## 3. 与 DI/BFI/KLS-window 的匹配项

`(KWR-8)` 已具备 Kloosterman 窗口结构：

1. **模数**：`R(c)=lcm(r_-,r_+)`；
2. **逆元变量**：`ell`，相位为 `e(-h rho(c) bar(ell)/R(c))`；
3. **频率**：`h`，`1<=h<R(c)`；
4. **第二变量**：互补商 `m`，带短窗口 `W_{ell,c}` 与相位 `e(hm/R(c))`；
5. **素数权**：`alpha_ell` 与 `Lambda(m)`，可经 Vaughan/Heath-Brown 分解进入 Type I/II。

因此可引用输入必须覆盖如下窗口型估计：

\[
\mathcal K(C_*)
=
O_A\!\left({q\over(\log q)^A}\right)
\tag{KWR-10}
\]

或至少给出 `O(q/log^2 y)`。

## 4. 参数关口

这里不能简单写“由 DI/BFI 得到”。必须核验：

### 4.1 模数范围

由于 `r_\pm<=y`，

\[
R(c)\le y^2.
\tag{KWR-11}
\]

若 `y>q^{2/3}`，则最坏 `R(c)` 可达 `q^{4/3}`，大于行尺度 `q`。DI/BFI 型 KLS-window
通常只覆盖某个 dyadic level 内的模数族。因此必须做分裂：

```text
R(c)<=R_0       : KLS-window branch;
R(c)>R_0        : high-lcm clamp branch.
```

高 `R(c)` 分支不能直接由同一个 KLS 输入覆盖；它必须由夹逼低模集中、端点稀疏或高 lcm
容量排斥另行吸收。

新增高 `lcm` 路由见
`docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md`。该路由证明：若
`R(c)>R_0` 分支承载 `q/log y` 级质量，则一行内每个夹逼单元容量至多
`1+floor((q+O(1))/R_0)`，所以大质量必变成大量几乎单点的高 `lcm` 激活单元。
进一步按坏行集合做 persistent/sparse 二分：persistent 分支给出坏行指示函数的非零
CRT/Fourier 缺陷，进入 `PDEC/ColumnCRT`；sparse 分支进入 `SAE` 单窗逃逸。
因此 high-lcm 不再是 KLS-window 的未说明参数漏洞，而是一个已经路由到既有最终出口的分支。
进一步的能量夹逼见
`docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md`：同模高 `lcm` 相位块满足
`\sum_{h\ne0}|\widehat\mu(h)|^2=R\sum_a\mu(a)^2-U^2`，且当 `U<=R/2` 时至少为 `RU/2`。
所以 high-lcm 大质量必注入非零 Fourier 能量；持久时进入 `PDEC/ColumnCRT`，非持久时进入
`SAE/endpoint`。
阈值形式见 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md`：
对同一 formal unit，persistent 高 `lcm` 出口给出
`L_HLC=((R sum g(a)^2-U^2)/(R-1))^(1/2)`。若 `U>R/2`，则不是分散逃逸，而是
稠密有效模集中，回到 `KLS-window`、`PDEC/ColumnCRT` 或 `SAE/endpoint`。
若同口径 PDEC 上界失败，则
`docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 证明失败必局部化为
非零频率 Bohr-cap 集中，帽内质量至少 `(L-alpha U)/(1-alpha)`；该集中只能成为新的
PDEC 约束行或 `SAE/endpoint` 单窗出口。
进一步 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 将该帽集中拆成
`d=(h,R)` 的有效模数层：若 `d` 大，则是低有效模集中；若 `d` 小，则某个短弧组件承载
至少 `(L-alpha U)/(d(1-alpha))` 的质量，进入 PDEC 约束或 `SAE/endpoint`。
`docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 进一步证明 high-gcd 分支可无损
下降到 `R'=R/d`：Fourier 系数与 Bohr-cap 质量都保持，且有效模数严格缩小。因此 high-gcd
不再是独立剩余，只能终止于低有效模 PDEC/KLS 或 short-arc cap。
`docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 继续把 short-arc cap
压成密度压力：
`R(L-alpha U)/(D0(1-alpha)U(D0+omega(alpha)R))`。若该量超过 `1+epsilon`，
则强制 PDEC 局部密度行或 `SAE/endpoint`；否则只剩显式参数残余不等式。

### 4.2 互补商窗口长度

由 `(KWR-7)`，`m` 窗口长度最多 `q^{1/3}`，且当 `ell` 接近 `q` 时为常数级。这是强短窗口。
任何外部定理必须允许：

```text
短窗口平滑权 W_{ell,c}；
ell 依赖的窗口端点；
dyadic 分块后仍保持多对数损失。
```

### 4.3 频率范围

频率 `h` 满足 `1<=h<R(c)`。若用 Vaaler 或平滑截断削尾，需证明高频尾可由端点预算吸收，
并把有效范围压到

\[
|h|\le H_0(R,q)
\tag{KWR-12}
\]

进入 KLS-window 可控区。

### 4.4 系数二范数

无尾标签集中、无夹逼集中应给出

\[
\sum |\beta_{c,h}|^2,\qquad \sum|\alpha_\ell|^2
\tag{KWR-13}
\]

的多对数账本。若某项二范数过大，本身就是 `Tail-label concentration` 或 `Clamp concentration`
缺陷。

## 5. 确定性二分

由以上参数，得到当前最窄二分：

```text
H3-DSB bad row
=> Kloosterman window sum K(C_*) is large
=> either
   (A) KLS-window estimates cover the active parameter range and contradict largeness;
   (B) active mass lies in high-lcm clamp branch R(c)>R0,
       hence enters Persistent-HLC/PDEC-ColumnCRT or Sparse-HLC/SAE;
   (C) active mass lies in high-frequency/sawtooth tail;
   (D) coefficient norms concentrate.
```

其中：

- `(B)` 已路由到 `Persistent-HLC` 非零 CRT/Fourier 缺陷或 `Sparse-HLC` 单窗逃逸；
- `(C)` 应路由到端点 sawtooth 缺陷；
- `(D)` 是尾标签或夹逼集中；
- `(A)` 是唯一需要外部 DI/BFI/KLS-window 输入的分支。

## 6. 本步实际推进

本步严格完成：

1. 把 `m≡rho bar(ell) mod R` 改写为加性逆元相位；
2. 得到 Kloosterman 核 `e(-h rho bar(ell)/R)`；
3. 写出短互补商窗口双线性和 `(KWR-8)`；
4. 明确 DI/BFI/KLS-window 需要核验的四个参数关口；
5. 将最终硬点拆成 `KLS-window`、`high-lcm clamp`、`high-frequency endpoint`、`coefficient concentration`
   四个仍属于同一命题内部的分支。

因此当前真正剩余不再是抽象“大筛缺陷”，而是：

```text
证明 KLS-window 覆盖活跃参数，并对每个 HLC formal unit 证明
`U_CRT(B)<L_HLC(B)`，或把失败 Bohr-cap 全部物化为 PDEC/SAE 证书，
并排除低有效模出口与 short-arc density pressure 残余，
并逐项排除 high-frequency / concentration 两个逃逸分支。
```
