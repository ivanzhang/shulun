# FO-PDEC 低模能量下界引理

**状态：** `energy_lower_bound_proved_pdec_threshold_open`

本文继续硬攻 `FO-PDEC`，不再引入新的等价命题。目标是直接处理剩余的低模能量不等式：

```text
fixed-offset missing equations
=> enough low-mod positive defect energy
=> PDEC
```

本轮完成的是第一箭头的无条件组合下界；第二箭头仍需要正式 `PDEC` 阈值比较。

## 1. 低模能量

设 `E` 是固定偏移满载后产生的解释方程多重集。对每个解释因子 `ell`，记：

```text
t_ell = E 中使用 ell 的方程数；
s_ell = E 中出现过的 ell-行残基数。
```

定义正超额能量

\[
  \mathcal E_\ell(E)=t_\ell-\frac{s_\ell t_\ell}{\ell},
  \qquad
  \mathcal E(E)=\sum_\ell \mathcal E_\ell(E).
\]

该能量衡量解释方程相对于模 `ell` 均匀铺开的正偏斜。它只依赖已经证明的方程

\[
  r\equiv1-cq^{-1}\pmod\ell。
\]

## 2. 能量或高负载二分

**引理 FO-Energy.**
固定 `0<theta<1`。对任意解释方程多重集 `E`，至少一项成立：

```text
(A) 存在 ell 使 t_ell > theta*ell；
(B) E(E) >= (1-theta)|E|。
```

**证明。**
若 (A) 不成立，则对所有 `ell` 有 `t_ell<=theta ell`。又因 `s_ell<=t_ell`，

\[
  \mathcal E_\ell
  =
  t_\ell-\frac{s_\ell t_\ell}{\ell}
  \ge
  t_\ell-\frac{t_\ell^2}{\ell}
  =
  t_\ell\left(1-\frac{t_\ell}{\ell}\right)
  \ge
  (1-\theta)t_\ell。
\]

对 `ell` 求和得到

\[
  \mathcal E(E)\ge(1-\theta)\sum_\ell t_\ell=(1-\theta)|E|。
\]

证毕。

## 3. 高负载分支的吸收

若 (A) 发生，则同一解释因子 `ell` 在短固定偏移结构中承载超过 `theta ell` 条方程。
这不是分散逃逸，而是低模集中：

```text
t_ell > theta ell
=> row residues forced into ell-periodic class at density > theta
=> Tail/PDEC high-load exit.
```

因此 `FO-PDEC` 的真正剩余可以只考虑 (B) 的能量分支。

## 4. 有限能量账本

新增脚本：

```text
experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger.md
docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger.json
```

默认 `theta=0.25`。在当前低模方程账本上：

```text
global equation count = 43
global energy = 41.05561437370496
global energy per equation = 0.9547817296210457
global theta lower bound = 32.25
global high-load factor count = 0
min group energy per equation = 0.9667283278007247
max group high-load factor count = 0
```

该数据与引理一致：没有高负载因子时，能量非常接近每条方程贡献 `1`。

## 5. 剩余阈值接口

现在 `FO-PDEC` 已缩成一个明确的阈值比较：

```text
Need:
  L_PDEC(E) <= (1-theta)|E|
or
  U_CRT(E) < E(E)
with the same bad-window set E.
```

当前未证明的是 `L_PDEC` 的正式常数和同一坏窗集合上的 `U_CRT` 上界。换言之：

```text
FO-PDEC energy production is proved.
FO-PDEC-to-PDEC threshold comparison remains open.
```

这已经是全局闭合前的最窄定量硬点。下一步不应再转换结构，而应直接提交
`PDEC` 阈值账本：

1. 明确 `L_PDEC(E)` 的定义和常数；
2. 证明同一方程集合的 `U_CRT(E)` 上界；
3. 核验 `U_CRT(E)<(1-theta)|E|`。

## 6. 显式 Fourier 阈值更新

新增：

```text
experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py
docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-threshold-comparison.md
```

后，`FO-PDEC` 的下界侧又被显式化。对每个解释因子 `ell` 的行残基计数向量 `g_ell`，直接计算

\[
  M_\ell(E)=\max_{h\ne0}|\widehat g_\ell(h)|.
\]

当前账本最佳投影为：

```text
ell = 199
h = 95
M_ell(E) = 3.959247567099438
```

因此剩余硬点从抽象阈值比较变成具体目标：

```text
prove U_CRT,199 < 3.959247567099438
for the same projected bad-window set.
```

该 `U_CRT` 上界仍未证明；它必须来自合法的 `PDEC-Dual-Cert` 约束行或 `SAE/Endpoint`
排斥，不能来自完整 CRT 周期均衡。
