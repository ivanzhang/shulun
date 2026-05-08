# Prime Matrix B=3 交错边界余项终端路由器

**状态：** `boundary_remainder_split_to_mertens_and_variation_inputs_open`

B=3 交错边界余项是当前内部 beta-sieve 线的真实终端。它不能靠有限 checkpoint 直接闭合，也不能把标准基本引理改名为自足证明。本步把它拆成两个最小可攻输入：显式 prime-harmonic/Mertens 统一包络，以及 B=3 admissible 区域的边界变差传递账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
alternating_boundary_remainder_atom_reduced=true
alternating_boundary_remainder_one_percent_proved=false
beta_sieve_main_coefficient_99pct_proved=false
row_column_unconditional_closed=false
```

## 1. checkpoint 余量

```text
checkpoint_count=7
min_checkpoint_P=10000000
min_checkpoint_ratio=1.5527757826943358
min_surplus_to_99pct=0.5627757826943358
```

## 2. 自足替换

```text
B3AlternatingBoundaryRemainderOnePercentLedger
  =>
(B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger)
```

If the standard Rosser-Iwaniec beta-sieve fundamental lemma is accepted as an external theorem, the B=3 alternating boundary remainder closes externally. The current self-contained chain does not yet include that proof.

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AlternatingBoundaryGateActive | `true` | `false` | 最新唯一内部 beta-sieve 点是 B=3 交错边界余项的一百分点控制。 | B3AlternatingBoundaryRemainderOnePercentLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条中的筛主系数，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExactStieltjesLedgerAvailable | `true` | `true` | prime-word 离散和已精确表示为 Stieltjes 积分；误差只来自阶梯测度到连续密度的替换。 | 无表示层剩余。 |
| LargeFiniteMarginRegistered | `true` | `false` | checkpoint 最小余量约 0.5628，高于 1% 目标许多；但有限余量不是全尾段证明。 | 需要统一尾段误差界。 |
| DirectInternalClosureBlocked | `true` | `true` | 当前仓库尚无显式 prime-harmonic 包络和 B=3 边界变差合成定理，不能把标准基本引理冒充自足证明。 | B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger |
| BoundaryAtomSplitToMertensAndVariation | `true` | `false` | 交错边界余项被压成两个真正原子：一维素数倒数 Mertens 包络与 B=3 区域边界变差传递。 | B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger |
| B3PrimeHarmonicMertensUniformEnvelopePGe100000 | `false` | `false` | 需要显式证明 P>=100000、0<u<=0.43 下 H_P(u)=sum_{p<P^u}1/p 与 log u+C_P 的统一误差包络。 | B3PrimeHarmonicMertensUniformEnvelopePGe100000 |
| B3BoundaryVariationOnePercentTransferLedger | `false` | `false` | 需要证明该一维误差经过 B=3 admissible 多面体和交错截断后，总损失小于 1% f(s) 或被 checkpoint 正余量吸收。 | B3BoundaryVariationOnePercentTransferLedger |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭这两个原子；但不是内部自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开整个内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((B3PrimeHarmonicMertensUniformEnvelopePGe100000 AND B3BoundaryVariationOnePercentTransferLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

先攻 `B3PrimeHarmonicMertensUniformEnvelopePGe100000`，再攻 `B3BoundaryVariationOnePercentTransferLedger`。
