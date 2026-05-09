# Prime Matrix B=3 内部 psi_0 精确显式公式路由器

**状态：** `internal_psi0_exact_formula_closed_truncation_kernel_open`

内部 psi_0 精确显式公式已经闭合：通过 Perron 半权入口、移线取留数和对称零点和，得到 x>1 上的无截断公式。该结论只关闭公式身份本身；真正数值余项 R_T 和零点尾和预算仍开放，下一最窄点为 PerronKernelTruncationConstantForPsi0Ledger。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
internal_psi0_exact_formula_closed=true
perron_kernel_truncation_constant_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger
  =>
InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost
```

## 2. 定理合同

| item | value |
| --- | --- |
| domain | `x>1；本项目只需 x>=20000` |
| psi0 | `psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer` |
| closed_formula | `psi_0(x)=x-sum_rho x^rho/rho-log(2*pi)-1/2*log(1-x^-2)` |
| zero_sum_mode | `对称极限 lim_{T->infty} sum_{\|Im rho\|<T}` |
| what_is_not_closed | `截断到有限 T 的 R_T 常数与零点尾和预算仍未闭合` |

## 3. 证明链

| step | closed | reason |
| --- | --- | --- |
| Perron半权入口 | `true` | 对 -zeta'/zeta(s)=sum Lambda(n)n^-s 使用 Perron 半权公式，得到 psi_0 端点规范。 |
| 矩形移线 | `true` | 用 zeta 的亚指数竖线增长与端点避零序列，把积分线移到左侧并取对称极限。 |
| 留数清单 | `true` | s=1 给 x，非平凡零点给 -x^rho/rho，s=0 给 -log(2*pi)，平凡零点给 -1/2 log(1-x^-2)。 |
| 对称零点和 | `true` | 按 \|Im rho\|<T 的共轭对称极限解释零点和，避免条件收敛顺序歧义。 |
| 有限截断余项 | `false` | 本步不估计 finite T 余项；该任务留给 PerronKernelTruncationConstantForPsi0Ledger。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| InternalPsi0FormulaGateActive | `true` | `false` | 上一层把外部高阈值 RvM 候选排除为严格闭合后，当前最窄点是内部 psi_0 公式。 | InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ZetaMeromorphicHadamardBasisAvailable | `true` | `true` | zeta/xi 函数方程、亚纯延拓、Hadamard/零点结构已经在前序基础包登记。 | CompletedZetaXiFunctionalEquationAndHadamardProductClosed |
| Psi0EndpointConventionAvailable | `true` | `true` | psi_0 半权端点口径已经闭合，跳点不再造成公式歧义。 | ChebyshevPsi0EndpointHalfWeightConventionClosed |
| ResidueFormulaProofClosed | `true` | `true` | Perron 半权入口、矩形移线、留数清单和对称零点和给出无截断精确公式。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger | `true` | `true` | 内部 all-x psi_0 精确公式闭合；但该闭合不含 finite-T 截断常数。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| PerronKernelTruncationConstantForPsi0Ledger | `false` | `false` | 下一步必须把精确公式截断为 \|gamma\|<=T 并给出 R_T 常数。 | PerronKernelTruncationConstantForPsi0Ledger |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 截断核常数之后，仍需把 C=1280,T0=14 代入零点尾和预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |
| PerronTruncationTrivialZeroPrimePowerTailBudgetLedger | `false` | `false` | 平凡零点与素数幂/尾项同口径预算仍是独立子账本。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

当前最窄点更新为 `PerronKernelTruncationConstantForPsi0Ledger`；完成后再进入 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger`。
