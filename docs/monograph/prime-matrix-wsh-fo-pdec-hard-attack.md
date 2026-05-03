# FO-PDEC 硬攻稿：低模缺陷方程与剩余不等式

**状态：** `fo_pdec_equation_closed_global_inequality_open`

本文专攻 `FO-PDEC`。本轮完成的不是全局无条件闭合，而是把 `FO-PDEC` 从描述性出口压成
精确方程组和唯一剩余不等式。

## 1. 已闭合的方程化部分

固定相邻素数 `p<q`，行宽为 `q`。令固定偏移满载长块给出缺失候选

\[
  n=b+d,\qquad b=u v,\qquad 1<n<q^2。
\]

由 `FO-1/FO-2`，若 `n` 非素，则存在解释因子 `ell in (13,p]`。将

\[
  n=(r-1)q+c,\qquad 1\le c\le q
\]

写成方阵坐标，则 `ell|n` 等价于精确 CRT 行方程

\[
  r\equiv 1-cq^{-1}\pmod{\ell}.
\tag{FO-CRT}
\]

同时，由 `b=uv` 和 `n=b+d`，同一缺失还满足双尾双线性方程

\[
  uv+d\equiv0\pmod{\ell}.
\tag{FO-BIL}
\]

因此固定偏移缺失不再是“素数不足”的黑箱，而是每个缺失候选都产生一条
`(FO-CRT)` 低模行相位约束和一条 `(FO-BIL)` 双尾同余约束。

## 2. 有限低模账本

新增脚本：

```text
experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.md
docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json
```

在 `SCB-1` 最紧长块的满载固定偏移账本上，结果为：

```text
full offset rows = 11
lowmod equations = 43
distinct explaining factors = 21
CRT equation failures = 0
bilinear equation failures = 0
semiprime factor failures = 0
max global factor load = 4
max factor-residue load = 2
max same (q,row,factor) load = 2
max same (block,factor) load = 1
```

解释：

1. `CRT equation failures=0` 说明每个解释因子都严格给出行相位约束；
2. `bilinear equation failures=0` 说明每个解释因子都同时约束双尾因子对；
3. `max same (block,factor) load=1` 说明最紧样本局部不是 Tail-repeat 型；
4. `max same (q,row,factor)=2` 和 `max factor-residue load=2` 显示低模信号已经有重复相位，
   但有限样本仍不足以替代全局持久化证明。

## 3. FO-PDEC 的最小剩余不等式

对一族固定偏移缺失候选 `E`，定义解释方程多重集

\[
  \mathcal L(E)=\{(\ell,\rho): \ell\in(13,p],\ \rho=1-cq^{-1}\bmod \ell,\ \ell\mid n\}.
\]

定义低模缺陷能量

\[
  \mathcal E(E)
  =
  \sum_{\ell\le p}
  \sum_{\rho\bmod \ell}
  \left(
    m_{\ell,\rho}(E)-{|\mathcal L(E)_\ell|\over \ell}
  \right)_+,
\]

其中 `m_{ell,rho}` 是 `(\ell,\rho)` 的出现次数。

`FO-PDEC` 现在可压成以下明确目标：

```text
若固定偏移满载长块缺少足够素数，
且没有 Tail-anchor，
且 SAE/Endpoint 稀疏逃逸不触发，
则 E 的低模缺陷能量 E(E) 超过 PDEC 证书阈值。
```

换言之，剩余不是寻找新的结构，而是证明一个能量下界：

\[
  \mathcal E(E)\ge L_{\mathrm{PDEC}}(E)
\tag{FO-PDEC-E}
\]

并把同一坏窗集合的 CRT 上界证明为

\[
  U_{\mathrm{CRT}}(E)<L_{\mathrm{PDEC}}(E).
\tag{PDEC-CLOSE}
\]

`(FO-PDEC-E)+(PDEC-CLOSE)` 才能给出全局排斥。

## 4. 已经排除的误攻方向

本轮方程化也排除了三个不严谨路线：

1. **不能只说“固定偏移满载必矛盾”。** 有些满载候选本身就是素数；不足部分才进入解释因子。
2. **不能只靠局部 Tail-repeat。** 当前最紧样本的同块解释因子最大负载为 `1`。
3. **不能用有限重复相位替代全局 PDEC。** 有限账本显示重复信号，但全局还需要统一能量下界。

## 5. 下一步唯一硬攻点

下一步应直接构造 `FO-PDEC-E` 的证明或证书：

```text
Input:
  fixed-offset full-load, insufficient primes, no Tail-anchor, no SAE/Endpoint.

Output:
  low-mod defect energy exceeds explicit PDEC threshold.
```

可攻路线：

1. **持久化路线：** 在相邻行、镜像块、递归壳层中证明同一 `(ell,rho)` 或同一低模字典方向必须重复；
2. **双线性路线：** 利用 `uv+d=0 mod ell`，证明分散解释因子会迫使尾因子对在低模图中过密；
3. **端点路线：** 若上述重复不发生，则缺失只能分散在短端点，转入 `SAE/Endpoint` 排斥。

当前结论保持：

```text
FO-PDEC equation layer closed;
global FO-PDEC inequality still open.
```

## 6. 能量下界硬攻更新

新增：

```text
experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py
docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-energy-lemma.md
```

后，`FO-PDEC` 的能量产生部分已经有无条件组合下界。对任意解释方程多重集 `E`，
固定 `0<theta<1`，若不存在 `t_ell>theta ell` 的高负载解释因子，则

\[
  \mathcal E(E)\ge(1-\theta)|E|.
\]

若存在 `t_ell>theta ell`，则已经进入 `Tail/PDEC` 高负载出口。因此当前状态更新为：

```text
FO-PDEC energy production: proved.
FO-PDEC-to-PDEC threshold comparison: open.
```

默认 `theta=0.25` 的有限账本给出：

```text
global energy per equation = 0.9547817296210457
global high-load factor count = 0
```

下一步唯一硬点是同一坏窗集合上的 `PDEC` 阈值比较，而不是继续寻找新的结构命名。
