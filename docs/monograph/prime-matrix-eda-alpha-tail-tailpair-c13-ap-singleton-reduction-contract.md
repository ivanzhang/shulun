# AlphaTail `C13` 低筛 AP 单点化归约合同

**状态：** `ap_singleton_reduction_sample_closed_global_open`

本文把 `LowDeletionAllowance` 的实际删除量 `D_low` 进一步改写为活跃 AP 类计数。
这一步把低筛删除密度问题压成短 AP 中尾素对命中的稀疏性问题。

## 1. AP 删除类

固定几何候选通道 `(j1,j2,u,g)` 与低素 `ell`。低筛删除条件等价为

\[
q\equiv a\pmod \ell,\qquad q,q+g\in T,
\tag{ASR-1}
\]

其中 `T` 是尾素块，`a` 由被筛点位 `j` 唯一决定。因此每个删除类可记为

```text
(ell,j,a,g,u,j1,j2)。
```

若某类中有 `c` 个尾素对，则它贡献 `c` 个 raw AP 删除。真实删除还要按几何候选
`(j1,j2,u,g,q)` 去重。

## 2. 单点化现象

当前高 `P` 样本满足更强恒等式：

```text
D_low = unique_ap = raw_ap = active_AP_classes；
max_AP_pairs_per_class = 1。
```

也就是说，每个活跃 AP 类只命中一个尾素对，不存在同一低素同余类中的多点 AP 聚集。
于是 `LowDeletionAllowance`

\[
D_{\rm low}\le A
\tag{ASR-2}
\]

可进一步替换为

\[
N_{\rm active\ AP}\le A.
\tag{ASR-3}
\]

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_reduction_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_reduction_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
actual=50；
active_classes=50；
AP_classes=3552；
raw_ap=50；
unique_ap=50；
max_class=1；
allowed=1385.963717；
margin=1335.963717；
active_geom_density=0.002800；
active_class_density=0.014077；
allowed_geom_density=0.077602；
singleton=True；
class_pay=True。
```

逐窗口：

```text
p=5003:
  active_classes=5；
  AP_classes=1776；
  active_class_density=0.002815；
  allowed_class_density=0.060094；
  margin=101.727367。

p=10007:
  active_classes=45；
  AP_classes=1776；
  active_class_density=0.025338；
  allowed_class_density=0.720291；
  margin=1234.236350。
```

## 4. 新最窄义务

完整目标族的 `LowDeletionAllowance` 可继续拆为两步：

```text
APSingleton:
  每个活跃 AP 类至多含一个尾素对；

ActiveClassBound:
  活跃 AP 类数不超过允许删除量 A。
```

当前样本两步均成立。下一步应证明：

```text
尾素短差值对在低素模 ell 的同一残基类中不能形成高重数聚集；
或给出活跃 AP 类数的通用上界，直接压低 D_low/G。
```

新增 `prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-structural-contract.md`
后，单点化已被压成结构充分条件：当前所有活跃 AP 类满足

```text
u in {2,3}；
q=ell+residue；
q<2ell；
max(q/ell)=1.099922。
```

因此同一 AP 类中不可能有第二个 `q`。

## 5. 审稿边界

本文仍是显式样本合同，不是全局定理。全局闭合还需要：

```text
完整目标族上的 APSingleton 或高重数 AP 类上界；
完整目标族上的 ActiveClassBound；
失败窗口的有限证书/PDEC/SAE 出口。
```
