# Triad-A1 Lift-D：NoDeletion-KL 二分

**状态：** `nodeletion_kl_dichotomy_proved_terminal_certificates_open`

本文承接 `Lift-C`。删除势若发散，支撑密度趋零；剩余最窄硬点是：

```text
sum D_n < infinity,  即 a_n -> 1。
```

这就是 `NoDeletion`：新层几乎不再删除 fiber。本文证明 `NoDeletion` 不能成为新出口；它必须进入：

```text
KL 偏斜累计  => new-layer/profinite PDEC；
KL 偏斜趋零  => CleanKLS/DLS 平坦残余。
```

## 1. NoDeletion 的含义

沿同一 `C_P` 投影塔，令第 `n` 层平均 fiber 幸存率为 `a_n`。`NoDeletion` 是：

\[
a_n\to 1.
\tag{NDK-1}
\]

等价地，大多数活跃旧相位的新增素因子 fiber 几乎全保留。此时支撑集合本身不再给出矛盾，
必须看正式坏窗质量 `g_n` 在 fiber 中如何分布。

对活跃旧相位 `t`，写：

```text
p_{n,t}(b)=g_{n+1}(t,b)/g_n(t)。
```

取结构基准 `mu_{n,t}`。在当前 LHB 同口径支撑上，最自然基准是幸存 fiber 上的均匀分布；
若正式反例分支使用更细的列位移/尾锚权重，则必须登记对应 `mu_{n,t}`，否则不能进入 PDEC 上界。

## 2. KL 成本

定义层 KL：

\[
H_n=\sum_t {g_n(t)\over M}
D_{\rm KL}(p_{n,t}\|\mu_{n,t}).
\tag{NDK-2}
\]

对任意 fiber cap `B`，二元压缩给出：

\[
D_{\rm KL}(p_{n,t}\|\mu_{n,t})
\ge
p_{n,t}(B)\log {p_{n,t}(B)\over \mu_{n,t}(B)}
+
(1-p_{n,t}(B))\log {1-p_{n,t}(B)\over 1-\mu_{n,t}(B)}.
\tag{NDK-3}
\]

因此若某新增层方向 cap 在正质量旧相位上持续获得超过基准的质量差：

```text
p_{n,t}(B) >= mu_{n,t}(B)+epsilon，
```

则该层支付正 KL 成本。这个偏斜正是 refined/new-layer PDEC 的输入。

## 3. 二分

### 3.1 KL 发散

若

\[
\sum_n H_n=\infty,
\tag{NDK-4}
\]

则坏窗质量在新增素因子 fiber 上持续偏离结构基准。有限截断层必能抽取：

```text
direction/cap；
positive excess；
same formal unit g；
refined signature Q_N。
```

这就是 new-layer/profinite PDEC。它不再是无名层叠，而是 PDEC family 的一个高层实例。

### 3.2 KL 可求和

若

\[
\sum_n H_n<\infty,
\tag{NDK-5}
\]

则新增层条件分布相对基准趋平。由 Pinsker：

\[
\|p_{n,t}-\mu_{n,t}\|_{\rm TV}
\le
\sqrt{D_{\rm KL}(p_{n,t}\|\mu_{n,t})/2}.
\tag{NDK-6}
\]

所以对任意固定复杂度的 cylinder/cap，坏窗质量只能按基准比例分散，不能长期形成同向峰。
这正是 CleanKLS/DLS 的 admission 语义：

```text
无低模峰；
无新增层 cap 峰；
无列/尾锚同步；
系数 L2-flat；
同一 formal unit。
```

若 CleanKLS admission 的某项失败，该失败项按 `prime-matrix-cleankls-dls-certificate-contract.md`
回流到 PDEC/SAE/Column/Tail；若全部通过，则交给大筛证书吸收。

## 4. 当前有限审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_nodeletion_kl_gate.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-nodeletion-kl-gate.md/json
```

当前已物化两层审计结果：

```text
gate_counts = {'FiberDeletion': 6}
current_nodeletion_triggered = False。
```

也就是说，当前数据尚未进入 NoDeletion；所有已物化层仍由 fiber 删除支付。

这很重要：`NoDeletion-KL` 是后续层的门控，不是当前层的数值闭合。

### 4.1 KL 见证分解

新增脚本：

```text
experiments/prime_matrix_triad_a1_nodeletion_kl_witness_extractor.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md/json
```

它把条件 KL 拆成可定位的两个部分：

```text
H_cond = E_t KL(B|t || U_B)
       = KL(B || U_B) + I(T;B)。
```

因此 NoDeletion 后的 KL 偏斜不再是黑箱：

```text
KL(B||U_B) 累计
  => 全局新增 residue 偏斜，进入 GlobalResiduePDEC；

I(T;B) 累计
  => 旧相位与新增 residue 同步，进入 refined (old_phase,residue) PDEC；

二者同时趋零
  => CleanKLS/DLS admission。
```

当前两层读数：

```text
gate_route_counts={'FiberDeletionCurrentLayer': 6}
shape_route_counts={'PhaseResidueMutualPDECWitness': 6}
max_global_residue_normalized_kl=0.0388557
max_global_residue_tv_to_uniform=0.186813
min_phase_residue_mutual_normalized_kl=0.412500
max_kl_chain_abs_error=0
```

解释：当前仍由删除势推进；但若未来进入 `a_n->1` 的 NoDeletion 区域，偏斜若不出现在全局
residue 投影上，就必须作为 `(old_phase,residue)` 互信息登记，不能保持无名。

进一步，`prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.md/json` 已把这些互信息原子提升到
下一层相位：

```text
(t,b) -> u=t+bQ。
```

当前 top 原子审计：

```text
atom_count=36；
all_lift_identities_hold=True；
route_counts={
  NoNextLayerDataProfiniteObligation: 24,
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}。
```

已有下一层数据的原子已经分成 `CleanFiberCandidate` 与 `RefinedPDECEntropy`，说明互信息峰继续升层后仍只落入
CleanKLS 或 PDEC 两个终端方向。

再进一步，`prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md/json` 把已有下一层数据的
`12` 个原子全部展开到完整 CRT 相位：

```text
source_route_counts={
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}
route_counts={FullCRTTerminalFarBeyondPxP: 12}
all_terminal_mass_identities_hold=True
all_terminal_phases_gt_p2=True
min_terminal_phase=3659
```

因此当前这些 `NoDeletion-KL` 形状见证在有限已物化层中不会产生 `P×P` 早期零行；它们已经变成远处
finite/profinite PDEC 数据包。

最后，`prime-matrix-triad-a1-no-next-profinite-obligation-resolver.md/json` 解析了剩余的
`NoNextLayerDataProfiniteObligation`：

```text
obligation_count=24
route_counts={FullCRTTerminalFarBeyondPxP: 24}
all_mass_identities_hold=True
all_terminal_phases_gt_p2=True
min_terminal_phase=2323
```

所以当前见证器抽出的 `36` 个 top phase-residue 互信息原子全部已被终端化为远处完整 CRT 相位包：

```text
12 个已有下一层数据原子 + 24 个局部剩余高素 fiber 原子
=> 全部 FullCRTTerminalFarBeyondPxP。
```

再新增 `prime-matrix-triad-a1-all-phase-residue-terminal-audit.md/json` 后，这个结论不再限于 top 原子：

```text
total_nonzero_phase_count=5030
total_terminal_count=14348
all_phase_mass_identities_hold=True
all_terminal_gt_p=True
total_terminal_le_p_count=0
global_min_terminal_phase=59
```

这说明当前已物化 `Q=30030,510510` 两层的全部非零 phase-residue 原子，完整 CRT 终端相位都在第 `P` 行之后。

## 5. 结构闭合链

把 `Lift-C` 与本文合并，Triad-A1 new-layer 塔变成：

```text
ProjectionMonotonicity:
  N=empty；

DeletionPotential:
  sum D_n=infinity => density tends to 0；

NoDeletion:
  sum D_n<infinity => a_n->1；

KL branch:
  sum H_n=infinity => new-layer/profinite PDEC；
  sum H_n<infinity => CleanKLS/DLS admission。
```

这给出一般逻辑链：无限轮筛层叠可以继续，但它不能同时做到：

```text
不删除支撑；
不产生 KL 偏斜；
不满足 CleanKLS 平坦。
```

三者不可兼得。

## 6. 闭合边界

本文完成：

```text
NoDeletion 的 KL/PDEC vs CleanKLS 二分；
cap excess => KL 成本的结构不等式；
当前有限层 NoDeletion 未触发的机器审计；
KL 偏斜的 GlobalResidue / PhaseResidueMutual 见证化。
```

本文未完成：

```text
所有 possible cap/direction 的正式 PDEC 对偶上界 U_CRT<L_PDEC；
CleanKLS/DLS 大筛证书全集；
Sparse/LocalSurvivor 与最终行命题的完全接合。
```

因此下一硬点不再是“无穷层叠是否有规律”，而是两个证书全集：

```text
new-layer PDEC-Cert；
CleanKLS/DLS-Cert。
```
