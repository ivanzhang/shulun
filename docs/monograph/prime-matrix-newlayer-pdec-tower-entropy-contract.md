# New-layer PDEC 塔熵合同：无穷层叠不能保持无名

**状态：** `newlayer_pdec_tower_entropy_reduction_not_terminal_exclusion`

本文承接 `prime-matrix-pdec-cap-refinement-no-cycle.md`。上一层说明：固定有限签名群内的 cap 细化
不能无限循环；若必须不断提升签名群 `G_0<G_1<G_2<...`，则进入 `new-layer PDEC` 或 `CleanKLS`。

本文继续处理用户强调的“无穷迭代、无穷层叠、无穷缠绕”：允许素数规律逐层叠加，但每一层新增
偏斜都必须支付一个可累计的熵/能量成本。无限塔只有两种归宿：

```text
累计偏斜不消失 => profinite/global PDEC；
累计偏斜可求和并趋零 => asymptotic flat / CleanKLS。
```

因此 `new-layer PDEC` 不能成为新的无名逃逸。

## 1. 层塔对象

设签名层逐步提升：

```text
G_0 -> G_1 -> G_2 -> ...,
G_{n+1} = G_n x F_{r_{n+1}}
```

其中 `F_{r}` 是新增素因子层的单位类、列位移类或 Fourier cap 分区。令 `g_n` 是同一坏窗集合
在 `G_n` 上的投影计数，`M=sum g_n` 不变。

对每个旧原子 `A in G_n`，新层把它分成若干 fiber `A x b`。写：

```text
p_A(b)  = g_{n+1}(A,b)/g_n(A)；
mu_A(b) = 结构模型给出的条件基准分布。
```

这里 `mu_A` 不是概率猜测，而是该层允许类、列位移或 cap 分区的条件基准；若没有合法基准，
该层不能作为 `PDEC-Cert` 上界输入，必须回到 `Multiplicity/Stitching` 或约束来源证明。

## 2. 熵成本

定义第 `n+1` 层相对熵成本：

\[
H_{n+1}
=
\sum_{A:g_n(A)>0}
{g_n(A)\over M}
\sum_b p_A(b)\log {p_A(b)\over \mu_A(b)}。
\tag{NPT-1}
\]

并定义二次能量成本：

\[
E_{n+1}
=
\sum_{A:g_n(A)>0}
{g_n(A)\over M}
\sum_b { (p_A(b)-\mu_A(b))^2 \over \mu_A(b)}。
\tag{NPT-2}
\]

Pinsker/Cauchy 给出：

```text
若某新层 fiber/cap 有 p_A(B)-mu_A(B)>=epsilon，
则 H_{n+1} 或 E_{n+1} 有正成本。
```

更具体地，对任意 fiber 集合 `B`：

\[
\sum_b p_A(b)\log {p_A(b)\over\mu_A(b)}
\ge
p_A(B)\log {p_A(B)\over\mu_A(B)}
+
(1-p_A(B))\log {1-p_A(B)\over1-\mu_A(B)}。
\tag{NPT-3}
\]

因此 new-layer PDEC 若在固定比例坏窗质量上持续出现，就不能零成本穿过无限层。

## 3. 塔二分

考虑无限层塔。必有二分：

### 3.1 熵发散分支

若

\[
\sum_n H_n=\infty
\quad\text{或}\quad
\sum_n E_n=\infty,
\]

则坏窗分布相对基准在乘积签名群上出现不可吸收偏斜。有限截断层已给出任意大的低模能量，
因此形成：

```text
profinite/global PDEC certificate；
或某有限截断层的 ColumnCRT/endpoint atom。
```

这不是新出口；它是 `PDEC-Cert` 在更大 `G_N` 上的同一对象。

### 3.2 熵可求和分支

若

\[
\sum_n H_n<\infty
\quad\text{且}\quad
\sum_n E_n<\infty,
\]

则新增层条件偏斜趋零：

```text
for most active atoms A,
p_A(b)-mu_A(b) -> 0。
```

于是高层新增相位只剩高维分散振荡，不能持续给固定方向的 PDEC cap。该分支进入：

```text
asymptotic flat NewLayer；
CleanKLS / high-dimensional DLS absorption。
```

若在可求和分支中仍出现某个固定方向的正比例 cap，则 `(NPT-3)` 给出正熵成本，与可求和且趋零矛盾。

## 4. 与层叠轮筛的解释

`30 -> 210 -> 2310 -> ...` 的新增素因子层确实会不断产生新 Fourier 能量；这不需要被否认。
真正的结构刚性是：

```text
新增能量集中同步
  => 熵成本累积，进入 profinite/new-layer PDEC；

新增能量高维分散
  => 单层峰不能支付行覆盖压力，进入 CleanKLS/DLS；

新增层口径不合法
  => Multiplicity/Stitching 或约束来源义务。
```

这正好表达“素数规律无穷层叠”的本质：可以无穷层叠，但每层若要帮助零行覆盖，就必须留下
可累计的相位信息；若不留下，就只能是分散噪声，不能支付自归一化余量。

## 5. 形式化结论

**NewLayer-PDEC Tower Dichotomy.**
沿任意最小反例族，若 PDEC cap 细化需要无限提升签名层，则必有：

```text
1. 某有限截断层形成 explicit/refined PDEC 或 ColumnCRT；
2. 无限塔的熵/能量发散，形成 profinite/global PDEC；
3. 熵/能量可求和，新增层偏斜趋零，进入 CleanKLS/DLS；
4. 层间口径不一致，进入 Multiplicity/Stitching。
```

因此 `new-layer PDEC` 塔不能作为第五类无名终端。

## 6. 当前闭合边界

本文完成：

```text
无限提升层塔的结构二分；
new-layer PDEC 不能无限保持无名。
```

本文未完成：

```text
profinite/global PDEC 的最终 U_CRT<L_PDEC；
CleanKLS/DLS 的全局证明；
ColumnCRT/SAE/Multiplicity-Stitching 的终端排斥。
```

所以当前主链更新为：

```text
new-layer PDEC tower
=> finite PDEC/ColumnCRT
   or profinite PDEC
   or CleanKLS
   or Multiplicity-Stitching。
```

这仍是结构归约，不是最终无条件闭合。

## 7. Multiplicity-Stitching 吸收

新增 `prime-matrix-multiplicity-stitching-absorption-contract.md` 后，层间口径不一致不再作为终端出口保留。
它必须进入三归宿：

```text
WeightedDualIndependence => weighted PDEC；
CoordinateQuotient       => primitive/physical PDEC 或 CleanKLS；
ReuseDefect              => ColumnCRT / SAE / TailAnchor / CofactorAnchor。
```

因此 `Multiplicity-Stitching` 是证书规范化步骤，而不是新的数学逃逸机制。

## 8. 删除势前置筛

新增 `prime-matrix-triad-a1-infinite-tower-deletion-entropy-dichotomy.md` 后，new-layer 熵账前面补上了
一个更基础的支撑删除账。沿同一全周期完成集合 `C_P` 的投影塔，设每层平均 fiber 幸存率为 `a_n`，
删除势为：

\[
D_n=-\log a_n.
\]

则：

```text
sum D_n = infinity
  => 支撑密度趋零，进入 Sparse/LocalSurvivor/容量矛盾；

sum D_n < infinity
  => a_n -> 1，才进入本文的 KL/PDEC vs CleanKLS 熵二分。
```

因此 new-layer tower 的实际流程应为：

```text
ProjectionMonotonicity
=> DeletionPotential
=> NoDeletionEntropy
=> PDEC or CleanKLS。
```

这使“无穷层叠”更硬：每层先支付删除成本；删除不够，才必须支付信息偏斜成本。
