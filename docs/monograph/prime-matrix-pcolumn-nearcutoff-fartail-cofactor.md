# 第P列近截止峰与远尾互补因子反演

**状态：** `structural_identity_plus_audit_not_a_proof`

本文接续 `PColumn Dynamic Capacity`。上一层发现全行动态容量的最紧行常出现在

\[
y\asymp Y=P^{0.43}
\]

附近，表面 top labels 是 cutoff 后第一批高素。新的审计进一步修正了这个判断：最大单线确实来自 `q≈Y`，但相对正偏差 `D+=max(0,T-HS)` 的主来源是远尾 `q>10Y`。

## 1. 近截止 top label 与正偏差分离

脚本：

```text
experiments/prime_matrix_pcolumn_nearcutoff_spike_audit.py
```

报告：

```text
docs/pcolumn_nearcutoff_spike_audit_20260506.md
docs/pcolumn_nearcutoff_spike_audit_20260506.json
```

在 `y<=4Y` 中扫描最强 `T/S` 行，结果为：

| P | cutoff | best y | S | T | margin | T/S | U/S | overlap/T | D+/sqrt | model/sqrt | top q |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 5003 | 38 | 41 | 741 | 695 | 46 | 0.937922 | 0.464238 | 0.505036 | 3.415103 | 5.104955 | `41,43,47,53` |
| 10007 | 52 | 46 | 1389 | 1291 | 98 | 0.929446 | 0.462203 | 0.502711 | 4.026284 | 6.655795 | `53,59,61,67` |
| 20011 | 70 | 71 | 2596 | 2484 | 112 | 0.956857 | 0.473806 | 0.504831 | 6.659539 | 8.857731 | `71,73,79,83` |
| 50021 | 104 | 104 | 5884 | 5400 | 484 | 0.917743 | 0.454623 | 0.504630 | 7.434438 | 13.744143 | `109,107,113,127` |
| 100003 | 141 | 147 | 11128 | 10351 | 777 | 0.930176 | 0.460550 | 0.504879 | 11.044909 | 18.410582 | `157,151,163,149` |

两点很稳定：

```text
1. top q 位于 cutoff 后第一批高素；
2. 实际并集覆盖 U/S 只有约 0.45 到 0.48，overlap/T 约 0.50。
```

所以这些行的高 `T/S` 有强重叠，离全覆盖仍很远。

但按 `q/Y` 分桶后，最大正偏差来自 `q>10Y`：

| P | best y | q>10Y hit share | q>10Y D+/sqrt |
|---:|---:|---:|---:|
| 5003 | 41 | 0.512230 | 3.438574 |
| 10007 | 46 | 0.529822 | 4.101221 |
| 20011 | 71 | 0.564412 | 6.727107 |
| 50021 | 104 | 0.602222 | 8.771821 |
| 100003 | 147 | 0.624867 | 12.725422 |

因此硬点应重命名为：

```text
NearCutoff-FarTail Split:
  近截止高素 q≈Y 造成最大单线；
  远尾 q>10Y 承担主要正偏差；
  两者通过互补因子反演相连。
```

## 2. 远尾互补因子恒等式

脚本：

```text
experiments/prime_matrix_pcolumn_far_tail_cofactor_audit.py
```

报告：

```text
docs/pcolumn_far_tail_cofactor_audit_20260506.md
docs/pcolumn_far_tail_cofactor_audit_20260506.json
```

对远尾 `q>10Y`，写

\[
Py-d=qm,\qquad 1\le d<P.
\]

则命中条件严格等价于

\[
\left\lceil {Py-P+1\over m}\right\rceil
\le q\le
\left\lfloor {Py-1\over m}\right\rfloor,
\tag{NFT-1}
\]

同时

```text
q prime, q>10Y, q<P,
m 避开所有 ell<=Y。
```

因为 `q>Y`，`Py-d` 避开低素当且仅当 `m` 避开低素。这给出精确反演：

\[
T_{>10Y}(P,y)=
\sum_{\substack{m\le (Py-1)/(10Y)\\(m,\mathcal P_Y)=1}}
\#\left\{
q\ {\rm prime}:
\max(10Y,\lceil (Py-P+1)/m\rceil)<q<P,\ 
q\le \lfloor (Py-1)/m\rfloor
\right\}.
\tag{NFT-2}
\]

审计中按 `q` 直接计数与按 `m` 反演计数完全一致：

| P | y | tail q min | tail hits | direct | delta | active m | m range | top m |
|---:|---:|---:|---:|---:|---:|---:|---|---|
| 5003 | 41 | 381 | 356 | 356 | 0 | 87 | `41..523` | `41,47,43,61` |
| 10007 | 46 | 521 | 684 | 684 | 0 | 135 | `53..883` | `53,59,61,67` |
| 20011 | 71 | 701 | 1402 | 1402 | 0 | 277 | `71..2017` | `73,71,83,79` |
| 50021 | 104 | 1041 | 3252 | 3252 | 0 | 610 | `107..4957` | `109,107,113,127` |
| 100003 | 147 | 1411 | 6468 | 6468 | 0 | 1181 | `149..10321` | `167,163,157,181` |

## 3. 双边界结构

最强 `m` 也位于 cutoff 后第一批 `Y`-rough 数。于是远尾高素命中具有双边界形态：

```text
m ≈ Y,          q ≈ Py/m ≈ P；
m 为 Y-rough， q 为素数；
qm 落入 (P(y-1), Py) 的一行短窗。
```

例如 `P=100003,y=147`：

```text
m=167, q in [87428,88026], hits=60；
m=163, q in [89574,90186], hits=58；
m=157, q in [92997,93633], hits=57。
```

这说明远尾不是无结构噪声，而是大量低互补因子 `m≈Y` 在靠近 `P` 的短素数区间内取素数。

互补因子分桶也显示主要质量来自低 `m/y` 层：

| P | largest m-band | hits in largest band |
|---:|---|---:|
| 5003 | `(2,5]y` | 128 |
| 10007 | `(2,5]y` | 228 |
| 20011 | `(2,5]y` | 375 |
| 50021 | `(2,5]y` | 767 |
| 100003 | `(2,5]y` | 1392 |

但 `(1,2]y` 也持续承担很大质量，且 top `m` 全部落在这一层附近。

## 4. 对闭合路线的意义

`PColumn Dynamic Capacity` 现在分成三道门：

```text
Capacity:
  T_Y(P,y)<S_Y(P,y) 直接给素数洞。

NearCutoff-FarTail Split:
  最紧 T/S 行若出现，先拆成 q≈Y 单线峰与 q>10Y 正偏差。

FarTail Cofactor Inversion:
  q>10Y 正偏差等价于 Y-rough m 上的短素数区间总计数。
```

下一步最小硬点不应再写成泛泛的“高素斜线偏差”，而应写成：

```text
FarTail-Cofactor Bound:
  对 y≈Y 的目标行，证明 NFT-2 的总量不足以把 T 推到 S；
  若失败，则某些 Y-rough m 的短素数区间持续超额，
  进入 cofactor-anchor / SAE / ColumnCRT / PDEC。
```

这与用户提出的“素数规律是无穷层叠轮筛”一致：低层轮筛留下 `m` 的粗骨架，高层素数 `q` 在反演短区间中继续筛；若某层异常同步，就显化为固定互补因子相位或列位移缺陷。

## 5. 模型付款常数

新增：

```text
docs/monograph/prime-matrix-pcolumn-fartail-model-payment.md
experiments/prime_matrix_pcolumn_far_tail_model_bound.py
experiments/prime_matrix_pcolumn_tail_payment_constant_scan.py
```

定义

\[
\operatorname{Model}_{tail}=\sum_m {|I_m|\over\log q_m^-}.
\]

对 `P=5003,10007,20011,50021,100003,200003` 的最强近截止行，实际远尾命中满足

```text
actual/model = 0.993758 到 1.025423。
```

而闭合 `T<S` 允许常数为

```text
C_allow = (S-non_tail)/model = 1.107340 到 1.160000。
```

进一步扫描每个 `P` 的 top-16 风险行，`C_tail=1.05` 全部通过，失败数为 `0`。最紧点仍为
`P=20011,y=71`：

```text
S=2596, T=2484,
tail=1402, non_tail=1082,
model_tail=1367.240,
C_allow=1.107340,
payment_margin(C=1.05)=78.398。
```

因此下一硬点升级为：

```text
FarTail-Model Bound:
  证明 tail <= 1.05 * Model_tail；
  若失败，则超标层进入 cofactor-anchor / SAE / PDEC / ColumnCRT。
```
