# AlphaTail `C13` 低筛 AP 删除的提升层刚性

**状态：** `c13_ap_lift_rigidity_sample_closed_global_open`

本文接续 AP-Brun 常数余量。上一层确认 `C_AP<=20` 不能解释为逐 AP 类常数：当前样本存在
单点 AP 类，其逐类所需常数超过 `20`。因此必须研究 AP 删除的更细结构。

## 1. 提升层分解

低筛删除类具有形式

\[
q\equiv a\pmod\ell,
\tag{ALR-1}
\]

其中 `ell` 是低大素，`q` 是尾素。写

\[
q=a+t\ell,\qquad t\ge1.
\tag{ALR-2}
\]

称 `t` 为该 AP 删除事件的提升层。若 `t=1`，则

\[
q=\ell+a,
\tag{ALR-3}
\]

这把删除事件变成低素 `ell` 与尾素 `q` 的近邻素对；再加上 `q+g` 为尾素，实际是三素邻接
结构：

\[
\ell,\quad \ell+a,\quad \ell+a+g.
\tag{ALR-4}
\]

这比普通 AP 素对计数更刚性。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_ap_lift_rigidity_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_lift_rigidity_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
highP-total:
  active=50；
  lift1=50；
  lift_ge2=0；
  possible_lift1=541；
  possible_lift_ge2=1368；
  max_possible_lift=3；
  all_active_lift1=True。
```

逐窗口：

```text
p=5003:
  active=5；
  lift1=5；
  lift_ge2=0；
  possible_lift1=285；
  possible_lift_ge2=704。

p=10007:
  active=45；
  lift1=45；
  lift_ge2=0；
  possible_lift1=256；
  possible_lift_ge2=664。
```

逐层偏移：

```text
p=5003,m=4: offset=18；
p=5003,m=5: offsets=18,54；
p=10007,m=4: offsets=300,450,600,900；
p=10007,m=5: offsets=300,450,600,900。
```

这里 `offset=q-ell`。当前样本的所有真实 AP 删除都来自低素与尾素之间的第一提升邻接。

更强的是，当前样本中 `lift=1` 的纯整数候选总量已经小于低筛保存余量：

```text
p=5003:
  possible_lift1=285 < slack=682.727367；

p=10007:
  possible_lift1=256 < slack=1855.236350。
```

因此当前压力样本若只剩 `lift=1` 删除，则不需要任何 AP-Brun 素对分布输入；纯整数候选数已经
足够付款。

## 3. 对 AP-Brun-C20 的影响

现在可以把 AP 删除分成两类：

```text
Lift-1:
  q=ell+h，形成 ell, ell+h, ell+h+g 的三素邻接结构；

Lift>=2:
  q=a+t ell, t>=2，当前样本无真实删除。
```

因此下一步不应直接证明逐类 `C_AP<=20`，而应走二分：

```text
Lift-1-adjacency:
  优先证明 lift=1 纯整数候选数已小于余量；
  若失败，再证明三素邻接结构总数受 AP-Brun 聚合余量控制；

Lift>=2-void/PDEC:
  证明高提升层为空，或其持续出现触发固定模 CRTDefect/PDEC/SAE。
```

## 4. 审稿边界

已完成：

```text
提升层定义；
当前压力样本所有真实 AP 删除均为 lift=1；
当前压力样本 lift=1 纯整数候选数已小于余量；
把 AP-Brun 局部常数失败解释为单点 lift=1 邻接现象。
```

仍未完成：

```text
全局证明 lift=1 纯整数候选数小于余量，或三素邻接总量上界；
全局排斥 lift>=2 删除，或将其送入 PDEC/SAE；
把该二分接回 C_AP<=20 聚合常数包。
```

所以本文是结构压缩与样本证书，不是行命题最终闭合。
