# H3-DSB 高 lcm L2-flat residual 的 KLS admission 接口

**状态：** `hlc_l2_flat_kls_admission_proved_kls_parameter_check_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层证明：short-arc pressure 的低压残余必给出同一 formal unit 的 L2 平坦性。本文把该
平坦残余接入 `KLS-window` 的可审查 admission 表；若某项不通过，则它必须回到既有出口，
不能作为新的 short-arc 缺口保留。

## 1. L2-flat 输入

固定 HLC formal unit `B`，模数为 `R`，相位计数为 `g(a)`，总质量为 `U`。低压残余给出

\[
\sum_{a\bmod R}g(a)^2
\le
\mathfrak C_{\rm flat}(R,\tau)\frac{U^2}{R},
\qquad
\mathfrak C_{\rm flat}(R,\tau)=1+(R-1)\tau^2.
\tag{LKLS-1}
\]

同时支持大小满足

\[
A_B=\#\{a:g(a)>0\}
\ge
\frac{R}{\mathfrak C_{\rm flat}(R,\tau)}.
\tag{LKLS-2}
\]

因此该残余不是相位集中型对象；它是同模低二范数系数对象。

## 2. KLS admission 条件

L2-flat residual 进入 `KLS-window` 前必须逐项满足：

| 编号 | 条件 | 失败出口 |
|---|---|---|
| K1 | 有效模数 `R_eff<=R_KLS` | high-gcd 已下降；否则低有效模 PDEC/ColumnCRT |
| K2 | 有效频率 `|h|<=H_0(R,q)` | high-frequency/sawtooth endpoint |
| K3 | 互补商窗口 `J_ell=I/ell` 已平滑且端点误差入账 | endpoint/SAE |
| K4 | 系数二范数满足 `(LKLS-1)`，无大原子 | coefficient concentration |
| K5 | gcd/nonunit 层只产生多对数损失 | clamp low-mod / unit conflict |
| K6 | dyadic 与尾标签分块数量为多对数级 | tail-label concentration |

只有 K1--K6 全部满足，才能调用外部 `DI/BFI=>KLS-window` 输入；否则失败项已经是命名出口。

## 3. L2-flat 对 K4 的实际贡献

令归一化系数

\[
b_a=\frac{g(a)}{U}.
\tag{LKLS-3}
\]

由 `(LKLS-1)`，

\[
\sum_a |b_a|^2
\le
\frac{\mathfrak C_{\rm flat}(R,\tau)}{R}.
\tag{LKLS-4}
\]

这正是 Kloosterman 大筛需要的二范数输入。若 `(LKLS-4)` 不成立，则不是 KLS 失败，
而是 coefficient concentration 已触发。

## 4. admission 定理

**命题。** 对任意 HLC L2-flat residual，必有如下二分：

```text
要么 K1--K6 中某一项失败，并进入对应命名出口；
要么该 residual 是 KLS-window admissible。
```

**证明。**
K1 失败即模数仍在高有效层；由 high-gcd descent 只能是低有效模 PDEC/ColumnCRT 或尚未下降
完的等价层。K2 失败是频率截断外项，按 KWR 参数关口进入 high-frequency endpoint。K3 失败
只来自窗口端点与平滑误差，进入 endpoint/SAE。K4 由 `(LKLS-4)` 给出；若不满足则定义上就是
coefficient concentration。K5 失败说明非单位或 gcd 相容层超出多对数账本，回到 clamp
low-mod/unit conflict。K6 失败说明尾标签或 dyadic 块数集中，回到 tail-label concentration。
若无失败，则所有 KLS-window 变量条件均已满足。证毕。

## 5. 当前实际闭合度

本文完成：

1. L2-flat residual 的 KLS admission 条件表；
2. L2-flat 对系数二范数 K4 的直接证明；
3. 任一 admission 失败项的命名出口路由；
4. 证明低压平坦残余不能作为独立 short-arc 缺口保留。

本文仍未完成：

```text
逐项核验所有 HLC formal unit 的 K1--K6，
以及在 admissible 情形下引用/证明 KLS-window 覆盖本 HLC 参数。
```

这就是当前剩余障碍的精确外部输入/出口分界。

后续 clean-unit 归约见 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md`。
该文定义 clean HLC formal unit，证明无 E1--E6 命名出口时 K1--K6 自动通过，并把剩余
写成单一外部输入 `HLC-KLS-ext`：对 clean unit 的 Kloosterman 窗口对象 `(CKR-4)` 给出
`O(q/log^2 y)` 上界。

外部深定理版适配见 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md`。
该文把 `(CKR-4)` 的变量逐项接入 DI/BFI/Kuznetsov 型窗口化 Kloosterman 输入；完全自足版
仍需重证该谱/dispersion 定理。
