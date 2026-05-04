# AlphaTail `C13` 的 `lift=1` 纯整数候选余量

**状态：** `c13_lift1_integer_margin_sample_closed_global_open`

本文接续提升层刚性审计。目标是把 `lift=1` 分支从素数分布问题降为纯整数候选计数问题。

## 1. 纯整数候选

低筛 AP 删除类写成

\[
q\equiv a\pmod \ell,\qquad q=a+t\ell.
\tag{LIM-1}
\]

当 `t=1` 时，候选 `q` 被唯一确定为

\[
q=\ell+a.
\tag{LIM-2}
\]

因此每个删除类最多贡献一个 `lift=1` 整数候选。定义

\[
N_1:=
\#\{(\text{channel},\ell,j):\ell+a\in J_{\rm channel}\}.
\tag{LIM-3}
\]

这里不要求 `q` 或 `q+g` 为素数，所以真实 `lift=1` AP 删除量 `D_1` 满足

\[
D_1\le N_1.
\tag{LIM-4}
\]

若再记 `D_{\ge2}` 为所有 `t>=2` 的真实 AP 删除量，则

\[
D_{\rm low}\le N_1+D_{\ge2}.
\tag{LIM-5}
\]

**引理 LIM-1（lift=1 纯整数付款）。**  
若

\[
N_1\le G^{\rm geom}-R
\quad\text{且}\quad
D_{\ge2}=0,
\tag{LIM-6}
\]

则 `LowSievePreservation` 成立。

**证明。**  
由 `(LIM-5)` 与 `D_{\ge2}=0` 得 `D_low<=N_1`。再由 `(LIM-6)` 得

\[
G^L=G^{\rm geom}-D_{\rm low}
\ge G^{\rm geom}-N_1
\ge R.
\]

这正是 `HighP-PLT` 所需的低筛保存条件。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_integer_margin.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_integer_margin.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  possible_lift1=541；
  margin=1996.963717；
  possible_lift1/slack=0.213163；
  possible_lift_ge2=1368；
  active_lift1=50；
  active_lift_ge2=0。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  possible_lift1=285；
  margin=397.727367；
  possible_lift1/slack=0.417443。

p=10007:
  slack=1855.236350；
  possible_lift1=256；
  margin=1599.236350；
  possible_lift1/slack=0.137988。
```

逐层最紧者为 `p=5003,m=5`：

```text
slack=461.520978；
possible_lift1=206；
margin=255.520978；
possible_lift1/slack=0.446350。
```

## 3. 剩余压缩

当前样本的 `lift=1` 分支已经由纯整数候选数付款，不需要 AP-Brun 常数或素对分布输入。剩余
只在 `lift>=2`：

```text
当前样本:
  possible_lift_ge2=1368；
  active_lift_ge2=0。
```

所以下一硬点变为：

```text
LiftGE2-Void/PDEC:
  证明 t>=2 候选不可能同时满足 q,q+g 为尾素数；
  或证明持续出现会形成固定模 CRTDefect/PDEC/SAE。
```

## 4. 审稿边界

已完成：

```text
lift=1 纯整数候选上界；
当前压力样本中 lift=1 分支逐窗口和逐层付款；
把低筛保存的剩余压缩为 lift>=2。
```

仍未完成：

```text
全局证明 N1<=G_geom-R；
全局证明 D_ge2=0，或给出 PDEC/SAE 出口；
把该二分应用到全部 P>1000 目标窗口。
```

所以本文闭合的是当前样本的 `lift=1` 分支，不是行命题最终闭合。
