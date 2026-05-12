# Prime Matrix strict Dusart Table 6.3 机器可读表行审计证书

**状态：** `table63_b28_external_row_machine_readable_full_generation_open`

Table 6.3 的 b=28 行已被压成最小机器可读外部表行：`epsilon_psi(28)=0.00002224`，适用高尾 `x>=exp(28)`。若接受 Dusart 外部表语义，它与已闭合的高尾拼接算术严格匹配，因为 `0.00002224 < 1/36260`。但作者侧自足版尚未闭合：仍需证明该值如何由同一显式公式、有限零点/零点自由尾项、区间传播、外向舍入和可复现 hash 生成。

```text
machine_readable_table63_b28_row_closed=true
machine_readable_table63_external_row_usable=true
machine_readable_table63_closed=false
table63_generation_rounding_closed=false
psi_epsilon_table_algorithm_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 机器表行

| table | b | function | epsilon | interval | needed by |
| --- | ---: | --- | ---: | --- | --- |
| Dusart Table 6.3 | `28` | `psi` | `0.00002224` | x >= exp(28) | `PsiEpsilonHighTailB28TableCertificate` |

## 2. 高尾拼接算术

| field | value |
| --- | ---: |
| `epsilon_psi_28` | `0.00002224` |
| `target_1_over_36260` | `0.000027578599007170435741864313292884721456150027578599` |
| `p51_high_tail_margin` | `0.000005338599007170435741864313292884721456150027578599` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只登记反例链可调用的外部 Table 6.3 高尾输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `Table63GateActiveAfterMiddleSync` | `true` | `true` | 中段 psi 上界已由 delta-aware 归档关闭后，下一表算法门确认为 Table 6.3。 | MachineReadableDusartTable63EpsilonPsiLedger |
| `EpsilonPsi28Table63SourceLedger` | `true` | `false` | 已有证书把 Dusart Table 6.3 的 b=28 行定位为 epsilon_psi(28)=2.224E-5。 | MachineReadableDusartTable63EpsilonPsiLedger |
| `DusartTableEpsilonStatementExtractionImported` | `true` | `true` | epsilon 表审计已把 eps_psi_28=0.00002224 抽成机器可读责任项。 | MachineReadableDusartTable63B28EpsilonPsiRowLedger |
| `MachineReadableDusartTable63B28EpsilonPsiRowLedger` | `true` | `false` | 本步形成最小机器可读外部表行：b=28, epsilon_psi=0.00002224, asserted interval x>=exp(28)。 | Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger |
| `HighTailP51ArithmeticMargin` | `true` | `true` | 若接受该表行的上界语义，则高尾拼接满足 0.00002224 < 1/36260。 | margin=0.000005338599007170435741864313292884721456150027578599 |
| `MachineReadableTable63ExternalRowUsable` | `true` | `false` | 外部路线可严格使用 b=28 表行关闭高尾数值输入；这仍不是作者侧自足生成证明。 | external Table 6.3 accepted |
| `Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger` | `false` | `false` | 还缺从显式公式、有限零点验证、零点自由尾项与外向舍入规则生成 2.224E-5 的证明。 | VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `MachineReadableDusartTable63EpsilonPsiLedger` | `false` | `false` | 完整 MachineReadableDusartTable63 不能只靠单行摘录闭合；还需要生成规则、舍入方向、适用区间与可复现 hash。 | Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger AND VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `PsiEpsilonTableAlgorithmStillOpen` | `false` | `false` | 中段归档和 b=28 外部表行仍未关闭 Table 6.4、零点输入绑定、区间传播与表 hash。 | ThetaLessThanIdentityTable64To8e11SourceLedger AND VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | Table 6.3 表行机器化不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger
```

