# AlphaTail `C13` 的 `lift=1` offset/h-layer 分解

**状态：** `c13_lift1_offset_decomposition_sample_closed_global_open`

本文接续 `lift=1` 纯整数候选余量，把候选 `q=\ell+a` 的剩余自由度进一步分解为
同余 offset 与提升层 `h`。目标不是宣称行命题闭合，而是把 `N_1` 的全局上界压成
可逐项证明的边缘低素数区间计数。

## 1. 精确提升层恒等式

固定一个低筛删除 channel

\[
c=(j_1,j_2,u,g,j),
\]

其中 `u` 为乘数、`g` 为固定 gap，并令

\[
n:=-(j-j_1)r .
\tag{LOD-1}
\]

低筛 AP 条件为

\[
q\equiv a \pmod{\ell},\qquad
u a\equiv n\pmod{\ell},\qquad 0\le a<\ell .
\tag{LOD-2}
\]

`lift=1` 等价于

\[
q=\ell+a .
\tag{LOD-3}
\]

由 `(LOD-2)` 存在整数 `h` 使

\[
u a=n+h\ell .
\tag{LOD-4}
\]

于是

\[
q=\ell+a=\frac{(u+h)\ell+n}{u}.
\tag{LOD-5}
\]

因此对 channel 的允许尾素区间 `J_c=[Q_-,Q_+]`，`lift=1` 候选必须满足

\[
Q_-\le \frac{(u+h)\ell+n}{u}\le Q_+,
\qquad
h\ell+n\equiv0\pmod u,
\tag{LOD-6}
\]

并同时满足 `0<=a<ell`。这给出完全确定的 h-layer 门控公式。

**引理 LOD-1（lift=1 h-layer 精确化）。**  
对固定 channel，`lift=1` 候选数等于

\[
\sum_{0\le h\le u}
\#\left\{\ell\in L_{\rm low}:
\ell\in I_h(c),\ h\ell+n\equiv0\pmod u
\right\},
\tag{LOD-7}
\]

其中

\[
I_h(c)=
\left[
\left\lceil\frac{uQ_- - n}{u+h}\right\rceil,\,
\left\lfloor\frac{uQ_+ - n}{u+h}\right\rfloor
\right]
\tag{LOD-8}
\]

再与 `0<=a<ell` 的线性不等式相交。

**证明。**  
`(LOD-2)` 与 `0<=a<ell` 给出唯一整数 `h=(ua-n)/ell`。代入 `q=ell+a` 得
`(LOD-5)`；尾区间限制给出 `(LOD-8)`，整除性给出 `h ell+n == 0 mod u`。
反向若 `(LOD-7)` 中的 `ell,h` 成立，则
`a=(n+h ell)/u` 为整数且满足 `0<=a<ell`，所以 `q=ell+a` 是对应 AP 类的
`lift=1` 候选。□

## 2. 两个边缘层

公式 `(LOD-7)` 中最有结构的两层是：

```text
h=0:
  n>=0 且 u|n，
  q=ell+n/u。

h=u:
  n<0 且 u|n，
  q=2ell-|n|/u。
```

它们分别是低素块的头部平移和尾部镜像平移。中间层 `0<h<u` 才是真正的
分数同余自由层。

当前压力样本中所有实际 `lift=1` 候选均落在这两个边缘层：

```text
h0_head_integer = 277；
hu_tail_integer = 264；
hmid_fractional = 0。
```

这说明 `N1` 在样本中不是自由 CRT 随机量，而是低素块沿少数小 offset 的边缘投影。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_offset_decomposition.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_offset_decomposition.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  lift1=541；
  exact_hgate=541；
  edge=541；
  mid=0；
  lift1/slack=0.213163；
  lift1_margin=1996.963717；
  h0_head_integer=277；
  hu_tail_integer=264；
  identity=True。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  lift1=285；
  edge=285；
  mid=0；
  lift1/slack=0.417443；
  lift1_margin=397.727367。

p=10007:
  slack=1855.236350；
  lift1=256；
  edge=256；
  mid=0；
  lift1/slack=0.137988；
  lift1_margin=1599.236350。
```

逐层最紧仍为 `p=5003,m=5`：

```text
slack=461.520978；
lift1=206；
edge=206；
mid=0；
lift1/slack=0.446350；
lift1_margin=255.520978。
```

主要边缘 offset：

```text
p=5003,m=5:
  edge 36:60, 72:48, 108:40, 144:24。

p=10007,m=5:
  edge 900:56, 300:48, 450:40, 600:24。
```

## 4. 全局证明接口

`LOD-1` 把剩余全局义务压成两项：

```text
LOD-MidVoid:
  证明目标窗口族中 0<h<u 的中间 h 层为空，
  或把中间层残余送入 PDEC/SAE。

LOD-EdgeBudget:
  对 h=0 与 h=u 的边缘平移低素块计数给出统一上界，
  并证明总 N1 小于 LowSievePreservation slack。
```

在 `LOD-EdgeBudget` 中可使用的确定形式为

\[
N_1
\le
\sum_c
\#\{\ell\in L_{\rm low}:\ell+s_c\in J_c\}
+
\sum_c
\#\{\ell\in L_{\rm low}:2\ell-s_c\in J_c\}
+
N_{\rm mid},
\tag{LOD-9}
\]

其中 `s_c=|n|/u`，第一项对应 `h=0`，第二项对应 `h=u`。当前样本中
`N_mid=0`。

## 5. 审稿边界

已完成：

```text
lift=1 候选的精确 h-layer 恒等式；
当前压力样本中 N1=541 的复现；
证明样本实际候选全部为边缘整数层，非中间分数层；
证明实际低素块门控 exact_hgate 与原始 lift1 计数逐项一致。
```

仍未完成：

```text
全局 LOD-MidVoid；
全局 LOD-EdgeBudget；
将该 N1 上界与 lift>=2 Mod6Void 一起接回 HighP-D2-Lower。
```

所以本文是 `lift=1` 分支的结构压缩，不是行命题的最终无条件闭合。
