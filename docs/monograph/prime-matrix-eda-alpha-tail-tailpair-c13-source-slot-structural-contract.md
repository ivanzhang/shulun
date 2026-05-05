# AlphaTail `C13` 前向源槽结构合同

**状态：** `source_slot_structural_sample_closed_forward_open`

本文把 `SkeletonCountBound` 再向下压一层：当前样本中的所有活跃模板骨架都不是任意骨架，
而是满足严格前向链

```text
j > j1 > j2
```

的源槽。该结构把残基、gap 和尾素对位置全部写成显式偏移。

## 1. 前向源槽恒等式

记 `R=|r|`。若活跃类满足

```text
u in {2,3}；
q_lift=1；
j > j1 > j2；
u divides R；
```

则

\[
g=\frac{(j_1-j_2)R}{u},
\tag{SSC-1}
\]

且在 `q<2ell` 的单点化口径下，

\[
q=\ell+\frac{(j-j_1)R}{u},\qquad
q+g=\ell+\frac{(j-j_2)R}{u}.
\tag{SSC-2}
\]

因此一个前向源槽只需记录

```text
(m,j,g,u,j1,j2)
```

而残基由 `(j-j1)R/u` 自动给出。若所有活跃类都落在前向源槽内，则每层的纯组合槽数至多为

\[
2\binom m3,
\tag{SSC-3}
\]

其中因子 `2` 来自 `u in {2,3}`。于是窗口级粗上界为

\[
A(W)\le K\sum_{m\in M}2\binom m3.
\tag{SSC-4}
\]

对 `M={4,5}` 与 `K=8`，右端为 `224`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

总账：

```text
active=50；
sources=28；
slot_ceiling=56；
class_ceiling=448；
exact_source_ceiling=224；
allowed=1385.963717；
forward=True；
gap_id=True；
residue_id=True；
tail_offset=True；
exact_pay=True。
```

逐窗口：

```text
p=5003:
  active=5；
  sources=5；
  coarse slot class ceiling=224；
  allowed=106.727367；
  coarse_pay=False；
  exact_source_ceiling=40；
  exact_source_margin=66.727367。

p=10007:
  active=45；
  sources=23；
  coarse slot class ceiling=224；
  allowed=1279.236350；
  coarse_pay=True；
  exact_source_margin=1095.236350。
```

因此大余量窗口可直接由纯组合前向源槽上界付款；小余量窗口不能只靠
`2*C(m,3)` 粗槽数，需要继续证明实际可激活源槽远少于全部前向槽。

## 4. 剩余接口

该合同把 `SkeletonCountBound` 分成两类：

```text
SSC-G1: ForwardSourceBound，证明完整目标族的活跃类均满足 j>j1>j2 或给出反向槽出口；
SSC-G2: LargeSlackSlotPay，证明 Allow(W)>=K*sum_m 2*C(m,3) 的窗口自动付款；
SSC-G3: SmallSlackSourceCertificate，对未满足粗槽付款的小余量窗口证明实际源槽数 T(W)<=Allow(W)/K。
```

当前最窄剩余是 `SSC-G3`。在当前样本中它只对应 `p=5003`，
实际源槽数为 `5`，而允许源槽预算为 `13.340921`。

新增 `SmallSlackSourceCertificate` 后，`p=5003` 的 `SSC-G3` 已在当前样本内有限闭合：
全部 `224` 个前向低素试验中只有 `5` 个激活，且该枚举与
`active_ap_classes()` 完全一致。全局剩余改为证明小余量窗口族可被有限列举，
或证明统一的源槽稀疏上界。
