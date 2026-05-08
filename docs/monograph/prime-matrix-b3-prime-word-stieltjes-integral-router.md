# Prime Matrix B=3 prime-word Stieltjes 积分账本路由器

**状态：** `prime_word_stieltjes_exact_ledger_closed_boundary_remainder_open`

Stieltjes 账本已经闭合：prime-word 离散倒数和与迭代 Stieltjes 积分是同一个对象的两种写法。本步没有使用外部定理，也没有用有限 checkpoint 外推。剩余唯一内部 beta-sieve 点变成 B3AlternatingBoundaryRemainderOnePercentLedger，即阶梯测度到连续密度的交错边界余项控制。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
prime_word_stieltjes_integral_ledger_closed=true
alternating_boundary_remainder_one_percent_proved=false
discrete_prime_sum_uniform_error_proved=false
beta_sieve_main_coefficient_99pct_proved=false
row_column_unconditional_closed=false
```

## 1. 精确公式

```text
For each r, sum_{p1>...>pr, B3-admissible} (-1)^r/(p1...pr) = (-1)^r int_{Omega_r(B=3)} dH_P(u1)...dH_P(ur), with H_P(u)=sum_{p<P^u, p<P^0.43} 1/p.

Omega_r(B=3): 0<u_r<...<u_1<0.43 and u1+...+u_{2m-1}+3u_{2m}<1 for every 1<=2m<=r.
```

## 2. 证明骨架

- H_P is a finite right-continuous step function with jump 1/p at u=log p/log P.
- A one-dimensional Stieltjes integral against dH_P is exactly summation over prime atoms.
- Iterating the integral over the ordered region enforces p1>...>pr without multiplicity.
- The B=3 Rosser word gates are exactly the listed linear inequalities in log coordinates.
- Thus the Stieltjes expression is an exact rewriting of the finite prime-word sum, with no analytic error.
- All analytic loss is therefore isolated in the next atom: replacing dH_P by its continuous model across alternating moving boundaries.

## 3. 替换

```text
B3PrimeWordStieltjesIntegralUniformLedgerPGe100000
  =>
EXACT_PRIME_WORD_STIELTJES_REPRESENTATION_CLOSED
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StieltjesLedgerGateActive | `true` | `false` | 上一层把离散素和误差压成 prime-word Stieltjes 表示和交错边界余项。 | B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只做精确表示，不使用真实零行缺席或有限样本外推。 | 保持 row_column_unconditional_closed=false。 |
| DiscreteErrorBoundaryReductionAvailable | `true` | `true` | 离散误差已经被拆成 Stieltjes 表示账本和边界余项账本。 | 无拆分层剩余。 |
| PrimeReciprocalStepMeasurePinned | `true` | `true` | 定义 H_P(t)=sum_{p<exp(t log P), p<P^0.43}1/p；其 Stieltjes 原子质量正好是 1/p。 | 无测度自由度。 |
| B3AdmissibleWordRegionPinned | `true` | `true` | B=3 admissible 条件在降序 log 坐标中是有限个线性半空间：sum_{i<2m}u_i+3u_{2m}<1。 | 无区域自由度。 |
| FinitePrimeWordSumEqualsIteratedStieltjesIntegral | `true` | `true` | 对每个 word length r，离散 prime-word 倒数和精确等于该区域上 dH_P 的 r 重 Stieltjes 积分。 | 无误差项。 |
| B3PrimeWordStieltjesIntegralLedgerClosed | `true` | `true` | Stieltjes 账本只是精确重写，已经闭合；全部误差集中到交错边界余项。 | B3AlternatingBoundaryRemainderOnePercentLedger |
| B3AlternatingBoundaryRemainderOnePercentLedger | `false` | `false` | 仍需证明将阶梯测度 dH_P 替换为连续密度时，交错截断边界/跳变余项小于 1% f(s) 或整体正向。 | B3AlternatingBoundaryRemainderOnePercentLedger |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭边界余项；但不是内部自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((B3AlternatingBoundaryRemainderOnePercentLedger OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((B3AlternatingBoundaryRemainderOnePercentLedger OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((B3AlternatingBoundaryRemainderOnePercentLedger OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `B3AlternatingBoundaryRemainderOnePercentLedger`。
