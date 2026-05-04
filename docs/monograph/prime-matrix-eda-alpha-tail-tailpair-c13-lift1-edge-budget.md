# AlphaTail `C13` 的 `lift=1` 边缘层去重预算

**状态：** `c13_lift1_edge_budget_sample_closed_global_open`

本文接续 `lift=1` 的 h-layer 分解。前一层已经把当前压力样本中的所有 `lift=1`
候选压到两个边缘整数层：

```text
h=0；
h=u；
mid=0。
```

本节进一步处理 `LOD-EdgeBudget`：把边缘层写成低素块短区间计数，并对重复指向同一
物理删除单元的低筛 witness 去重。

## 1. 边缘层公式

仍记

\[
n:=-(j-j_1)r .
\tag{LEB-1}
\]

### 1.1 头部边缘 `h=0`

若 `n>=0` 且 `u|n`，写

\[
s=\frac{n}{u}.
\tag{LEB-2}
\]

则

\[
a=s,\qquad q=\ell+s .
\tag{LEB-3}
\]

所以对尾区间 `J_c=[Q_-,Q_+]`，

\[
\ell\in L_{\rm low}\cap[Q_- -s,Q_+-s].
\tag{LEB-4}
\]

### 1.2 尾部边缘 `h=u`

若 `n<0` 且 `u|-n`，写

\[
s=\frac{-n}{u}.
\tag{LEB-5}
\]

则

\[
a=\ell-s,\qquad q=2\ell-s .
\tag{LEB-6}
\]

所以

\[
\ell\in L_{\rm low}\cap
\left[
\left\lceil\frac{Q_-+s}{2}\right\rceil,
\left\lfloor\frac{Q_++s}{2}\right\rfloor
\right].
\tag{LEB-7}
\]

两种边缘层还要保留原始低筛非退化条件

\[
a+g\not\equiv0\pmod \ell.
\tag{LEB-8}
\]

## 2. Formal unit 去重

原始 `N1` 按低筛 witness 计数。同一个物理尾素对删除单元可能由多个
`(\ell,j)` witness 指向。实际删除只需要按物理单元付款。

定义边缘 formal unit 为

\[
E=(j_1,j_2,u,g,q).
\tag{LEB-9}
\]

这里 `q` 是候选尾素对的左端，右端为 `q+g`。若多个低素 `ell` 或点位 `j`
给出同一个 `(j1,j2,u,g,q)`，它们只删除同一个 formal unit。

**引理 LEB-1（边缘 formal 去重）。**  
记 `N_edge_raw` 为边缘层低筛 witness 数，`U_edge` 为不同 formal unit 数。
则真实 `lift=1` 边缘删除量满足

\[
D_{1,\rm edge}\le U_{\rm edge}\le N_{\rm edge,raw}.
\tag{LEB-10}
\]

**证明。**  
每个真实边缘删除事件必有某个 witness 产生同一 `q` 与同一 `(j1,j2,u,g)`。
删除对象只取决于 `(j1,j2,u,g,q)`，不取决于它由哪个低素 `ell` 或点位 `j`
见证。因此把全部 witness 投影到 `(LEB-9)` 后不会漏掉真实删除，只会合并重复付款。
故 `D_{1,edge}<=U_edge`。投影像的基数不超过原集合基数，所以
`U_edge<=N_edge_raw`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  raw_edge=541；
  unique_edge=527；
  duplicate_saving=14；
  unique_edge/slack=0.207647；
  unique_margin=2010.963717；
  max_unit_multiplicity=2。
```

逐窗口：

```text
p=5003:
  raw_edge=285；
  unique_edge=271；
  duplicate_saving=14；
  unique_edge/slack=0.396937。

p=10007:
  raw_edge=256；
  unique_edge=256；
  duplicate_saving=0；
  unique_edge/slack=0.137988。
```

逐层最紧者仍为 `p=5003,m=5`：

```text
slack=461.520978；
raw_edge=206；
unique_edge=194；
duplicate_saving=12；
unique_edge/slack=0.420349。
```

## 4. 压缩后的全局接口

前一层接口为

\[
D_1\le N_1=N_{\rm edge}+N_{\rm mid}.
\tag{LEB-11}
\]

本节将边缘项替换为更强的 formal 去重版本：

\[
D_1
\le
U_{\rm edge}+N_{\rm mid}.
\tag{LEB-12}
\]

因此下一步全局义务变为：

```text
LEB-EdgeBudget:
  证明 U_edge 小于 LowSievePreservation slack 的可分配部分。

LOD-MidVoid:
  证明 N_mid=0，或把 N_mid 残项送入 PDEC/SAE。
```

当前压力样本满足

\[
U_{\rm edge}=527<2537.963717.
\tag{LEB-13}
\]

但这仍是样本闭合，不是全局无条件证明。

## 5. 审稿边界

已完成：

```text
边缘层 h=0/h=u 的短区间公式；
formal unit 去重引理；
当前压力样本 raw edge=541 与前一层精确接合；
当前压力样本 unique edge=527，较 raw N1 节省 14。
```

仍未完成：

```text
全局证明 U_edge<=slack；
全局证明 N_mid=0 或给出残项出口；
与 lift>=2 Mod6Void 一起接回 LowSievePreservation。
```
