# Prime Matrix PDEC-CAP 横向源支撑路由器

**状态：** `transverse_source_support_reduced_to_embedding_layer_transfer_or_direct_ncblk`

`TransverseSourceSupportNonconcentrationCertificate` 已继续拆成严格自足边界：`TransverseFormalUnitA1SourceEmbedding` 已由有限测度函子性闭合：横向商 formal unit 确实来自已闭合来源账本的 canonical A1/KZ-E pre-Cauchy 源。新的下游剩余是 Buchstab 层准入、非零转移与薄区间回流；若不走源路线，则必须直接证明 actual transverse NC-BLK 非集中。

## 1. 归约律

A transverse source-support/nonconcentration certificate has two honest self-contained routes. The source route must first embed the transverse formal unit into the already provenance-closed canonical A1/KZ-E pre-Cauchy source; after that, the existing canonical RIW support chain reduces the problem to layer admission, nonzero coefficient transfer, and thin-interval return for Buchstab squarefree products. The direct route proves actual transverse NC-BLK non-concentration without using canonical support. No route may import a generic WFD self-contained theorem.

```text
TransverseSourceSupportNonconcentrationCertificate
  source route:
    TransverseFormalUnitA1SourceEmbedding (closed by finite-measure functoriality);
    then CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn;
  direct route:
    DirectTransverseNCBLKActualCoefficientNonConcentration.
```

## 2. 汇总

- `transverse_source_support_reduced=true`。
- `transverse_source_support_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。
- `downstream_source_route_hardpoint=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。
- `direct_fallback_hardpoint=DirectTransverseNCBLKActualCoefficientNonConcentration`。
- `open_final_gates=['CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `TransverseSourceSupportFrontierActive` | `true` | `false` | TransverseSourceSupportNonconcentrationCertificate | 上一层已经把横向 clean 原子的自足路线压成源支撑/非集中证书。 |
| `SourceLockSplitAvailable` | `true` | `false` | A1CleanBranchCanonicalSourceAdmissionOrExternalDIBFIOriginalDispersion | canonical 分支可接入内部支撑链；generic 分支必须外部化或回流 PDEC/SAE。 |
| `ActualA1SourceProvenanceClosed` | `true` | `false` | NoFurtherActualSourceProvenanceGap | 原始 A1/KZ-E pre-Cauchy 来源账本已声明 canonical RIW/Buchstab 决策树系数。 |
| `CanonicalRIWSupportReduced` | `true` | `false` | SquarefreeBuchstabLayerSupportLowerBoundOrExternalDIBFIOriginalDispersion | 一旦横向 formal unit 嵌入 canonical 源头，支撑问题降到 Buchstab 层支撑下界。 |
| `RawThickSquarefreeSupportClosed` | `true` | `false` | CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturnOrExternalDIBFIOriginalDispersion | 厚 surviving balanced interval 中 squarefree product 原始计数已闭合；剩余是 canonical 层准入与非零转移。 |
| `NCBLKBoundaryNamed` | `true` | `false` | Triad-A1 same-set capacity / full-S terminal on the canonical RIW/Buchstab source branch. | 直接 NC-BLK 路线仍可走，但必须证明实际横向系数块非集中，不能用 generic 自足版偷换。 |
| `TransverseSourceSupportReducedToEmbeddingOrDirectNCBLK` | `true` | `false` | source lock + provenance + Buchstab support chain + direct NC-BLK fallback | 横向源支撑证书已拆为 formal unit 嵌入、canonical 层转移、或直接实际 NC-BLK。 |
| `TransverseFormalUnitA1SourceEmbedding` | `true` | `false` | CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn | 横向商 formal unit 已证明为 canonical A1/KZ-E pre-Cauchy 源的限制、商或条件化，不改变来源系数。 |
| `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn` | `false` | `true` | CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn | 若嵌入 canonical 源成立，还需证明 Buchstab squarefree products 被 exact canonical 层承认、系数非零，薄区间回流 edge/PDEC/SAE。 |
| `DirectTransverseNCBLKActualCoefficientNonConcentration` | `false` | `false` | not submitted | 这是备用自足路线：若不走已嵌入的 canonical 来源链，才需要直接证明横向商实际系数在 moving block 上不能集中。 |

## 4. 下一步

下一步最窄自足硬点是 `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`：在已嵌入的 canonical 源内，证明 Buchstab squarefree products 被 exact canonical 层承认、系数非零；若 balanced interval 太薄，必须回流 edge/PDEC/SAE。
