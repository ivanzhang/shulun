# AlphaTail `C13` 失败见证相位账本

**状态：** `c13_witness_phase_ledger_input_ready_exits_open`

本文接续 `C13` 失败见证障碍，把每个具体尾素对见证进一步提升为相位输入行。核心点是：
`C13` 失败见证不仅是两个尾素 `q,q+g` 同时出现，而且强制二者在原始变量 `d` 上拥有同一个
商数 `u`。这给出比普通素对计数更硬的 CRT/商数锁定结构。

## 1. 商数锁定恒等式

固定形状 `(g,j_1,j_2,u)`，责任线为

\[
d=qu-j_1r.
\tag{WPL-1}
\]

由于

\[
u={-(j_1-j_2)r\over g},
\tag{WPL-2}
\]

对任意见证对 `(q,q+g)` 有

\[
d+j_1r=qu,
\qquad
d+j_2r=u(q+g).
\tag{WPL-3}
\]

因此

\[
q\mid d+j_1r,\qquad q+g\mid d+j_2r,
\tag{WPL-4}
\]

且两个整除事件的商数完全相同：

\[
{d+j_1r\over q}
=
{d+j_2r\over q+g}
=u.
\tag{WPL-5}
\]

## 2. 见证相位输入

对每个失败见证原子记录：

```text
shape_key = (g,j1,j2,u,side);
pair_key  = (g,q,q+g);
d         = q*u - j1*r;
Q_pair    = q(q+g);
tau_pair  = d mod Q_pair;
depth     = d-A 或 B-d，按 side 取端点深度。
```

若同一 `shape_key` 在窗口族中持久产生见证原子，则进入：

```text
PairPhase-PDEC/ColumnCRT。
```

若只孤立出现，则作为：

```text
SAEWitness。
```

该出口仍未排斥 persistent 分支；它只保证所有真实失败都已经变成带有
`Q_pair,tau_pair,depth` 的可审稿输入行。

审稿时还必须区分固定模与变模。具体分流见
`prime-matrix-eda-alpha-tail-tailpair-c13-pairphase-modulus-route.md`：只有同一
`Q_pair=q(q+g)` 重复的原子才可直接进入同模 `PDEC`；变化的 `Q_pair` 必须进入
`MovingModulusDepth-SAE` 或先证明 cross-modulus stitching。

## 3. 可引用引理

**引理 WPL-1（尾素对见证的同商数锁定）。**  
任意 `C13` 失败见证 `(q,q+g)` 满足 `(WPL-3)`--`(WPL-5)`。

**证明。**  
责任区间由固定差值几何给出：`d=qu-j_1r`，所以 `d+j_1r=qu`。又由
`u=-(j_1-j_2)r/g` 得 `(j_2-j_1)r=ug`，从而
`d+j_2r=d+j_1r+(j_2-j_1)r=qu+ug=u(q+g)`。□

**引理 WPL-2（见证相位无损分流）。**  
任意有限窗口族中的 `C13` 失败见证原子，按 `shape_key` 不交分解。持久键给出
`PairPhase-PDEC/ColumnCRT` 输入；非持久键给出 `SAEWitness` 输入。

**证明。**  
`shape_key` 由每个见证原子的固定 gap、点位、商数和端点方向唯一确定，故按键分组为不交
分解。持久键表示同一商数锁定形状反复产生尾素对见证，正是相位缺陷输入；非持久键仅留下
有限见证原子，按 SAE 逐项登记。□

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger.py
```

默认 `C=1.3` 核验命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
```

输出：

```text
atoms 0 shapes 0 quotient_lock_failures 0 route_counts none local_C 1.300000
```

压力测试 `C=1.2`：

```text
atoms 281 shapes 37 quotient_lock_failures 0
route_counts PairPhase-PDEC/ColumnCRT:32,SAEWitness:5
```

这说明脚本在真实失败出现时会生成见证相位原子，并且所有原子均满足同商数锁定。

## 5. 审稿边界

已完成：

```text
见证对的同商数锁定恒等式；
见证原子的 Q_pair/tau_pair/depth 输入格式；
按 shape_key 的 PairPhase-PDEC/SAE 无损分流；
固定模/变模分流接口已独立物化；
样本 C=1.3 无失败相位原子；
C=1.2 压力样本中 281 个原子全部 quotient_lock 通过。
```

仍未完成：

```text
全局证明 C=1.3 下 atom_count=0；
或对 persistent shape_key 构造 U_CRT<L_PDEC 上界；
或对 SAEWitness 给出全局可求和账本。
```

所以本文继续把 `C13` 分支的真实失败出口压缩为可审稿相位输入，但仍不是 Prime Matrix
行命题的最终无条件闭合。
