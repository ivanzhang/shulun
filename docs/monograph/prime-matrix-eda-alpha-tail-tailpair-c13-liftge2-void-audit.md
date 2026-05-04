# AlphaTail `C13` 的 `lift>=2` 空性审计

**状态：** `c13_liftge2_void_sample_closed_global_open`

本文接续 `lift=1` 纯整数余量。上一层把低筛保存的剩余压缩为 `lift>=2` 删除是否可能出现。
本文审计当前压力样本中 `lift>=2` 候选的空性机制。

## 1. 空性对象

低筛 AP 删除类写成

\[
q=a+t\ell,\qquad t\ge2.
\tag{LGV-1}
\]

若该候选要成为真实删除，必须同时满足：

```text
q 是尾素；
q+g 是尾素；
q 位于对应几何通道区间。
```

因此只要证明 `q` 本身已经合成，就可直接排除该候选。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
highP-total:
  candidates=1368；
  q_tail=0；
  qg_tail=0；
  both_tail=0；
  q_not_tail=1368；
  void_by_q=True；
  q_spf={2: 440, 3: 928}；
  lift_hist={2: 888, 3: 480}。
```

逐窗口：

```text
p=5003:
  candidates=704；
  q_tail=0；
  void_by_q=True。

p=10007:
  candidates=664；
  q_tail=0；
  void_by_q=True。
```

逐层：

```text
p=5003,m=4 : q_spf={2:80, 3:144}；
p=5003,m=5 : q_spf={2:160,3:320}；
p=10007,m=4: q_spf={2:72, 3:144}；
p=10007,m=5: q_spf={2:128,3:320}。
```

## 3. 结构解释

当前样本中的 `lift>=2` 候选只出现在 `t=2` 和 `t=3` 两层。所有候选 `q` 在进入尾素判断前
已经被小素数杀掉：

```text
t=2 层主要由偶性杀掉；
t=3 层主要由 3-整除杀掉。
```

这与前面方阵斜线研究中的“小素因子斜线全杀”规律一致：高提升层不是自由补洞粗数区，而是
被 `2/3` 小素因子刚性锁死。

## 4. 当前 C13 低筛保存链

当前压力样本的链条已变为：

```text
lift=1:
  纯整数候选 N1 小于余量；

lift>=2:
  q 本身均非尾素，且最小素因子只为 2 或 3。
```

所以样本层的 `LowSievePreservation` 已不再需要 AP-Brun 常数输入。

## 5. 审稿边界

已完成：

```text
当前压力样本 lift>=2 候选全空；
空性由 q 本身含 2/3 小素因子给出；
与 lift=1 余量合并后，样本低筛保存分支闭合。
```

仍未完成：

```text
全局证明所有 P>1000 目标窗口中 lift>=2 候选仍被小素因子杀掉；
或证明未被杀掉的高提升候选进入 PDEC/SAE；
把 lift=1 余量与 lift>=2 空性推广到完整目标窗口族。
```

所以本文闭合的是当前压力样本的 `lift>=2` 分支，不是行命题最终闭合。
