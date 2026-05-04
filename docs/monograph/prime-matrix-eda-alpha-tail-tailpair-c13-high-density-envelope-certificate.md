# AlphaTail `C13` HighDensityEnvelope 层投影证书

**状态：** `c13_high_density_envelope_certificate_input_ready`

本文接续 `band sparse acceptance`，处理其互补分支 `HighDensityEnvelope`。目标是证明：一旦
某个 envelope group 不能由稀疏 SAE 吸收，它必然投影到某个具体 `m` 层，形成固定差值端点带
高密度尾素对块。这给 `cross-modulus stitching/ColumnCRT` 提供正式输入。

## 1. 层投影

设 envelope group `E` 有

\[
S(E)>\eta\Omega(E).
\tag{HDE-1}
\]

其中 `S(E)` 是观察到的深度槽数，`\Omega(E)` 是 envelope 槽数。若点位层集合为 `M`，
则至少存在一个层 `m in M` 满足

\[
S_m(E)\ge \left\lceil {S(E)\over |M|}\right\rceil
>
{\eta\over |M|}\Omega(E).
\tag{HDE-2}
\]

这里 `S_m(E)` 是该 `m` 层中的 witness depth slots 数。

**证明。**  
所有观察槽按其出现的 `m` 层投影。一个槽可出现在多个 `m` 层，但选择任意出现层即可得到
对 `S(E)` 个槽的覆盖。若每个层都少于 `S(E)/|M|`，总覆盖少于 `S(E)`，矛盾。□

因此 `HighDensityEnvelope` 给出一个具体固定差值高密度块：

```text
(p,B,r,m,g,j1,j2,u,side,epsilon; h-range)
with at least ceil(S/|M|) witness pairs.
```

## 2. 出口

该层投影不能再作为普通 SAE 稀疏项处理。它进入：

```text
LayerHighDensityEndpointPair
=> cross-modulus stitching / ColumnCRT
   or fixed-gap endpoint-band density contradiction.
```

它的输入字段为：

```text
gap g；
layer m；
shape (j1,j2,u,side)；
epsilon；
envelope slots Omega(E)；
observed slots S(E)；
best layer slots S_m(E)；
witness pairs q,q+g。
```

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_high_density_envelope_certificate.py
```

压力测试 `C=1.2, eta=0.04`：

```text
high_groups 0 high_slots 0
```

路线测试 `C=1.2, eta=0.03`：

```text
high_groups 3 high_slots 14
max_density 0.037594
max_best_layer_density 0.030075
```

最紧高密度块：

```text
g=24, u=3, eps=1, observed=5, envelope=133,
best_m=4, best_slots=4,
witnesses: 1399+24, 1409+24, 1423+24, 1427+24.
```

这说明高密度出口会输出实际层证书，而不是停留在抽象密度判断。

## 4. 对主链的影响

`HighDensityEnvelope` 现在细化为：

```text
HighDensityEnvelope
=> LayerHighDensityEndpointPair
=> stitching/ColumnCRT or endpoint-band density contradiction.
```

下一层一维化见 `prime-matrix-eda-alpha-tail-tailpair-c13-layer-interval-reduction.md`：
固定层内 `h` 与 `q` 一一对应，因此高密度层给出一个普通固定 gap q-区间
`J_band`，其中至少有 `S_m(E)` 个尾素对 `q,q+g`。

当前 `eta=1/25` 的压力样本没有该出口；但若全局证明中出现高密度 envelope，本文给出其
必须提交的证书格式和下游矛盾接口。

## 5. 审稿边界

已完成：

```text
HighDensityEnvelope 的层投影鸽巢引理；
层级高密度端点素对块证书格式；
一维固定 gap q-区间归约接口；
脚本可输出 eta=0.03 路线测试中的高密度证书。
```

仍未完成：

```text
全局排斥 LayerHighDensityEndpointPair；
或证明目标窗口族不会出现 HighDensityEnvelope；
SparseSAE 总 envelope 量的全局可求和。
```

所以本文把高密度出口物化为下游证书，不是行命题最终闭合。
