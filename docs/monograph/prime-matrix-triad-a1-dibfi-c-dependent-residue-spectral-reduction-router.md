# Triad-A1 DI/BFI c-dependent residue spectral reduction 路由器

**状态：** `c_dependent_residue_spectral_input_reduced_to_kfls_ncblk_or_external_open`

`CDependentResidueWeightSpectralCancellationInput` 已经接入已有 `BWFD -> BSC -> KFLS` 内核链：`B_{c,x}` 与 `\widehat\beta_c(\ell)` 由有限 Fourier 反演精确等价。自足版剩余不是新的普通大筛估计，而是 `NCBLKActualBlockNonConcentrationOrExternalDIBFI`。

## 1. 精确桥接恒等式

- `B_{c,x}=sum_{s≡x(c)} beta_s W(s/S)`。
- `hat_beta_c(ell)=sum_x B_{c,x} e_c(-ell*x)`。
- `sum_x^* B_{c,x} e_c(a_h*x+b_h*bar(x)) = (1/c) sum_ell hat_beta_c(ell) S(a_h+ell,b_h;c)`。

## 2. 结构律

The c-dependent residue object is not a new unrelated obstacle. It is the residue-space Fourier dual of the BWFD finite completion. After c=uv, the same object becomes the BSC/KFLS reciprocal-fraction phase. The remaining self-contained obstruction is therefore not another completion estimate, but actual same-(u,v) block non-concentration for the full-S non-AP WFD coefficients, unless a precisely matched external DI/BFI/Kuznetsov dispersion theorem is used.

```text
previous terminal:
  CDependentResidueWeightSpectralCancellationInput;

new terminal:
  NCBLKActualBlockNonConcentrationOrExternalDIBFI;

expansion:
  ['KFLSCoreInput', 'NCBLKActualBlockNonConcentration', 'ExternalDIBFIOrKuznetsovDispersionTheoremMatch'].
```

## 3. 被排除的捷径

- `flat residue mass`。
- `pointwise Weil plus L2`。
- `ordinary large sieve`。
- `APSourceLift`。
- `SOURCE-CEN`。
- `BD-CEN`。
- `raw BLK-energy-core as an arbitrary coefficient-array theorem`。

## 4. 汇总

- `c_dependent_residue_spectral_reduction_closed=false`。
- `closed_reduction_gates=['PriorCDependentResidueInputPinned', 'ResidueFourierCompletionEquivalence', 'BalancedWellFactorableBSCReduction', 'BSCToKFLSPhaseExpansion', 'KFLSToSquareKernelAudit', 'BlockCenteringNoGoImported', 'SourceCENAndRawBLKEnergyShortcutsBlocked', 'ReductionChainToNCBLKOrExternal']`。
- `open_reduction_gates=['NCBLKActualBlockNonConcentrationOrExternalDIBFI']`。
- `terminal_gap_after_router=NCBLKActualBlockNonConcentrationOrExternalDIBFI`。

## 5. 路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorCDependentResidueInputPinned` | `true` | previous terminal=CDependentResidueWeightSpectralCancellationInput; open=['CDependentResidueWeightSpectralCancellationInput']. | none at previous-frontier level | `ResidueFourierCompletionEquivalence` |
| `ResidueFourierCompletionEquivalence` | `true` | B_{c,x}=sum_{s≡x(c)} beta_s W(s/S), hat_beta_c(ell)=sum_x B_{c,x} e_c(-ell*x); hence the B_{c,x} Kloosterman residue sum is exactly the finite-Fourier completed sum (1/c) sum_ell hat_beta_c(ell) S(a_h+ell,b_h;c). | none; this is a finite Fourier identity, not an estimate | `BalancedBSCCompletionCore` |
| `BalancedWellFactorableBSCReduction` | `true` | The HLC BWFD completion file already performs c=uv with U,V=C^{1/2}log^O(y) and rewrites the completed Kloosterman sum as BSC-core. | BSC-core still needs logarithmic saving | `BSCCore` |
| `BSCToKFLSPhaseExpansion` | `true` | Expanding the two complete Kloosterman sums exposes the rigid phase e(bar(v)R/u + bar(u)T/v), so BSC-core reduces to KFLS-core. | KFLS-core is not proved by the expansion itself | `KFLSCore` |
| `KFLSToSquareKernelAudit` | `true` | The KFLS square-kernel audit rules out positive-kernel/Schur shortcuts and reduces the self-contained route to centered four-modulus control plus block-energy duties. | block diagonal/local variance cannot be discarded for free | `BlockCenteredFourModulusOrNCBLK` |
| `BlockCenteringNoGoImported` | `true` | CFQK/BD-CEN audits show that h=0 centering is not same-(u,v) block centering; BD-CEN is false for the current unblocked object. | must use real source non-concentration or external dispersion | `NCBLKActualBlockNonConcentrationOrExternalDIBFI` |
| `SourceCENAndRawBLKEnergyShortcutsBlocked` | `true` | SOURCE-CEN changes the current WFD target, and raw BLK-energy is false as an arbitrary coefficient-array theorem. | only actual-coefficient NC-BLK or an external theorem remains | `NCBLKActualBlockNonConcentrationOrExternalDIBFI` |
| `ReductionChainToNCBLKOrExternal` | `true` | C-dependent residue weights are the Fourier-dual form of the existing BWFD/BSC completion chain; all free centering and ordinary large-sieve exits have already been ruled out. | none at reduction level | `NCBLKActualBlockNonConcentrationOrExternalDIBFI` |
| `NCBLKActualBlockNonConcentrationOrExternalDIBFI` | `false` | The repository still lacks a proof that the actual full-S non-AP WFD coefficients are same-(u,v) block-nonconcentrated with arbitrary log saving, and also lacks a fully matched primary-source external DI/BFI theorem for this exact full-S object. | prove actual-coefficient NC-BLK, or cite/match an external DI/BFI/Kuznetsov dispersion theorem | `NCBLKActualBlockNonConcentrationOrExternalDIBFI` |

## 6. 当前结论

唯一剩余继续变窄为：

```text
NCBLKActualBlockNonConcentrationOrExternalDIBFI:
  prove actual same-(u,v) block non-concentration for the full-S
  non-AP WFD coefficients, or provide a precisely matched external
  DI/BFI/Kuznetsov dispersion theorem for the same uncentered object.
```

这一步没有证明 NC-BLK，也没有把外部定理逐项匹配完成；它关闭的是 `CDependentResidueWeightSpectralCancellationInput` 到既有 KFLS/NC-BLK 核心链之间的缺口。
