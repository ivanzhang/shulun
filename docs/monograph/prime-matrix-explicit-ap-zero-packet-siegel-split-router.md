# Prime Matrix Explicit AP Zero-packet / Siegel Split Router

**状态：** `explicit_ap_zero_packet_split_into_siegel_and_nonreal_phase_branches_open`

本步继续攻击 `ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2`，把它拆成两个不可混淆的解析硬分支：实例外/Siegel 零点在 square-scale 的危险半类偏置，以及非实零点包在单个 residue evaluation 方向上的相位同向集中。低阶项已被分离为后续显式常数账本。当前没有证明这两条主分支，因此行/列命题仍未无条件闭合；但无名零包出口已被替换为可审计的 Siegel/非实相位二分。

```text
siegel_branch_closed=false
nonreal_branch_closed=false
trivial_terms_isolated=true
classical_inputs_sufficient=false
row_column_unconditional_closed=false
next_direct_attack_target=ExplicitAPZeroPacketSiegelNonrealDichotomyAtP2
```

## 1. 零点包分裂

| component | scale at x=P^2 | role |
| --- | --- | --- |
| `principal main term` | `P` | 必须被所有误差包严格小于，才能推出 theta(P^2;P,a)>0。 |
| `real exceptional / Siegel zero` | `P^(2 beta-1)/beta = P exp(-2 lambda)/beta when beta=1-lambda/log P` | 若 beta 距 1 只有 O(1/log P)，该项与主项同阶；危险半类不能靠平均或容量自动排除。 |
| `nonreal zero packet` | `signed sum of P^(2 rho-1)/rho over characters and ordinates` | 总绝对值或 L2 能量不足以闭合；需要逐 residue 的相位抵消，排除同向集中。 |
| `trivial zeros / imprimitive / finite terms` | `lower-order once the two genuine zero packets are controlled` | 不是当前主障碍，但必须保留在最终显式常数账本中。 |

## 2. 分支账本

| branch | needed input | current status | why hard |
| --- | --- | --- | --- |
| `SiegelExceptionalBiasExclusionAtSquareScale` | 排除 square-scale 危险半类中的实零偏置，或接受已认证的无 Siegel 零点/强 Linnik-2 型输入。 | not proved in corpus; no peer-accepted unconditional no-Siegel-zero theorem is available | 实零项在 x=P^2 仍可与主项同阶，Deuring-Heilbronn 排斥其它零点但不直接删除该偏置。 |
| `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2` | 证明所有非实零点包在每个 a mod P 上不能相位同向吃掉主项。 | not proved in corpus; GRH-shape, BV, full CRT average, and energy capacity are insufficient | 点态 residue 方向是 character simplex 的 rank-one evaluation；平均估计可留下单个异常方向。 |
| `TrivialAndFiniteExplicitFormulaTermsBelowMainMarginAtP2` | 在前两项给出主项余量后，用显式公式常数账本吸收低阶项。 | isolated as bookkeeping, not the frontier blocker | 没有前两项的正余量时，低阶项账本无法单独产生正性。 |
| `structural fallback` | 若解析零包分裂失败，反例链必须回到 PDEC scope、signed payload、ExactUV、RatePreservation 或 DStructure。 | named fallback only; not a proof of row/column theorem | 有限 CRT 周期只给位置相位约束，不能生成角色零点相位或 actual signed payload 的全局抵消。 |

## 3. 外部输入状态

| input | status | effect here |
| --- | --- | --- |
| `Dirichlet character explicit formula` | standard external theorem | 提供零点包分解，但不自动给 P^2 阈值正性。 |
| `classical zero-free region and Deuring-Heilbronn repulsion` | standard external theorem family | 可组织 Siegel 分裂，但常数尺度仍不足以证明每个 residue 在 P^2 前命中。 |
| `Bombieri-Vinogradov / complete CRT uniformity` | standard external theorem or identity | 平均控制，不排除单个 rank-one residue evaluation 方向。 |
| `GRH` | unproved conjecture | 即便使用 GRH-shape O(P log^2 P)，仍大于 P 级主项，不能直接闭合 sharp P^2 正性。 |
| `No Siegel zero for all prime moduli` | open; not peer-certified as an unconditional theorem | 若加上强常数量化，能删除实例外偏置分支的一大部分，但仍需处理非实零包。 |
| `Linnik exponent 2 / pointwise least prime <= P^2` | open-level target in this corpus | 等价闭合列侧 AP 分支；不能作为已证引理回用。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousZeroPacketHardPointImported` | `true` | `false` | 上一层已把 rank-one AP 正性压成显式零点包小于主项。 | ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2 |
| `ZeroPacketSiegelNonrealSplitClosed` | `true` | `true` | 零点包被拆成实例外/Siegel 偏置、非实相位集中和低阶项三块；没有保留无名误差。 | ExplicitAPZeroPacketSiegelNonrealDichotomyAtP2 |
| `SiegelExceptionalBiasBranchClosed` | `false` | `false` | 当前语料没有证明 square-scale 危险半类的实零偏置不可能吃掉主项。 | SiegelExceptionalBiasExclusionAtSquareScale |
| `NonrealZeroPacketPhaseBranchClosed` | `false` | `false` | 当前语料没有证明非实零点包在每个 residue 上必有足够相位抵消。 | NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2 |
| `TrivialFiniteTermBookkeepingIsolated` | `true` | `true` | 低阶项已从主硬点分离；它依赖前两块给出正余量后再由显式常数账本吸收。 | TrivialAndFiniteExplicitFormulaTermsBelowMainMarginAtP2 |
| `ClassicalAverageOrGRHShapeInputsSufficient` | `false` | `false` | BV、完整 CRT 平均、能量容量和 GRH 形状误差均不足以推出 x=P^2 的逐类正性。 | SiegelExceptionalBiasExclusionAtSquareScale AND NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2 |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步没有完成行/列命题无条件闭合；只把解析 AP 分支的剩余接口精确化。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR (SiegelExceptionalBiasExclusionAtSquareScale AND NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件不证明 Linnik=2、无 Siegel 零点、GRH 或行/列命题；它只把最新 AP 零包硬点拆成可复核的两个主分支，并关闭平均/容量/完整 CRT 直接替代点态正性的误用。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json` | `8634e16e1bcf7cd0d4ef6342b61bc73055246991c64d1940efb981f4c88c0390` |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json` | `9923c5fda90f30ef0bd67ada6e63fe8eaf0feaa88e07b6f557792bec22a1befe` |
| `docs/monograph/claim-status-table.md` | `371d885a0cc892988851d99342e474a511499c86f7dfdcc229aee3598dda7f4a` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `5d47b56e881c44d6717aaf3ed5ce002e7aa37e594581745e4dcc633d6736167a` |
