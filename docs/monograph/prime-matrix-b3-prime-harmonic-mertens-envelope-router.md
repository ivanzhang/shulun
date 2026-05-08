# Prime Matrix B=3 prime-harmonic Mertens 包络路由器

**状态：** `mertens_envelope_split_low_finite_high_explicit_open`

prime-harmonic/Mertens 包络又被压窄一层：低阈值 P^u<286 是有限素数阶梯表，可精确保留；真正剩余是 x>=286 的显式素数倒数 Mertens 统一误差，以及它与 B=3 边界变差的合成。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
prime_harmonic_mertens_envelope_reduced=true
low_prime_step_finite_ledger_closed=true
explicit_prime_reciprocal_mertens_envelope_proved=false
boundary_variation_transfer_proved=false
beta_sieve_main_coefficient_99pct_proved=false
row_column_unconditional_closed=false
```

## 1. 低阈值有限账本

| item | value |
| --- | ---: |
| cutoff x | 286 |
| z at P=100000 | 141.253754 |
| primes below cutoff | 61 |
| largest prime below cutoff | 283 |
| active primes at tail start | 34 |
| largest active prime at tail start | 139 |
| low step mass below cutoff | 2.009442439216 |
| active low step mass at tail start | 1.879797711065 |

## 2. 自足替换

```text
B3PrimeHarmonicMertensUniformEnvelopePGe100000
  =>
(B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND ExplicitPrimeReciprocalMertensEnvelopeXGe286)
```

Rosser-Schoenfeld/Dusart type explicit bounds for reciprocal prime sums would close the high-x envelope as an external standard input; an internal self-contained proof is not yet present.

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeHarmonicMertensGateActive | `true` | `false` | 上一层最新最窄点是 prime-harmonic/Mertens 统一包络。 | B3PrimeHarmonicMertensUniformEnvelopePGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的筛主系数误差，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| BoundarySplitAvailable | `true` | `true` | 交错边界余项已经拆成一维 Mertens 包络与 B=3 边界变差传递。 | 无上游拆分剩余。 |
| LogScaleTransferClosed | `true` | `true` | 变量 x=P^u 把 H_P(u)=sum_{p<P^u}1/p 精确转为素数倒数部分和，u 只改变阈值。 | 无尺度变换剩余。 |
| LowPrimeStepFiniteLedgerClosed | `true` | `true` | P^u<286 的阶梯部分只涉及有限素数表，可逐点精确保留，不进入渐近误差。 | B3LowPrimeStepFiniteLedgerXLt286PGe100000 |
| HighXExplicitMertensEnvelopeStillNeeded | `false` | `false` | P^u>=286 的统一包络需要显式素数倒数 Mertens 定理或自足证明。 | ExplicitPrimeReciprocalMertensEnvelopeXGe286 |
| MertensEnvelopeSplitToLowFiniteAndHighExplicit | `true` | `false` | Mertens 包络原子被压成低素数有限阶梯账本和高阈值显式 reciprocal-prime Mertens 包络。 | B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND ExplicitPrimeReciprocalMertensEnvelopeXGe286 |
| ExplicitPrimeReciprocalMertensEnvelopeXGe286 | `false` | `false` | 需要引用或证明 sum_{p<=x}1/p=log log x+B1+E(x) 的显式统一误差，至少覆盖 x>=286。 | ExplicitPrimeReciprocalMertensEnvelopeXGe286 |
| B3BoundaryVariationOnePercentTransferLedger | `false` | `false` | 高阈值 Mertens 包络还必须与 B=3 边界变差传递合成，才能关闭 1% 余项。 | B3BoundaryVariationOnePercentTransferLedger |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代高阈值 Mertens 与变差合成。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND ExplicitPrimeReciprocalMertensEnvelopeXGe286) AND B3BoundaryVariationOnePercentTransferLedger) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND ExplicitPrimeReciprocalMertensEnvelopeXGe286) AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND ExplicitPrimeReciprocalMertensEnvelopeXGe286) AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

先攻 `ExplicitPrimeReciprocalMertensEnvelopeXGe286`，再攻 `B3BoundaryVariationOnePercentTransferLedger`。
