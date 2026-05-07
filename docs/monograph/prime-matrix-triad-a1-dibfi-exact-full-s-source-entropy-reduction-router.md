# Triad-A1 DI/BFI exact full-S source entropy reduction 路由器

**状态：** `exact_full_s_source_entropy_reduced_to_factor_support_package_open`

`ExactFullSNonAPWFDSourceEntropy` 已压成 `FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov`：需要同时证明精确 u/v 因子支撑、balanced range 阈值和 Type/Fourier 容量兼容。

## 1. 结构律

Exact full-S source entropy is no longer a spectral problem at this level. With divisor-bounded factors, it follows from broad support of the exact u and v factors plus range and capacity compatibility. The full-S non-AP branch cannot silently borrow canonical support, so the next honest atom is a support package for this exact source or a matched external DI/BFI/Kuznetsov dispersion theorem.

```text
previous terminal:
  ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov;

new terminal:
  FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov;

expansion:
  ['FullSNonAPExactFactorSupportLowerBound', 'FullSNonAPBalancedRangeThreshold', 'FullSNonAPTypeFourierCapacityCompatibility', 'ExternalDIBFIKuznetsovDispersionTheoremMatch'].
```

## 2. 支撑包条款

- `sum_u |alpha_u| >= U/log^C on every surviving full-S non-AP balanced block`。
- `sum_v |delta_v| >= V/log^C on every surviving full-S non-AP balanced block`。
- `U,V >= log^B or small ranges return to PDEC/SAE/external route`。
- `Type/Fourier capacity does not concentrate on one moving factor pair`。

## 3. 被排除的捷径

- `canonical RIW/Buchstab support imported into generic full-S WFD`。
- `K4 residue flatness implies moving factor support without incidence`。
- `K6 dyadic bookkeeping implies internal block support`。

## 4. 汇总

- `exact_full_s_source_entropy_reduction_closed=false`。
- `closed_reduction_gates=['PriorExactFullSSourceEntropyPinned', 'FullSNonAPObjectBoundaryPinned', 'SupportLowerBoundImpliesEntropyImported', 'DivisorBoundedFactorBudgetAvailable', 'ExactFactorSupportLowerBoundStillOpen', 'BalancedRangeThresholdStillOpen', 'TypeFourierCapacityCompatibilityStillOpen', 'K4K6ProjectionMismatchStillBlocks', 'NoCanonicalBranchImport', 'ReductionToExactFactorSupportPackage']`。
- `open_reduction_gates=['FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov']`。
- `terminal_gap_after_router=FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov`。

## 5. 路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorExactFullSSourceEntropyPinned` | `true` | previous terminal=ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov; open=['ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov']. | none at previous-frontier level | `ExactFullSFactorSupportPackage` |
| `FullSNonAPObjectBoundaryPinned` | `true` | The full-S non-AP WFD object remains uncentered, no-projection, and cannot use AP-source lift or Maynard-W4 compression. | the factor-support package must apply to this exact object | `ExactFullSFactorSupportPackage` |
| `SupportLowerBoundImpliesEntropyImported` | `true` | Existing ExactWFDSourceEntropy ledger proves the elementary max-pair-share bound: broad factor support plus divisor bounds implies moving-block entropy. | support hypotheses are not yet proved for full-S non-AP coefficients | `ExactFullSFactorSupportPackage` |
| `DivisorBoundedFactorBudgetAvailable` | `true` | Divisor-bounded alpha_u and delta_v cost only a fixed log power. | none at divisor-bound level | `ExactFullSFactorSupportPackage` |
| `ExactFactorSupportLowerBoundStillOpen` | `true` | The source-entropy ledger records no exact factor support theorem for the surviving balanced full-S blocks. | prove lower absolute support in u and v for exact full-S non-AP factors | `FullSNonAPExactFactorSupportLowerBound` |
| `BalancedRangeThresholdStillOpen` | `true` | Balanced U,V ranges are plausible but exact log-power lower thresholds and small-range returns are not recorded for this branch. | record U,V >= log^B or route small ranges to PDEC/SAE/external | `FullSNonAPBalancedRangeThreshold` |
| `TypeFourierCapacityCompatibilityStillOpen` | `true` | Type-I/II splitting and h/Fourier smoothing must not hide a single factor pair behind an unrecorded capacity multiplier. | prove capacity compatibility or include it in exact factor support | `FullSNonAPTypeFourierCapacityCompatibility` |
| `K4K6ProjectionMismatchStillBlocks` | `true` | ExactFactorSupport ledger shows K4 residue flatness and K6 dyadic bookkeeping do not imply moving factor-pair support. | need factor-residue incidence, direct exact support, or external theorem | `FullSNonAPFactorResidueIncidenceOrDirectSupport` |
| `NoCanonicalBranchImport` | `true` | The branch-alignment router explicitly blocks silent import of canonical RIW/Buchstab support into generic full-S non-AP WFD. | direct support must be proved for this exact full-S source | `FullSNonAPExactFactorSupportPackageOrExternal` |
| `ReductionToExactFactorSupportPackage` | `true` | Exact source entropy has been reduced to its necessary support package: factor support, range threshold, and Type/Fourier capacity compatibility. | none at reduction level | `FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov` |
| `FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov` | `false` | The repository still lacks this full-S non-AP exact support package and still lacks a fully matched external dispersion theorem. | prove exact support package or cite/match external DI/BFI/Kuznetsov dispersion | `FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov` |

## 6. 当前结论

唯一剩余继续变窄为：

```text
FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov:
  prove exact u/v factor support, balanced range threshold,
  and Type/Fourier capacity compatibility for the full-S non-AP
  WFD source; or precisely match an external dispersion theorem.
```

这一步没有证明支撑包；它把 source entropy 的证明义务降成更初等、可逐项审计的 exact support/capacity 包。
