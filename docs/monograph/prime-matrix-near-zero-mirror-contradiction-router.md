# Prime Matrix 近邻零行与 CRT 镜像矛盾路线审计

**状态：** `direct_near_zero_mirror_contradiction_rejected_boundary_phase_route_retained`

不能直接从“P 行以内有非平凡零行”推出“下一个零行很近并与镜像对称矛盾”。镜像对称是真的，但只给周期内配对；近邻复现没有自动性。可保留的硬攻方向是：证明早期零行若存在就必须产生稳定短复现/PDEC 缺陷，或直接证明首端帽边界相位非覆盖。

```text
direct_contradiction_from_near_next_zero_and_mirror=false
row_column_unconditional_closed=false
retained_route=BoundaryPhaseNoncoverageOrStableRecurrencePDEC
```

## 1. 当前剩余

当前完全自足剩余仍为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本轮回顾不改变 new-layer/DLS/source 输入基；它只审查“近邻零行 + 镜像对称”能否成为独立闭合矛盾。

## 2. 结构律

A zero row is a CRT phase certificate, not a point in an arithmetic progression of zero rows. Full-period reflection pairs every certificate with its mirror, but it does not force a nearby second certificate. The strong global no-short-recurrence statement is false, while the boundary no-short-wrap statement is equivalent to the desired first-zero delay. Therefore the proposed contradiction can close only after an additional stability lemma: an early zero row must force a stable short recurrence or a same-formal-unit phase defect. Without that input the correct target is boundary phase noncoverage and high-prime patching delay.

## 3. 判定表

| gate | closed | verdict | meaning | consequence |
| --- | --- | --- | --- | --- |
| `FullPeriodMirrorSymmetry` | `true` | `usable_but_period_internal_only` | 完整 CRT 行周期内零行集合关于周期中心镜像对称。 | 给出镜像配对，但不限制中间还可有多少零行。 |
| `AutomaticNearNextZeroFromOneEarlyZero` | `false` | `not_proved_and_p23_warns_against_short_step` | 从一个零行自动推出下一个零行很近，需要额外稳定性。 | P=23 首零行 59 后首次复现为 2612，平移 2553；row 118=2*59 不是零行。 |
| `GlobalShortRecurrenceExclusion` | `false` | `false` | 任意两个零行都不能在 2P 内复现这一强命题为假。 | 全局 2P 短复现禁止被 P=23 反例否定；可用弱化是边界跨周期短复现禁止，但该命题在反射对称下等价于首零行大于 P，不能作为独立证明出口。 |
| `BoundaryShortWrapExclusion` | `true` | `equivalent_to_target_not_independent` | 首尾跨周期间隔由镜像等于 2r0-1。 | 边界 2P 短复现禁止等价于首零行 r0>P，不能作为独立证明出口。 |
| `MirrorRecursionToSmallerMatrix` | `false` | `blocked` | 完整周期镜像偶性不能递归推出更小素数方阵零行。 | 样本中有完整周期零行的顶层对 4 个，实际较小方阵早期零行 0 个。 |
| `AnnulusTerminalMirrorToZeroRow` | `false` | `nonzero_class_terminal_not_zero_row` | n -> q^2-n 落到早期区间时，覆盖条件变成 q^2 mod ell 非零类。 | 环带镜像行号命中 45 次，实际成为更小方阵零行 0 次。 |
| `UsableWeakRoute` | `true` | `boundary_phase_noncoverage_or_stable_recurrence_return` | 可用方向是首端帽边界非覆盖，或证明早期零行强制稳定短复现后回流 PDEC/SAE/ColumnCRT。 | 若没有稳定性，零行复现只是稀疏 CRT 相位证书集；若有稳定性，则形成命名结构缺陷。 |

## 4. 对用户路线的精确结论

用户路线中可严格保留的部分：

- 完整 CRT 周期零行集合有镜像对称。
- 若首零行行号为 `r0`，跨周期首尾镜像间隔为 `2r0-1`。
- 因而 `r0<=P` 等价于边界跨周期出现 `<=2P-1` 的短间隔。

不能直接使用的部分：

- 周期内部存在短复现的全局禁止命题是假的；P=23 有多对间隔不超过 `2P` 的零行。
- 从一个早期零行自动推出“下一个零行很近”没有已证机制；P=23 的首零行后首次复现平移为 `2553`，且 `2r0` 不是零行。
- 镜像递归不会自动给出更小素数方阵零行；剥层会复活洞，`q^2-n` 反射变成非零类终端块。

因此下一步若继续利用这条思路，最窄命题应改写为：

```text
EarlyZeroRowWithinP
  => StableShortRecurrencePDEC/SAE/ColumnCRT
     OR BoundaryPhaseNoncoverageFailure.
```

也就是说，必须额外证明早期零行会强制稳定短复现；否则应回到首端帽边界非覆盖和高素数补洞 CRT 延迟。
