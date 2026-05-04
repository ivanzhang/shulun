# AlphaTail `C13` 低筛保存的提升层闭合证书

**状态：** `c13_lowsieve_lift_closure_sample_closed_global_open`

本文合成 `lift=1` 纯整数余量与 `lift>=2` 空性，给出当前压力样本的低筛保存闭合证书。

## 1. 合成判据

记

```text
S = G_geom-R                 低筛删除可用余量；
N1                           lift=1 纯整数候选数；
D_ge2                        lift>=2 真实删除数。
```

由提升层分解，

\[
D_{\rm low}\le N_1+D_{\ge2}.
\tag{LLC-1}
\]

因此：

**引理 LLC-1（提升层闭合）。**  
若

\[
N_1+D_{\ge2}\le S,
\tag{LLC-2}
\]

则 `LowSievePreservation` 成立。

**证明。**  
由 `(LLC-1)` 得 `G^L=G_geom-D_low>=G_geom-N1-D_ge2`。若 `(LLC-2)` 成立，则
`G^L>=R`，这正是 `HighP-PLT` 的输入。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_lift_closure.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_lift_closure.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  lift1=541；
  ge2_candidates=1368；
  ge2_both=0；
  consumed=541；
  margin=1996.963717；
  consumed/slack=0.213163；
  pass=True。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  consumed=285；
  margin=397.727367；
  consumed/slack=0.417443。

p=10007:
  slack=1855.236350；
  consumed=256；
  margin=1599.236350；
  consumed/slack=0.137988。
```

逐层最紧者仍为：

```text
p=5003,m=5:
  slack=461.520978；
  consumed=206；
  margin=255.520978；
  consumed/slack=0.446350。
```

## 3. 当前链条状态

当前压力样本的低筛保存链条现在是：

```text
AP 删除总量
  <= lift=1 纯整数候选 + lift>=2 真实删除；

lift=1:
  纯整数候选数小于余量；

lift>=2:
  ge2_both=0，且候选 q 均被 2/3 小素因子杀掉；

结论:
  LowSievePreservation 样本闭合。
```

这一步不再依赖 `AP-Brun-C20`，但全局推广仍需要证明相同提升层机制对完整目标窗口族成立。

## 4. 审稿边界

已完成：

```text
当前高 P 压力样本的低筛保存分支闭合；
闭合方式为纯整数 lift=1 余量 + lift>=2 小素因子空性；
最紧层余量仍为正。
```

仍未完成：

```text
全局证明所有 P>1000 目标窗口的 N1+D_ge2<=S；
证明 lift>=2 小素因子空性全局成立，或给 PDEC/SAE 出口；
把该低筛保存闭合接回 HighP-D2-Lower 全局目标。
```

所以本文闭合的是当前压力样本低筛保存分支，不是行命题最终闭合。
