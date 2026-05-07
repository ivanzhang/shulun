# Triad-A1 DI/BFI 非 AP-source 原始 dispersion 路由器

**状态：** `nonap_source_dispersion_reduced_to_quantified_no_projection_certificate_open`

非 AP-source 分支已接回既有原始 dispersion 链条。定理位置、窗口接口与共同变量表都已路由；当前真正剩余是 `NoProjectionUncenteredDispersionIdentity` 与 `QuantifiedDIBFIWindowSubstitution` 的合取证书。

## 1. 结构律

The non-AP-source branch is not a new undefined gap. It reconnects to the already materialized original-dispersion chain: generic WFD contract, pinned DI/BFI theorem locations, current-window match, common variable table, and the transfer/scale certificate. All earlier stages are routed; the remaining fallback terminal is exactly the quantified no-projection window certificate for the non-AP source.

```text
previous terminal:
  DIBFIOriginalDispersionTheoremLocationAndHypothesisMatchForNonAPSource;

new terminal:
  DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource;

open terminal targets:
  ['NoProjectionUncenteredDispersionIdentity', 'QuantifiedDIBFIWindowSubstitution'].
```

## 2. 汇总

- `nonap_dispersion_closed=false`。
- `open_transfer_gates=['APErrorRepresentation', 'DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']`。
- `open_scale_gates=['BFILevelQuantified', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']`。
- `open_terminal_targets=['NoProjectionUncenteredDispersionIdentity', 'QuantifiedDIBFIWindowSubstitution']`。
- `terminal_gap_after_router=DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource`。

## 3. 接线表

| stage | closed | evidence | next |
| --- | --- | --- | --- |
| `NonAPSourceDetected` | `true` | open_branches=['NonAPSourceGenericWFD'] | `GenericWFDOriginalDispersionContract` |
| `GenericWFDOriginalDispersionContract` | `true` | DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch | `TheoremLocationPinned` |
| `TheoremLocationPinned` | `true` | DIBFIOriginalDispersionCurrentWindowHypothesisMatch | `CurrentWindowMatch` |
| `CurrentWindowMatch` | `true` | open_gates=['OriginalAPToWFDTargetTransfer', 'WindowScaleInequalities'] | `CommonVariableTable` |
| `CommonVariableTable` | `true` | DIBFICommonVariableTransferScaleCertificate | `TransferScaleCertificate` |
| `TransferScaleCertificate` | `false` | open_transfer=['APErrorRepresentation', 'DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']; open_scale=['BFILevelQuantified', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution'] | `DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource` |

## 4. 当前结论

非 AP-source fallback 的最窄终端为：

```text
DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource
  = NoProjectionUncenteredDispersionIdentity
    + QuantifiedDIBFIWindowSubstitution.
```

这说明下一步不应再找定理号或重复 AP-source 账本，而应直接攻未中心化无投影恒等式和量化窗口代入。
