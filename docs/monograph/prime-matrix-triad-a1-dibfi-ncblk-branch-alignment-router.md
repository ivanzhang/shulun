# Triad-A1 DI/BFI NC-BLK branch alignment 路由器

**状态：** `ncblk_branch_alignment_reduced_to_exact_full_s_source_entropy_or_external_open`

`NCBLKActualBlockNonConcentrationOrExternalDIBFI` 已被分支对齐为 `ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov`：canonical source branch 不能静默借用，形式 WFD 模板也不能推出 moving-block 熵。

## 1. 结构律

NC-BLK is a block-energy statement. SourceBlockEntropy is a valid sufficient condition, but branch coverage forbids importing the canonical RIW/Buchstab source chain into the broader full-S non-AP generic WFD object. Therefore the honest next target is exact moving-block source entropy for this full-S non-AP coefficient generation, or a matched external DI/BFI/Kuznetsov theorem.

```text
previous terminal:
  NCBLKActualBlockNonConcentrationOrExternalDIBFI;

new terminal:
  ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov;

expansion:
  ['ExactFullSNonAPWFDSourceEntropy', 'ExternalDIBFIKuznetsovDispersionTheoremMatch'].
```

## 2. 被排除的捷径

- `silent canonical RIW/Buchstab source import`。
- `APSourceLift`。
- `formal WFD template implies moving-block entropy`。

## 3. 汇总

- `ncblk_branch_alignment_closed=false`。
- `closed_alignment_gates=['PriorNCBLKTerminalPinned', 'FullSNonAPGenericObjectPinned', 'APSourceLiftStillRejected', 'NoSilentCanonicalSourceImport', 'SourceEntropyImpliesNCBLK', 'FormalWFDInputsDoNotForceSourceEntropy', 'AlignmentToExactSourceEntropyOrExternal']`。
- `open_alignment_gates=['ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov']`。
- `terminal_gap_after_router=ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov`。

## 4. 分支对齐账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorNCBLKTerminalPinned` | `true` | previous terminal=NCBLKActualBlockNonConcentrationOrExternalDIBFI; open=['NCBLKActualBlockNonConcentrationOrExternalDIBFI']. | none at previous-frontier level | `FullSNonAPGenericObjectAdmission` |
| `FullSNonAPGenericObjectPinned` | `true` | NewFullSTheoremInput is pinned as the current full-S, non-AP, uncentered, no-projection WFD window. | cannot replace this by AP-source or a centered object | `NoSilentCanonicalSourceImport` |
| `APSourceLiftStillRejected` | `true` | APSourceLift is already rejected; the full-S non-AP object cannot be reclassified as AP-source. | none; this blocks the AP-source shortcut | `NoSilentCanonicalSourceImport` |
| `NoSilentCanonicalSourceImport` | `true` | Branch coverage closes the canonical RIW/Buchstab source branch, but explicitly leaves generic WFD self-contained closure false. | full-S non-AP generic WFD must prove its own source entropy or use external DI/BFI | `ExactFullSNonAPWFDSourceEntropy` |
| `SourceEntropyImpliesNCBLK` | `true` | SourceBlockEntropy gives max_b M_b/M <= log^{-2A}, hence sum_b \|S_b\|^2 <= log^{-2A} M^2 and implies NC-BLK. | source entropy itself is not proved for the exact full-S non-AP source | `ExactFullSNonAPWFDSourceEntropy` |
| `FormalWFDInputsDoNotForceSourceEntropy` | `true` | The source entropy router records moving-delta well-factorable models that pass formal templates while concentrating on one moving block. | must use exact coefficient generation, not the formal WFD template alone | `ExactFullSNonAPWFDSourceEntropy` |
| `AlignmentToExactSourceEntropyOrExternal` | `true` | The full-S non-AP NC-BLK terminal is aligned with the same valid sufficient condition as the KZ-E NC-BLK route, but without silent canonical-source import. | none at branch-alignment level | `ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov` |
| `ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov` | `false` | The repository has not proved scale-uniform moving-block entropy for the exact full-S non-AP WFD coefficients, and has not completed a primary-source theorem match for this exact object. | prove exact source entropy for the full-S non-AP coefficients, or cite/match external dispersion | `ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov` |

## 5. 当前结论

唯一剩余继续变窄为：

```text
ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov:
  prove scale-uniform moving-block source entropy for the exact
  full-S non-AP WFD coefficient generation, or precisely match
  an external DI/BFI/Kuznetsov dispersion theorem.
```

这一步没有证明 exact source entropy；它只关闭了“把 full-S generic WFD 静默并入 canonical source branch”的错误路线。
