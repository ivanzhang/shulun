# Prime Matrix 调和窗口 Dusart 显式账本路由器

**状态：** `harmonic_window_alpha043_upper0850_closed_skeleton_open`

本步关闭调和窗口上界。有限段 3001<=P<500000 直接精确枚举，最大值为 0.839537989723；尾段 P>=500000 用 Dusart 素数倒数和显式误差，得到统一上界 0.849293925490<0.850。因此 HarmonicWindowAlpha043PGe3001Upper0850Ledger 可从活动输入基中删除，下一最窄点转为动态粗骨架下界 S_Y(P)>=401。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
harmonic_window_alpha043_upper0850_closed=true
dynamic_rough_skeleton_lower401_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
closed_input_removed=HarmonicWindowAlpha043PGe3001Upper0850Ledger
closed_interface_atom=DusartPrimeReciprocalWindowAlpha043Upper0850Closed
```

## 1. 闭合律

```text
HarmonicWindowAlpha043PGe3001Upper0850Ledger
  =>
DusartPrimeReciprocalWindowAlpha043Upper0850Closed
  => 从活动输入基删除该调和窗口门。
```

使用的标准显式定理：Dusart, *Estimates of some functions over primes without R.H.*, arXiv:1002.0442。其素数倒数和定理给出上下误差项 `1/(10 log^2 x)+4/(15 log^3 x)`；上界侧要求 `x>=10372`，本路由尾段从 `P=500000` 起满足。

## 2. 两段账本

| segment | count/bound | worst | target | closed |
| --- | ---: | --- | ---: | --- |
| finite 3001<=P<500000 | 41108 primes | P=289181, cutoff=222, H=0.839537989723 | 0.850 | true |
| Dusart P>=500000 | bound | log(1/alpha)+err(P)+err(P^alpha)=0.849293925490 | 0.850 | true |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| HarmonicWindowGateActive | `true` | `false` | 最新最窄点是 P>=3001 的高素窗口调和和上界。 | HarmonicWindowAlpha043PGe3001Upper0850Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍在假设早期零行反例链条的模型余量账本内，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FiniteHarmonicWindow3001To499999 | `true` | `true` | 3001<=P<500000 的素数窗口已精确枚举，最大调和和仍小于 0.850。 | 有限段关闭。 |
| DusartPrimeReciprocalTheoremSpecialized | `true` | `true` | Dusart 素数倒数和显式误差给出 P>=500000 的窗口上界。 | DusartPrimeReciprocalWindowAlpha043Upper0850Closed |
| HarmonicWindowAlpha043PGe3001Upper0850Ledger | `true` | `true` | 有限核查与 Dusart 尾段合并，调和窗口 H(P)<=0.850 已闭合。 | DusartPrimeReciprocalWindowAlpha043Upper0850Closed |
| DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger | `false` | `false` | 动态粗骨架 S_Y(P)>=401 仍是模型余量侧的剩余解析输入。 | DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

下一步直接攻 `DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger`：证明把所有 `q<=P^0.43` 提升进底座后，`1<=k<P` 中避开这些低素同余类的动态粗骨架在 plus/minus 两侧均至少 `401`。
