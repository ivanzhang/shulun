# Triad-A1 Phase-Residue 互信息无循环引理

**状态：** `phase_residue_mutual_no_cycle_reduction_terminal_open`

本文承接 `prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md`。该见证器显示，当前升层中的 KL 偏斜主要不是全局
residue 质量峰，而是旧相位 `T` 与新增 residue `B` 的互信息：

```text
H_cond=KL(B||U_B)+I(T;B)。
```

本文把 `I(T;B)` 分支改写成无循环结构：它若持久，就必然生成更细轮层上的普通相位/PDEC 签名；若不持久，就进入
CleanKLS 的平坦条件。

## 1. 互信息峰就是新相位原子

设 `Q'=rQ`。旧相位 `t mod Q` 与新增 residue `b mod r` 唯一对应新相位：

```text
u=t+bQ mod Q'。
```

因此任何 `(old_phase,residue)` 峰都不是新型对象，而是 `Q'` 层的一个 cylinder atom。若某组原子在正式坏窗质量中承担
正比例超额，则它已经是 refined PDEC 的相位支撑。

## 2. 不能同层循环

互信息峰若在 `Q->Q'` 出现，下一步只有三种归宿：

```text
A. 该新相位在 Q' 层继续持久过载
   => 普通 refined PDEC / column-tail / next-lift 输入；

B. 该新相位在下一层 fiber 中被大量删除
   => 删除势 D_n 增长，回到 Sparse/LocalSurvivor/PDEC；

C. 该新相位不再集中，质量跨许多 residue 分散
   => I(T;B) 下降，进入 CleanKLS/DLS admission。
```

所以 phase-residue 互信息不能作为第四终端存在。它每出现一次，就把模数从 `Q` 提升到 `Q'`，并成为下一层的普通相位账本。

## 3. 无限层滤过形式

令 `F_n` 是模 `Q_n` 的相位分割，`F_{n+1}` 由 `F_n` 加上新增 residue 细化。设正式坏窗质量在这些分割上的投影为
`g_n`。每层信息增量可写为：

```text
H_n = D(g_{n+1} || lift(g_n) * uniform_new_residue | F_n)。
```

若

```text
sum H_n = infinity，
```

则某些有限层 cylinder family 持续承担正信息成本。截断到第一批累计成本超过阈值的层，就得到有限模数
`Q_N` 上的偏斜签名：

```text
finite cylinder support；
positive excess；
same formal unit g_N；
refined PDEC input。
```

若

```text
sum H_n < infinity，
```

则 `H_n->0`。由 Pinsker，每个固定复杂度的新增 cylinder/cap 相对基准趋平，不能长期承担同向覆盖责任。这正是
CleanKLS/DLS 的 `K9 no fiber mutual info` 准入。

## 4. 与当前审计的连接

当前见证器读数：

```text
gate_route_counts={'FiberDeletionCurrentLayer': 6}
shape_route_counts={'PhaseResidueMutualPDECWitness': 6}
max_global_residue_normalized_kl=0.0388557
min_phase_residue_mutual_normalized_kl=0.412500
```

所以当前不是 NoDeletion 终端，而是删除势仍在推进；但若未来删除停止，同类互信息峰不能无名逃逸：

```text
固定/嵌套复现 => profinite/refined PDEC；
不复现       => CleanKLS/DLS；
下一层删除   => 删除势/Sparse/LocalSurvivor。
```

## 5. 原子提升审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_phase_residue_mutual_atom_lift_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.md/json
```

该审计直接核验：

```text
u=t+bQ；
M_{Q'}(u)=atom_mass。
```

当前结果：

```text
atom_count=36；
with_next_layer_count=12；
all_lift_identities_hold=True；
route_counts={
  NoNextLayerDataProfiniteObligation: 24,
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}。
```

已有下一层数据的 `12` 个原子全部没有第四出口：

```text
P=19:
  6 个代表原子在 Q=30030->510510 的下一 fiber 上全支撑且均匀；
  next_normalized_kl=0；
  => CleanKLS 候选。

P=23:
  6 个代表原子在下一 fiber 上全支撑但有单 residue 峰；
  next_normalized_kl=0.309287；
  top residue share=19/35；
  => refined PDEC entropy 或继续升层。
```

这给出一个很硬的结构读数：互信息峰在下一层不是消失成无名噪声，而是明确分成“趋平”和“继续偏斜”。
趋平进入 CleanKLS；继续偏斜进入 refined/profinite PDEC 或下一次升层。

## 6. 完整 CRT 终端展开

新增脚本：

```text
experiments/prime_matrix_triad_a1_phase_residue_full_crt_terminal_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md/json
```

该审计把已有下一层数据的 `12` 个原子继续展开到完整 CRT 终端相位：

```text
atom u at Q'；
next residue phase v=u+sQ'；
terminal phase w=v+y*nextQ；
completion_count(v)=#{y: w 是完整 CRT 零行相位}。
```

当前结果：

```text
rows_with_next_count=12；
source_route_counts={
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}；
route_counts={FullCRTTerminalFarBeyondPxP: 12}；
all_terminal_mass_identities_hold=True；
all_residue_mass_identities_hold=True；
all_terminal_phases_gt_p=True；
all_terminal_phases_gt_p2=True；
min_terminal_phase=3659；
min_terminal_phase_over_p2=10.1357。
```

这说明当前已有下一层数据的 clean/refined 两类互信息原子，全部已经是远处完整 CRT 零行相位包。
它们可以进入 finite/profinite PDEC 账本，但不能作为 `P×P` 内早期零行。

## 7. NoNext ProfiniteObligation 解析

新增脚本：

```text
experiments/prime_matrix_triad_a1_no_next_profinite_obligation_resolver.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-no-next-profinite-obligation-resolver.md/json
```

上一节只处理了已有下一层 `m_vector` 的 12 个原子。剩余 24 个原子原先标记为
`NoNextLayerDataProfiniteObligation`。新解析器不生成整层巨大 `m_vector`，而是直接对每个原子局部展开：

```text
atom u at Q'；
remaining high primes R={ell<P: ell does not divide Q'}；
terminal phase w=u+yQ'；
completion_count(u)=#{y mod prod(R): w 完整覆盖}。
```

当前结果：

```text
obligation_count=24；
resolved_count=24；
route_counts={FullCRTTerminalFarBeyondPxP: 24}；
all_mass_identities_hold=True；
all_terminal_phases_gt_p=True；
all_terminal_phases_gt_p2=True；
min_terminal_phase=2323；
min_terminal_phase_over_p2=8.03806。
```

因此当前 top 互信息原子的早期出口已经全部关闭：

```text
已有下一层数据的 12 个 => FullCRTTerminalFarBeyondPxP；
无下一层数据的 24 个   => 局部剩余高素 fiber 展开后 FullCRTTerminalFarBeyondPxP。
```

这不是最终行命题闭合；它关闭的是当前 `NoDeletion-KL` 见证器抽出的 top phase-residue 互信息原子。

## 8. 全 PhaseResidue 原子终端审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_all_phase_residue_terminal_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-all-phase-residue-terminal-audit.md/json
```

这一步不再只看 top KL 原子，而是把当前已物化 `Q=30030` 与 `Q=510510` 的全部非零相位逐一展开到完整 CRT
终端：

```text
M_Q(u)>0；
R={ell<P: ell does not divide Q}；
terminal row w=u+yQ, y mod prod(R)；
M_Q(u)=#{y: w 完整覆盖}。
```

当前结果：

```text
total_nonzero_phase_count=5030；
total_terminal_count=14348；
all_total_mass_identities_hold=True；
all_phase_mass_identities_hold=True；
all_terminal_gt_p=True；
all_terminal_gt_p2=False；
total_terminal_le_p_count=0；
total_terminal_le_p2_count=2；
global_min_terminal_phase=59。
```

`all_terminal_gt_p=True` 是行命题相关读数：当前有限升层的全部 phase-residue 原子都不会在第 `P` 行以内形成零行。
`all_terminal_gt_p2=False` 是预期现象，例如 `P=23` 的第 `59` 行零行；它仍满足 `59>P`，不反驳行命题。

所以当前有限层结论已经从：

```text
top 互信息原子早期出口关闭
```

升级为：

```text
当前已物化 Q=30030,510510 的全部非零 phase-residue 原子早期出口关闭。
```

## 9. 闭合边界

本文完成：

```text
PhaseResidueMutual 不是新终端；
互信息峰等价于提升层 cylinder atom；
无限换壳被压成 PDEC 或 CleanKLS；
当前 top 互信息原子的提升恒等式和下一层二分已物化；
已有下一层数据的互信息原子全部展开为远处完整 CRT 终端相位；
无下一层数据的 top 互信息原子也被局部剩余高素 fiber 解析为远处完整 CRT 终端相位；
当前已物化升层的全部非零 phase-residue 原子都已证明终端相位 >P。
```

本文未完成：

```text
refined/profinite PDEC 的 U_CRT<L_PDEC 证书；
CleanKLS/DLS 的最终大筛证书；
Sparse/LocalSurvivor 的全集证书。
```

因此它关闭的是 `I(T;B)` 的无名循环口，不是最终行命题闭合。
