# Triad-A1 DI/BFI full-S source anti-atom 路由器

**状态：** `full_s_support_capacity_reduced_to_source_antiatom_or_external_open`

`FullSNonAPExactFactorSupportAndCapacityCompatibility` 已压成 `FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov`：必须证明最终 source capacity measure 无 moving atom，或匹配外部 dispersion 定理。

## 1. 反原子合同

`For the final full-S non-AP WFD source capacity measure M_{u,v}, prove max_{u,v} M_{u,v}/sum_{u,v}M_{u,v} <= log^{-2A} for every A.`

## 2. 结构律

After range closure, exact factor support and Type/Fourier capacity compatibility are not two independent analytic estimates. Together they are exactly a source-level anti-atom condition for the final moving same-(u,v) capacity measure. Existing ledgers show this condition is not forced by formal WFD inputs, K4/K6, naive incidence, or canonical branch import.

```text
previous terminal:
  FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov;

new terminal:
  FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov;

expansion:
  ['FullSNonAPStrengthenedSourceAntiAtomContract', 'ExternalDIBFIKuznetsovDispersionTheoremMatch'].
```

## 3. 被排除的捷径

- `formal well-factorable convolution`。
- `Type-I/II algebraic decomposition`。
- `Fourier h-smoothing`。
- `K4/K6 residue/tail projections`。
- `naive factor-residue incidence`。
- `silent canonical source import`。

## 4. 汇总

- `source_antiatom_reduction_closed=false`。
- `closed_antiatom_gates=['PriorSupportCapacityTerminalPinned', 'SupportCapacityPairPinned', 'FormalWFDTypeFourierDoNotForceAntiAtom', 'K4K6DoNotForceMovingFactorSupport', 'NaiveFactorResidueIncidenceBlocked', 'CanonicalSourceImportBlocked', 'SupportCapacityReducedToSourceAntiAtom']`。
- `open_antiatom_gates=['FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov']`。
- `terminal_gap_after_router=FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov`。

## 5. 路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSupportCapacityTerminalPinned` | `true` | previous terminal=FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov; open=['FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov']. | none at previous-frontier level | `FullSNonAPSourceAntiAtomContract` |
| `SupportCapacityPairPinned` | `true` | After range closure the remaining clauses are exact u/v factor support and Type/Fourier capacity compatibility. | combine them into one source-level capacity anti-atom statement | `FullSNonAPSourceAntiAtomContract` |
| `FormalWFDTypeFourierDoNotForceAntiAtom` | `true` | SourceBlockEntropy records that well-factorable convolution, Type decomposition, and Fourier smoothing can all pass while capacity concentrates on one moving block. | anti-atom must be an additional exact source theorem | `FullSNonAPSourceAntiAtomContract` |
| `K4K6DoNotForceMovingFactorSupport` | `true` | ExactFactorSupport records residue-flat but factor-concentrated models. | cannot infer the source anti-atom from K4/K6 projection data | `FullSNonAPSourceAntiAtomContract` |
| `NaiveFactorResidueIncidenceBlocked` | `true` | FactorResidueIncidence is blocked by the internal h, ell, x, z fiber inside one (u,v) block. | no bounded-multiplicity incidence shortcut remains | `FullSNonAPSourceAntiAtomContract` |
| `CanonicalSourceImportBlocked` | `true` | Branch coverage closes only the canonical RIW/Buchstab branch; generic WFD self-contained closure remains false. | full-S non-AP generic WFD needs its own source anti-atom or an external theorem | `FullSNonAPSourceAntiAtomContract` |
| `SupportCapacityReducedToSourceAntiAtom` | `true` | Exact support plus Type/Fourier capacity compatibility is precisely a statement that the final source capacity measure has no moving same-(u,v) atom. | none at reduction level | `FullSNonAPStrengthenedSourceAntiAtomContractOrExternal` |
| `FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov` | `false` | The repository has not proved a source-level anti-atom theorem for the full-S non-AP generic WFD capacity measure, and has not fully matched an external dispersion theorem. | prove source anti-atom before dispersion, strengthen the source contract, or cite/match external dispersion | `FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov` |

## 6. 当前结论

唯一剩余继续变窄为：

```text
FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov:
  prove the final full-S non-AP WFD source capacity measure
  has no moving same-(u,v) atom, or precisely match an external
  DI/BFI/Kuznetsov dispersion theorem.
```

这一步没有证明反原子合同；它排除了把支撑/容量兼容从形式 WFD、K4/K6、朴素 incidence 或 canonical 分支中免费推出的路线。
