# Prime Matrix 终端行到平方相位 Jacobsthal 桥

**状态：** `terminal_row_localization_routed_to_square_phase_special_jacobsthal_or_pdec_open`

终端行 reduced atom 存在性已经无损并入平方锚 `P^2±r` 特殊相位问题。末行缺失等价于 minus 窗口 `P^2-(1..P-1)` 被 `q<P` 全覆盖；下一行缺失等价于 plus 窗口 `P^2+(1..P-1)` 被 `q<P` 全覆盖。任何一侧全覆盖都会使 `P^2` 在 `M_<P` 周期中启动长度 `P-1` 的低筛覆盖块。普通全周期 Jacobsthal 短块上界已被既有数据否定，所以最新可攻点不是全周期最大块，而是 `P^2` 特殊相位避让长块，或把该相位命中登记并排斥为 PDEC/SAE/ColumnCRT。

```text
previous_target=TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer
next_direct_attack_target=SquarePhaseSpecialPhaseLongBlockPDECExclusion
alternative_attack_target=TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound
ap_zero_packet_fallback=PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier
special_phase_period_bound_failure_count=4
row_column_unconditional_closed=false
```

## 1. 等价公式

对 `1<=r<P`：

```text
plus survivor  <=> gcd(P^2+r, M_<P)=1
minus survivor <=> gcd(P^2-r, M_<P)=1
plus full cover  <=> r=-P^2 mod q 的禁类覆盖 r=1..P-1
minus full cover <=> r= P^2 mod q 的禁类覆盖 r=1..P-1
```

若 plus 或 minus full cover 成立，则从对应平方相位开始出现长度 `P-1` 的 primorial 覆盖块。

## 2. P=5,7 样本桥接

### P=5

```text
M_below_P=6
plus_window=[26, 29]
minus_window=[21, 24]
plus_survivors=[{'r': 4, 'n': 29, 'phase_start': 2}]
minus_survivors=[{'r': 2, 'n': 23, 'phase_start': 3}]
plus_full_cover_implies_long_block_start=2
minus_full_cover_implies_long_block_start=3
```

### P=7

```text
M_below_P=30
plus_window=[50, 55]
minus_window=[43, 48]
plus_survivors=[{'r': 4, 'n': 53, 'phase_start': 20}]
minus_survivors=[{'r': 2, 'n': 47, 'phase_start': 13}, {'r': 6, 'n': 43, 'phase_start': 13}]
plus_full_cover_implies_long_block_start=20
minus_full_cover_implies_long_block_start=13
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalReducedAtomEquivalentToSquarePhaseSurvivor` | `true` | `true` | 末行 P^2-r 与下一行 P^2+r 的 reduced atom 存在性等价于 plus/minus 平方相位幸存 r。 | none for equivalence |
| `ReducedAtomForcesPrimeBySqrtGate` | `true` | `true` | 1<=r<P 时 P^2±r 均小于下一素数平方；若避开所有 q<P，则为素数。 | none for atom-to-prime |
| `TerminalFullCoverImpliesSpecialLongBlock` | `true` | `true` | 若 plus 或 minus 终端窗口被 q<P 全覆盖，则 P^2 特殊相位启动长度 P-1 的 primorial 覆盖块。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion |
| `UniformJacobsthalBoundSuffices` | `true` | `false` | 若全周期最大覆盖块长度总小于 P-1 则可闭合，但既有 Jacobsthal 数据显示该强路线已失败。 | rejected route; use special phase instead |
| `GlobalSpecialPhaseAvoidanceProved` | `false` | `false` | 仍需证明 P^2 特殊相位不落入长覆盖块深处，或把命中登记为 PDEC/SAE/ColumnCRT。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步是接口合流，不是全局无条件闭合。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier |

## 4. 最新活动基

```text
(SquarePhaseSpecialPhaseLongBlockPDECExclusion OR TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier OR PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明特殊相位避让、PDEC/SAE/ColumnCRT 排斥、点态 AP 零点包界或行/列命题无条件闭合；它只完成接口合流。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-terminal-row-crt-atom-router.json` | `9cd30547530777703ba8019a20b7eee3bfa2c82da4bd8136178b73b64250193d` |
| `docs/monograph/prime-matrix-prime-square-pm-layered-wheel-alignment-router.json` | `7de9e5eb1bb711a844539a754b9193da519331382ac219f284dbbf241026968a` |
| `docs/monograph/prime-matrix-square-phase-jacobsthal-special-phase-router.json` | `fa548f93b15f6961478bb8ecff06afab73694bea5daaec2aeefb741e4a4d34a3` |
| `docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json` | `98232747aaf27a93f4cc68cc5bc8d29d80c5d0786bfeead635a6b42293ba6107` |
| `docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json` | `eb53bcf1653d6b09c9d09c021a8418a1883bdc8cb3eba102ba0810ea3cefdc44` |
| `docs/monograph/claim-status-table.md` | `6d2bd9b62d3a3effeaee7fb365c36bb03c13a7c393ee3555ebabf1d0b2c8e974` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `20e477a10e1f57979eab172bb661049d25cd98a2f8a1147b63b5f603448b34e6` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `a6b4064f6783edbdcb054ccb9dd85a65cd0729cc9486a6b425e012281e7a4d09` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `5558390e4129f301d6850d0be4926133cd8f92ebaf25d1e084e9e786b2b5f580` |
