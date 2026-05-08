# Prime Matrix 线性下界筛尾段余量路由器

**状态：** `linear_lower_sieve_tail_compressed_to_ten_percent_main_margin_open`

本步把 P>=100000 的 lower-sieve 尾段继续压窄。在 alpha=0.43、s=1/alpha=2.325581 下，一维线性筛模型主项在 P=100000 约为 4896.256004，其 10% 为 489.625600>401。因此剩余不再是一般 lower-sieve，而是证明实际尾段筛余至少达到模型主项 10% 的显式常数账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
tail_linear_sieve_input_compressed=true
ten_percent_main_margin_algebra_closed=true
ten_percent_main_margin_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 压缩律

```text
LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger
  =>
LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger
```

## 2. 常数账本

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| s=1/alpha | 2.325581 |
| linear sieve f(s) | 0.431718 |
| model main at P=100000 | 4896.256004 |
| 10% model main | 489.625600 |
| target S | 401 |
| target/main | 0.081899 |
| 10% margin | 88.625600 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LinearLowerSieveTailGateActive | `true` | `false` | 最新最窄点是 P>=100000 的动态粗骨架尾段 lower-sieve 账本。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内整理模型余量，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| TenPercentMainSufficesAlgebra | `true` | `true` | 在 P=100000 处，线性筛模型主项的 10% 已超过目标 401；尾段随 P/logP 增长。 | LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger |
| TailInputCompressedToTenPercentMainMargin | `true` | `false` | 尾段输入已从泛泛 lower-sieve 压成具体的 10% 主项显式余量包。 | LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger |
| LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger | `false` | `false` | 需要证明实际筛余计数至少达到标准线性筛模型主项的 10%，并显式支付 Mertens 乘积、端点和取整误差。 | LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

直接攻 `LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger`：给出一个显式 lower-bound sieve 常数包，证明动态同余骨架在 `P>=100000` 时至少保留标准模型主项的 10%。这只需远弱于完整最优线性筛常数的版本。
