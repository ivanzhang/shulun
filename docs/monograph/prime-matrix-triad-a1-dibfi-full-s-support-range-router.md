# Triad-A1 DI/BFI full-S support range 路由器

**状态：** `full_s_support_range_closed_factor_support_capacity_open`

`FullSNonAPBalancedRangeThreshold` 已在 full-S regime 下闭合；当前终端缩为 `FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov`。

## 1. 结构律

The balanced range threshold is not the true terminal hard point in the full-S regime. C≈P/log^O(P) and c=uv with U,V=C^{1/2}log^O(P) force U,V to dominate every fixed logarithmic support threshold. Thus the remaining internal support package is exact factor support plus Type/Fourier capacity compatibility.

```text
previous terminal:
  FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov;

closed clause:
  FullSNonAPBalancedRangeThreshold;

new terminal:
  FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov;

expansion:
  ['FullSNonAPExactFactorSupportLowerBound', 'FullSNonAPTypeFourierCapacityCompatibility', 'ExternalDIBFIKuznetsovDispersionTheoremMatch'].
```

## 2. 剩余支撑包条款

- `FullSNonAPExactFactorSupportLowerBound`。
- `FullSNonAPTypeFourierCapacityCompatibility`。

## 3. 汇总

- `balanced_range_threshold_closed=true`。
- `closed_range_gates=['PriorSupportPackagePinned', 'FullSScalePinned', 'CompletionRatioPolylogPinned', 'BalancedFactorizationPinned', 'PolynomialScaleBeatsAnyFixedLogThreshold', 'FiniteInitialRangeReturnLegal', 'FullSNonAPBalancedRangeThreshold']`。
- `open_range_gates=['FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov']`。
- `terminal_gap_after_router=FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov`。

## 4. 路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSupportPackagePinned` | `true` | previous terminal=FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov; open=['FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov']. | none at previous-frontier level | `FullSNonAPBalancedRangeThreshold` |
| `FullSScalePinned` | `true` | Full-S theorem input fixes X≈P^2, C≈P/log^O P and S≈P. | none at qualitative scale level | `FullSNonAPBalancedRangeThreshold` |
| `CompletionRatioPolylogPinned` | `true` | Full-S completion records L_c=S/c=log^O(P). | none; this confirms C is within a polylog factor of P | `FullSNonAPBalancedRangeThreshold` |
| `BalancedFactorizationPinned` | `true` | C-dependent residue reduction imports c=uv with U,V=C^{1/2}log^O. | none at factorization-shape level | `FullSNonAPBalancedRangeThreshold` |
| `PolynomialScaleBeatsAnyFixedLogThreshold` | `true` | For any fixed B,K, P^{1/2}/log^K(P) >= log^B(P) for all sufficiently large P. | only finite initial P below the threshold | `FullSNonAPBalancedRangeThreshold` |
| `FiniteInitialRangeReturnLegal` | `true` | Finite pre-asymptotic failures are not the analytic full-S hard point; they return to finite verification/PDEC/SAE bookkeeping. | none for asymptotic proof search | `FullSNonAPBalancedRangeThreshold` |
| `FullSNonAPBalancedRangeThreshold` | `true` | Since C≈P/log^O P and U,V=C^{1/2}log^O, every surviving balanced full-S block has U,V above any fixed log^B threshold for large P. | none; remove range threshold from the terminal package | `FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternal` |
| `FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov` | `false` | After range closure, the support package only needs exact u/v factor support and Type/Fourier capacity compatibility, unless an external theorem is matched. | prove exact support plus capacity compatibility, or cite/match external dispersion | `FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov` |

## 5. 当前结论

唯一剩余继续变窄为：

```text
FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov:
  prove exact u/v factor support and Type/Fourier capacity compatibility
  for the full-S non-AP WFD source, or precisely match an external theorem.
```

这一步只闭合 range 阈值；没有证明因子支撑或容量兼容。
