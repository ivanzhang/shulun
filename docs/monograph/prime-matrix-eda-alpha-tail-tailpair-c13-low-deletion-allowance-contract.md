# AlphaTail `C13` 低筛删除允许量合同

**状态：** `low_deletion_allowance_sample_closed_global_open`

本文把 `SlackFloor` 改写成更直接的删除允许量命题。该形式指出：真正需要全局证明的不是边缘门数，
而是低大素块在几何候选集上删除得足够少。

## 1. 等价变形

令

```text
G = G_geom；
L = low_survivor_exact = M2；
D_low = G-L；
R = B2_model + Cap_even；
E = K*E_M。
```

`SlackFloor` 为

\[
G-R\ge E.
\tag{LDA-1}
\]

等价于

\[
D_{\rm low}\le G-R-E.
\tag{LDA-2}
\]

右侧

\[
A:=G-R-E
\tag{LDA-3}
\]

称为允许删除量。于是当前最窄义务可写成：

```text
LowDeletionAllowance:
  low 大素块在几何候选集上的实际删除量 D_low 不超过 A。
```

密度形式为

\[
\frac{D_{\rm low}}G
\le
1-\frac{R+E}{G}.
\tag{LDA-4}
\]

这把证明目标变成两个可比较的量：

```text
实际删除密度；
允许删除密度。
```

## 2. 当前样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
G=17860；
low_survivor=17810；
D_low=50；
R+E=16474.036283；
A=1385.963717；
deletion_margin=1335.963717；
low_deletion_density=0.002800；
allowed_deletion_density=0.077602；
density_margin=0.074802；
allowance=True。
```

逐窗口：

```text
p=5003:
  G=6325；
  D_low=5；
  A=106.727367；
  deletion_density=0.000791；
  allowed_density=0.016874；
  margin=101.727367。

p=10007:
  G=11535；
  D_low=45；
  A=1279.236350；
  deletion_density=0.003901；
  allowed_density=0.110900；
  margin=1234.236350。
```

最紧层为 `p=5003,m=5`：

```text
G=3945；
D_low=4；
A=61.520978；
deletion_density=0.001014；
allowed_density=0.015595；
density_margin=0.014581。
```

## 3. 审稿价值

该接口比 `ResonanceFloor` 更具体：

```text
ResonanceFloor: 证明 M2-R >= E；
LowDeletionAllowance: 证明 G-M2 <= G-R-E。
```

在当前目标族中，`G-M2` 是低大素块对几何候选的实际删除量。由于低素块位于
`alpha p` 以上，而几何候选由尾素短差值结构生成，实验显示删除密度远小于允许密度。
下一步应专攻：

```text
证明 D_low/G 的通用上界；
证明 A/G 的通用下界；
或对两者的差给目标族统一正余量。
```

新增 `prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-reduction-contract.md`
后，`D_low` 又被改写为活跃 AP 类计数。当前样本满足

```text
D_low=raw_ap=unique_ap=active_AP_classes=50；
max_AP_pairs_per_class=1。
```

所以下一步可改攻：

```text
APSingleton + ActiveClassBound。
```

## 4. 审稿边界

本文没有证明完整目标族上的通用删除密度界。当前结论仍是：

```text
显式高 P 样本满足 LowDeletionAllowance；
完整行命题全局闭合仍需目标族生成器与通用密度界。
```
