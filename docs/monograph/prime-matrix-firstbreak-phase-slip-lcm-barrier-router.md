# Prime Matrix 首破裂 phase-slip LCM-支撑宽度屏障证书

**状态：** `firstbreak_phase_slip_lcm_width_barrier_closed_terminal_exclusion_open`

首破裂 phase-slip 的固定 carrier 复现已经被压成 LCM-支撑宽度屏障：若释放相位在首破裂行 y 之后以同一 carrier 标签集复现，则复现步长 d 必须被所有活动 carrier 的 lcm 整除；但到平方锚前的支撑宽度只有 H=P-y。因此 L>H 时没有非零复现，L<=H 时只剩小 LCM/ColumnCRT/PDEC 分支；逃避固定标签的情形必须登记为 moving-carrier PDEC/SAE。

```text
fixed_carrier_lcm_replay_period_closed=true
square_support_width_sharpened_to_p_minus_y=true
lcm_exceeds_width_no_fixed_replay=true
firstbreak_phase_slip_named_return_exclusion_proved=false
row_column_unconditional_closed=false
```

## 1. 屏障定理

设首破裂发生在行 `y<=P`，上一行 `y-1` 仍是零行。取释放 formal unit 的活动 carrier 标签集
`Lambda={q_1,...,q_s}`。若同一释放相位模式在 `y+d` 复现，并且 carrier 标签不移动，则每个活动标签都要求

```text
rho_q(y+d)=rho_q(y),
rho_q(t)=-tP mod q.
```

因此

```text
dP == 0 mod q.
```

由于 `q<P` 且 `q` 为素数，`(P,q)=1`，所以 `q|d`。于是

```text
lcm(Lambda) | d.
```

从首破裂行到平方锚前的可复现宽度只有

```text
H=P-y.
```

若 `lcm(Lambda)>H`，则 `1<=d<=H` 内没有非零固定标签复现。若 `lcm(Lambda)<=H`，则活动 carrier 的合成模数已被 `H<=P` 控制，只能进入小 LCM/固定 residue 的 ColumnCRT/PDEC 分支。

## 2. 三分出口

首破裂 phase-slip 终端由此分成三类：

```text
FirstBreakPhaseSlipNamedReturnExclusion
  -> SmallLCMColumnCRTPDECExclusion
  AND NonreplaySparseFirstBreakSAESummability
  AND MovingCarrierPhaseSlipPDECExclusion
```

- 小 LCM 分支：固定 carrier 标签可在剩余宽度内复现，必须作为小合成模数 ColumnCRT/PDEC 排斥。
- 无复现分支：`lcm>H`，不能形成稳定短周期支付链；若只孤立出现，进入 sparse SAE/LocalSurvivor 可求和问题。
- moving-carrier 分支：若通过更换 carrier 标签逃避 LCM 屏障，则不再是固定同标签复现，而是 moving family PDEC/SAE。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FirstBreakPhaseSlipImported | `true` | `false` | 上一层把 early-to-square 抽象转移压到 square-zero 或首破裂 phase-slip 命名终端。 | FirstBreakPhaseSlipNamedReturnExclusion |
| CarrierPhaseMotionFormulaClosed | `true` | `true` | 首破裂 carrier q 的相位满足 rho_q(t+d)=rho_q(t)-dP mod q；因 (P,q)=1，同标签复现要求 q\|d。 | none for formula |
| FixedCarrierLCMReplayPeriodClosed | `true` | `true` | 对固定 carrier 标签集 Lambda，精确同标签复现步长 d 必须被 L=lcm(Lambda) 整除。 | FirstBreakFixedCarrierLCMWidthBarrier |
| SquareSupportWidthSharpened | `true` | `true` | 首破裂发生在 y 后，直到平方锚前只剩 H=P-y 个可复现步长；这比旧 short< P 自同构门更窄。 | support width H=P-y |
| LCMExceedsWidthNoReplay | `true` | `true` | 若 L>H，则 1<=d<=H 内不存在固定 carrier 同标签复现；该 first-break 不能成为稳定短周期支付链。 | NonreplaySparseFirstBreakSAESummability OR MovingCarrierPhaseSlipPDECExclusion |
| SmallLCMBranchIsStructured | `true` | `false` | 若 L<=H，则所有互异 carrier 的乘积已被 H<=P 控制；多标签复现只能落在小 LCM/固定列位移/ColumnCRT/PDEC 分支。 | SmallLCMColumnCRTPDECExclusion |
| RepeatedCarrierResidueRouted | `true` | `true` | 同一 q 或同一 residue 的重复使用不增加 L，但它正是 fixed-residue/ColumnCRT/PDEC 账本对象。 | SmallLCMColumnCRTPDECExclusion |
| MovingCarrierIsNamedReturn | `true` | `true` | 若反例链通过更换 carrier 标签逃避 LCM 屏障，则它不是 fixed replay，而是 moving-carrier phase slip，进入 PDEC/SAE 命名回流。 | MovingCarrierPhaseSlipPDECExclusion |
| FirstBreakBarrierReduced | `true` | `false` | 首破裂终端已被分成小 LCM 固定复现、无复现稀疏 SAE、moving-carrier PDEC 三项；不再保留抽象 phase-slip 终端。 | SmallLCMColumnCRTPDECExclusion AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion |
| FirstBreakNamedReturnExclusionProved | `false` | `false` | 本步只关闭固定 carrier 复现的合成模数屏障；尚未排斥小 LCM PDEC、非复现 SAE 或 moving-carrier PDEC。 | SmallLCMColumnCRTPDECExclusion AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、上述三项终端排斥，或并行 signed-row/source-rank 前沿闭合。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND SmallLCMColumnCRTPDECExclusion AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 4. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND SmallLCMColumnCRTPDECExclusion AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND SmallLCMColumnCRTPDECExclusion AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书不证明首破裂不存在。
- 本证书只排除了固定 carrier 同标签复现在 `lcm>H` 时的可能性。
- 小 LCM PDEC、非复现 sparse SAE、moving-carrier PDEC 仍需继续排斥。
- 行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_phase_slip_lcm_barrier_router.py` | `ff61a1b66d3d7bb89976a4404a8b7a98934c63b90cd6c98c2ca1306d8b526bf1` |
| `docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json` | `54575ef141b22648dd85608f8db9144e24ef013b69df9a130147857c28840c2f` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
| `docs/monograph/prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json` | `700c2f6abf741e25d448151b2231720ae03c2e0de3caab67d2bdedfd443d7d25` |
| `docs/monograph/prime-matrix-early-zero-terminal-package-reduction-router.json` | `d53ae12d44d1a8d376d29589a9df6eb26aa48a35ad18f88c0372eba62ad03395` |
| `docs/monograph/prime-matrix-early-zero-terminal-schema-reconciliation-router.json` | `a998f03b4bbb260f47b9b9978b1ff22995ff800329fc75f6faa48bb10a4d14e8` |
| `docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json` | `3b4788e5d5ca0887a903422eff12882a5e41c2040c760df61cdda575cf4109e4` |
