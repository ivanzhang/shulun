# H3 全局尺度规律路线

**状态：** `global_scaling_reduction_not_global_proof`

本文把 H3 数据洞察上升为全局尺度二分。核心不是“有限模板覆盖无限变化”，而是：

```text
六轮粗剩余的自然尺度随 q/log q 增长；
H3 全阻断要求该尺度降为 0；
因此反例必须制造小首因子骨架过载或大量中尾标签同步。
```

这给出当前最窄硬点的全局本质：反例不是普通筛余波动，而是要在平方根长度窗口内持续抹掉一个增长的粗剩余尺度。

## 1. 自然尺度

固定 `p<q` 相邻，`I_s=[(s-1)q+1,sq]`。完整 3 行候选数为 `A_s`，其规模满足

\[
\#A_s={q\over 3}+O(1).
\]

若只按局部密度估计，避开所有 `5<=ell<=p` 的候选自然尺度为

\[
E_p(s)=\#A_s\prod_{5\le \ell\le p}\left(1-{1\over \ell}\right).
\]

由 Mertens 型乘积，这个尺度约为

\[
E_p(s)\asymp {q\over \log p}.
\]

因此，当 `q` 增大时，H3 幸存余量的自然尺度不是常数，而是增长量。

## 2. 数据支撑

新增审计：

```text
experiments/prime_matrix_h3_margin_growth_audit.py
docs/monograph/prime-matrix-h3-margin-growth-audit.md/json
```

在 `p<=5000` 全量 `1552462` 条非第一 `q` 行中：

```text
first p after which every prime layer has min margin >= 21: 331
bucket 318-500:   min margin 21,  avg margin 38.415350, avg expected 39.047703
bucket 1001-2000: min margin 54,  avg margin 113.613533, avg expected 117.873760
bucket 2001-3000: min margin 105, avg margin 173.344785, avg expected 180.903675
bucket 4001-5000: min margin 207, avg margin 286.620927, avg expected 300.919983
```

数据说明两点：

1. 最紧临界只发生在低层；到 `p=331` 后，最小余量已经离开 `<=20` 的近失败区。
2. 平均余量与 `A_s prod(1-1/ell)` 同阶，且 bucket 增长稳定，支持 `q/log q` 尺度。

## 3. 反例的尺度压力

若 H3 全阻断成立，则实际幸存余量为 `0`。与自然尺度比较，反例必须消除约

\[
\asymp {q\over \log q}
\]

个六轮粗候选。

这不是单个大因子或有限局部模板能长期完成的任务。结合 first-factor partition：

\[
A_s=\bigsqcup_{5\le \ell\le p}A_{s,\ell},
\]

反例只能走两种机制。

### 3.1 小首因子骨架过载

对 cutoff `y`，若小首因子骨架 `C_y` 已覆盖到接近 `#A_s`，则固定有限小素数在同一 `q` 行相位上承担异常高负载。该情形应进入：

```text
SmallSkeletonOverload(y,K) => Tail/PDEC.
```

### 3.2 多中尾标签同步

若小骨架不过载，令 `R_y=#A_s-C_y`。由小因子包络路线，H3 全阻断至少需要

\[
K_y=\left\lceil {R_y\over \lfloor q/\ell_+(y)\rfloor+1}\right\rceil
\]

个中尾标签。若取随 `p` 增长的 cutoff，例如 `y=p^\theta`，并用

\[
R_y\approx \#A_s\prod_{5\le \ell\le y}(1-1/\ell)
\asymp {q\over \log y},
\]

则

\[
K_y\gtrsim {y\over \log y}.
\]

这意味着：小骨架不过载时，反例必须激活随 `y/log y` 增长的中尾 first-factor 标签。大量标签在同一短行窗口内同步覆盖，会产生低模 PDEC 能量或 ColumnCRT 位移集中。

## 4. 全局二分命题

当前最小全局命题应写成：

```text
H3 Global Scaling Defect.
Fix y=p^theta with 0<theta<1.
If H3-SWR fails for a q-row, then either
  (i) C_y exceeds the admissible small-skeleton Tail/PDEC envelope;
  (ii) at least c_theta*y/log y middle-tail labels are active,
       and their label distribution gives H3-PDEC low-mod energy;
  (iii) endpoint rounding prevents the energy estimate,
       hence the row phase is SAE or ColumnCRT.
```

这是真正从数据到全局的本质规律：不是证明某个有限模板永远覆盖，而是证明反例若要把增长的粗剩余尺度压到 `0`，必然制造可命名的负载或相位缺陷。

## 5. 剩余硬点

本路线仍不是全局证明。剩余严证义务是：

1. 给 `C_y` 的 admissible Tail/PDEC envelope 明确定义并证明超过即触发缺陷；
2. 将 `K_y>=c y/log y` 的多标签结论转为低模能量下界；
3. 证明低模能量若被端点取整抵消，则端点相位进入 `SAE/ColumnCRT`；
4. 用同一阻断点集合和同一负载口径完成三出口不重不漏。

下一步最优专攻是第 1 项：`SmallSkeletonOverload(y,K)=>Tail/PDEC` 的阈值化。
