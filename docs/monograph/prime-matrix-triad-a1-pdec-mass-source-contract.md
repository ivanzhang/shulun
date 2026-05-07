# Triad-A1 PDEC 质量来源合同

**状态：** `pdec_mass_source_contract_reduces_to_btls_lfte_or_stitching`

本文补上 `PDEC -> BTLS/LFTE` 的缺口：一个 PDEC 帽或坏窗相位集合，只有在先接入同一个 formal unit 的
`M_Q(t)` 投影质量后，才能合法使用边界终端引理或局部 fiber 终端展开。否则它不是可排斥终端，而是
`Multiplicity-Stitching` 口径缺口。

## 1. 合法输入

设

```text
B_P=prod_{ell<P}ell；
C_P subset Z/B_P Z；
Q|B_P。
```

一个 PDEC 分支必须给出同一 formal unit：

```text
Omega=C_P 或其已证明包含的 allowed-set；
tau: Omega -> Z/QZ；
M_Q(t)=#{omega in Omega: tau(omega)=t}。
```

正式坏窗计数 `g(t)` 必须满足：

```text
g(t)<=M_Q(t)。
```

若没有 `S subset Omega` 或等价 attachment，不能把 `M_Q(t)` 作为 `g(t)` 的上界。

## 2. 质量来源三分

对任意 PDEC cap `C subset Z/QZ`：

```text
AttachedMass:
  C cap supp(g) subset C cap supp(M_Q)；
  可进入 BTLS/LFTE/PDEC dual upper。

NoAttachment:
  S subset Omega 未证明；
  回到 Attachment 义务，不能使用 M_Q。

MixedUnit:
  cap 来自多个 Q、多层重复或不同坏窗集合；
  回到 Multiplicity-Stitching / primitive quotient。
```

这条规则防止把不同层、不同坏窗集合或重复物理候选的质量混在一起，误当成同一个 PDEC 向量。

## 3. 与 BTLS/LFTE 的连接

一旦 `AttachedMass` 成立：

```text
若 Q>P 且只需排除前 P 行：
  用 BTLS。因为 C subset supp(M_Q)，全支撑的首端 LocalSurvivor 证书可对子集继承。

若抽出具体原子 u：
  用 LFTE 局部展开 u+yQ 的剩余高素 fiber。

若存在 w<=P：
  这不是远处 PDEC，而是真实早期零行硬点，必须直接产生反例矛盾。
```

所以 PDEC 帽不能绕过边界检查；它要么继承 LocalSurvivor，要么给出真实早期相位。

## 4. Lift 单调继承

若 `Q>P` 且 `Q'=rQ`，新相位写成

```text
v=u+bQ。
```

若 `v<=P`，则必有 `b=0` 且 `u=v<=P`。因此旧层 `u` 的 `y=0` LocalSurvivor 见证会直接继承到
任意 lift 子相位：

```text
BTLS closed at Q
=> BTLS closed for every refinement Q'=rQ,
   as long as the refinement stays inside pi^{-1}(supp(M_Q)).
```

这解释了为什么 ForcedPersistent cap 升层后不能重新打开前 `P` 行出口。升层只能改变远处 fiber、
删除势、KL 偏斜或 CleanKLS 入口，不能把已经关闭的首端行搬回前 `P` 行。

## 5. 当前路由

当前 `Q=2310` DualCap 三族可按此合同读成：

```text
SparseCap:
  已由 SparseLocalSurvivor 审计关闭 P×P 出口；
  剩余 finite PDEC packet 在 P 之后。

PersistentCap:
  cap subset supp(M_Q)；
  全支撑 BTLS 关闭 P×P 出口；
  剩余进入 ColumnTail/TailAnchor PDEC 或 CleanKLS。

ForcedPersistentByDensityBarrier:
  旧层 cap subset supp(M_Q)，BTLS 先关闭 P×P 出口；
  lift 到 Q'=30030 后只产生删除/KL/CleanKLS 义务。
```

对应机器审计为：

```text
experiments/prime_matrix_triad_a1_pdec_mass_source_router.py
docs/monograph/prime-matrix-triad-a1-pdec-mass-source-router.md/json
```

## 6. 闭合边界

本文完成的是接口约束：

```text
PDEC cap
=> AttachedMass
=> BTLS/LFTE/PDEC upper
or NoAttachment/MixedUnit
=> Stitching。
```

它没有完成：

```text
所有 PDEC family 的 U_CRT<L_PDEC；
ColumnTail/TailAnchor 的终端排斥；
CleanKLS/DLS 大筛证书。
```

但它排除了一个重要误用：不能把抽象 PDEC 帽直接当作早期零行候选。帽必须先说明它数的是同一
`C_P` 中的哪些相位质量；一旦说明，前 `P` 行出口就被 BTLS 或 LFTE 接管。
