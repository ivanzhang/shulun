# Prime Matrix PDEC-CAP 横向 clean 原子前沿路由器

**状态：** `transverse_clean_atom_routed_to_source_support_or_external_dibfi_frontier`

`TransverseQuotientCleanLargeSieveAtom` 已被拆成可审查前沿：它接入 A1 CleanKLS/SC-9，不再是无名大筛黑箱。自足路线不能直接调用 canonical 吸收，因为横向商系数的 canonical RIW/Buchstab 源支撑或实际 NC-BLK 非集中尚未证明；朴素 factor-residue incidence 桥已被内部 fiber 反例阻断。外部 DI/BFI 路线则压到 `DIBFIQuantifiedNoProjectionWindowCertificate`。

## 1. 前沿律

The transverse quotient clean large-sieve atom is not a fourth terminal. Once transverse sparse support, persistent transverse bias, and shell/column concentration have been removed, the residual satisfies the same K1--K9 clean admission grammar as the A1 CleanKLS branch. Hence it routes to the SC-9 frontier: self-contained actual-coefficient NC-BLK or external DI/BFI. The canonical NC-BLK branch is already absorbed only when canonical RIW/Buchstab source support is proved. K4/K6 flatness alone does not imply that support, and the naive factor-residue incidence bridge is blocked by the internal fiber obstruction. Therefore the self-contained next certificate is a transverse source-support/nonconcentration certificate. The external original DI/BFI route remains the quantified no-projection window certificate.

```text
TransverseQuotientCleanLargeSieveAtom
  => A1 K1--K9 clean admission;
admission failure
  => PDEC / SAE / ColumnCRT / Multiplicity;
admission success
  => SC-9 frontier;
SC-9
  => actual-coefficient NC-BLK or external DI/BFI;
self-contained route
  => TransverseSourceSupportNonconcentrationCertificate;
external original DI/BFI route
  => DIBFIQuantifiedNoProjectionWindowCertificate.
```

## 2. 汇总

- `transverse_clean_atom_routed_to_named_frontier=true`。
- `transverse_quotient_clean_large_sieve_closed=false`。
- `external_windowed_kls_version_closed_if_accepted=true`。
- `row_column_unconditional_closed=false`。
- `narrowest_self_contained_hardpoint=TransverseSourceSupportNonconcentrationCertificate`。
- `narrowest_external_hardpoint=DIBFIQuantifiedNoProjectionWindowCertificate`。
- `narrowest_next_hardpoint=TransverseSourceSupportNonconcentrationCertificate_OR_DIBFIQuantifiedNoProjectionWindowCertificate`。
- `open_final_gates=['TransverseSourceSupportNonconcentrationCertificate', 'DIBFIQuantifiedNoProjectionWindowCertificate']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `TransverseCleanAtomActive` | `true` | `false` | TransverseQuotientCleanLargeSieveAtom | 上一层已把横向纤维扩张压成横向商 L2-flat clean residual。 |
| `A1CleanKLSAdmissionAvailable` | `true` | `false` | KuznetsovLSAtomSC9OrExternalCitation | K1--K9 clean admission 已登记：失败回流 PDEC/SAE/Multiplicity/Promotion，通过才进入 KLS/SC-9。 |
| `TransverseAtomSpecializesA1CleanUnit` | `true` | `false` | transverse quotient L2-flat residual -> Kloosterman/dispersion formal unit | 横向商 clean 原子不是第四出口；它是 A1 clean KLS/SC-9 formal unit 的横向特化。 |
| `SC9FrontierNamed` | `true` | `false` | NCBLKOrExternalDIBFIOriginalDispersion | SC-9 已展开成实际系数 NC-BLK 或外部 DI/BFI 原始 dispersion。 |
| `CanonicalBoundaryAvailableButNotGenericUpgrade` | `true` | `false` | Triad-A1 same-set capacity / full-S terminal on the canonical RIW/Buchstab source branch. | canonical NC-BLK 可由已闭合边界吸收；generic WFD 不能偷渡为自足证明。 |
| `ExactFactorSupportNotAutomatic` | `true` | `false` | FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion | K4/K6 clean 平坦性不能自动推出因子支撑下界；还需源支撑/非集中证书。 |
| `NaiveFactorResidueIncidenceBlocked` | `true` | `false` | CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion | 单个 moving factor-pair 内有增长的内部 fiber，朴素 incidence 桥不能闭合自足版。 |
| `TransverseCleanAtomRoutedToNamedFrontier` | `true` | `false` | A1 CleanKLS/SC-9 + NC-BLK boundary + source-support obstruction | 横向 clean 大筛原子已接入既有前沿；剩余不再是宽泛 LargeSieve 标签。 |
| `TransverseSourceSupportNonconcentrationCertificate` | `false` | `true` | canonical RIW/Buchstab support lower bound or actual transverse NC-BLK not submitted | 完全自足路线还需证明横向商系数具有 canonical 源支撑下界，或直接证明实际块非集中。 |
| `DIBFIQuantifiedNoProjectionWindowCertificate` | `false` | `true` | DIBFIQuantifiedNoProjectionWindowCertificate | 外部原始 DI/BFI 路线还需无投影对象恒等式与量化尺度代入；直接接受窗口化 KLS 外部定理则属于外部输入版。 |

## 4. 下一步

自足路线直接攻 `TransverseSourceSupportNonconcentrationCertificate`：证明横向商系数继承 canonical RIW/Buchstab 源支撑下界，或直接证明实际 transverse NC-BLK 块非集中。外部路线则只能在明确接受窗口化 KLS 定理，或闭合 `DIBFIQuantifiedNoProjectionWindowCertificate` 后使用。
