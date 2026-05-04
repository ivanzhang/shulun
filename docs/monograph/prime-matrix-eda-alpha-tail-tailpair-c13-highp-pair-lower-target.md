# AlphaTail `C13` 高 P 的固定 gap 素对下界目标

**状态：** `c13_highp_pair_lower_target_open`

本文接续高 `P` 的 `D2` 余量账本。上一层把预算义务写成

\[
\mathrm{Cap}_{\rm even}\le D_2=M_2-B_2.
\tag{PLT-1}
\]

本文把 `(PLT-1)` 进一步转成固定 gap 尾素对的精确下界目标。

## 1. 等乘数素对恒等式

固定窗口 `(P,B,r)` 与点数 `m`。若尾素对事件在两个点位 `j_1<j_2` 上发生，且乘数相等，
则存在正整数 `u` 使

\[
d+j_1r=qu,\qquad d+j_2r=(q+g)u,
\tag{PLT-2}
\]

其中

\[
g={-(j_1-j_2)r\over u}.
\tag{PLT-3}
\]

因此候选起点唯一：

\[
d=qu-j_1r.
\tag{PLT-4}
\]

记 `G_m^L` 为所有满足 `(PLT-2)`、`d in I_m`、且 `d` 通过低大素筛的尾素对计数和。则

\[
M_{2,m}^{=}=G_m^L.
\tag{PLT-5}
\]

非等乘数部分记为 `E_m>=0`，于是

\[
M_{2,m}=G_m^L+E_m.
\tag{PLT-6}
\]

**引理 PLT-1（高 P 素对下界充分条件）。**  
若对目标窗口族有

\[
\sum_m G_m^L
\ge
\sum_m \left(B_{2,m}+\mathrm{Cap}_{{\rm even},m}\right),
\tag{PLT-7}
\]

则该窗口满足 `HighP-D2-Lower`。

**证明。**  
由 `(PLT-6)` 与 `E_m>=0`，

\[
\sum_m M_{2,m}\ge \sum_m G_m^L.
\]

若 `(PLT-7)` 成立，则

\[
\sum_m M_{2,m}
\ge
\sum_m B_{2,m}+\sum_m \mathrm{Cap}_{{\rm even},m},
\]

等价于

\[
\sum_m(M_{2,m}-B_{2,m})
\ge
\sum_m\mathrm{Cap}_{{\rm even},m}.
\]

左端就是 `D2`，故得到 `(PLT-1)`。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  Cap_even      = 7476.160000；
  B2            = 7845.876283；
  required_M2   = 15322.036283；
  M2            = 17810；
  margin        = 2487.963717；
  equal         = 17810；
  non_equal     = 0；
  geom_upper    = 17860；
  required/M2   = 0.860305；
  required/geom = 0.857897；
  low/geom      = 0.997200。
```

逐层最紧者为：

```text
p=5003,m=4:
  required/M2   = 0.907437；
  required/geom = 0.907056；
  low/geom      = 0.999580。
```

## 3. 当前洞察

当前高 `P` 样本有两个关键特征：

```text
1. non_equal=0：
   二阶实际矩全部来自等乘数固定 gap 尾素对。

2. low/geom 接近 1：
   固定 gap 几何候选尾素对几乎全部通过低大素筛。
```

因此 `HighP-D2-Lower` 的最窄目标已不是改进除数 envelope，而是证明：

\[
G_m^L
\ge
B_{2,m}+\mathrm{Cap}_{{\rm even},m}.
\tag{PLT-8}
\]

这可以拆成两步：

```text
PairLower:
  几何截断短区间中的固定 gap 尾素对数足够多；

LowSievePreservation:
  这些候选被低大素筛删除的比例不能超过剩余余量。
```

## 4. 审稿边界

已完成：

```text
HighP-D2-Lower 精确化为固定 gap 素对下界；
等乘数候选 d 的唯一性接入预算条件；
当前压力样本给出所需下界比例和最紧层。
```

仍未完成：

```text
全局证明 PairLower；
全局证明 LowSievePreservation；
或证明任一失败都会触发 PDEC/SAE/ColumnCRT 出口。
```

所以本文没有闭合行命题；它把当前唯一可攻硬点压缩成
`HighP-PLT = PairLower + LowSievePreservation`。
