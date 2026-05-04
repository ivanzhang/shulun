# AlphaTail 端点 PDEC 的镜像闭合约束

**状态：** `endpoint_mirror_constraint_routing_open`

本文把端点 PDEC 上界所需的第一类额外刚性——端点镜像——写成可审稿约束。结论不是
`PDEC` 排斥，而是：

```text
若端点坏窗集合可使用 mirror 约束，则必须镜像闭合；
若不镜像闭合，则缺失镜像质量本身成为 MirrorImbalanceDefect/PDEC-or-SAE。
```

## 1. 同窗口端点镜像

对窗口 `w=(p,B,r,m)`，记有效端点区间

\[
I_m=[L_w,R_w]\cap\mathbb Z.
\]

端点尖峰责任区间为

\[
D=[D^-,D^+]\subset I_m.
\]

定义同窗口反射

\[
\mathfrak m_w(D)
=
[L_w+R_w-D^+,\ L_w+R_w-D^-].
\tag{EMC-1}
\]

模 `Q` 的端点相位

\[
\tau_Q(D)=(D^-\bmod Q,\ D^+\bmod Q)
\]

在镜像下变为

\[
\tau_Q(\mathfrak m_w(D))
=
(L_w+R_w-D^+\bmod Q,\ L_w+R_w-D^-\bmod Q).
\tag{EMC-2}
\]

## 2. 镜像准入条件

对持久端点键 `K`，设同一窗口中的观测相位集为

\[
T_{K,w}(Q)=\{\tau_Q(D_e):\mathcal K(e)=K,\ e\in w\}.
\]

若要在 `PDEC-Cert` 中使用镜像约束，必须满足

\[
\tau_Q(D)\in T_{K,w}(Q)
\quad\Longrightarrow\quad
\tau_Q(\mathfrak m_w(D))\in T_{K,w}(Q).
\tag{EMC-3}
\]

否则，镜像闭合失败不能当作上界约束使用，必须登记为

```text
MirrorImbalanceDefect(K,w,Q).
```

## 3. 引理：镜像约束不可越界

**引理 EMC-1（镜像约束准入）。**  
`mirror` 行进入 `A,b,E,e` 上界证书的必要条件是 `(EMC-3)`；若 `(EMC-3)` 失败，
则该持久键必须转入 `MirrorImbalanceDefect/PDEC-or-SAE`，不能继续用镜像抵消估计。

**证明。**  
`mirror` 约束的含义是同一坏窗集合对反射映射封闭，且反射后的端点质量仍属于同一证书口径。
若某个观测端点相位的镜像相位不在同一 `T_{K,w}` 中，则把两者配对会引入不存在的坏窗质量；
这等价于使用了不属于同一集合 `S_K` 的约束，违反 `H4-PDEC` 证书模板中“同一坏窗集合”
要求。因此镜像行不可准入。缺失镜像伙伴本身就是端点方向偏置，可作为新的有向端点缺陷或
有限 SAE 项登记。□

## 4. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_mirror_constraint_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_mirror_constraint_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本给出两类：

```text
MIRROR_CONSTRAINT_ADMISSIBLE:
  9 个持久键，每个 self_mirror_count=2, missing_mirror=0；

MIRROR_IMBALANCE_DEFECT/PDEC_OR_SAE:
  5 个持久键，missing_mirror=2。
```

解释：

```text
自镜像键允许登记 mirror 约束，但自镜像本身不产生抵消；
缺镜像键不能使用 mirror 上界，必须回流到 MirrorImbalanceDefect/PDEC-or-SAE。
```

## 5. 对当前硬点的影响

结合 Parseval 地板，端点上界路线被进一步压缩为：

```text
1. 对 mirror-closed/self-mirror 键：
   mirror 只给准入，不给足够抵消；仍需 column/tail-anchor/Rankin 刚性。

2. 对 missing-mirror 键：
   直接进入 MirrorImbalanceDefect/PDEC-or-SAE；
   若该缺陷持久，则是新的有向端点 CRT 缺陷；
   若非持久，则进入 SAE。
```

因此镜像刚性不是终局闭合，但它排除了错误使用镜像抵消的路线，并把一部分端点键转入更窄的
`MirrorImbalance` 出口。

## 6. 审稿边界

已完成：

```text
同窗口端点镜像公式；
mirror 约束准入条件；
缺镜像伙伴的强制路由；
样本中 mirror-admissible 与 mirror-imbalance 键的分类。
```

未完成：

```text
MirrorImbalanceDefect 的全局排斥；
self-mirror 键上的 column/tail-anchor/Rankin 上界；
同频率 U_CRT<L_PDEC 的最终余量。
```
