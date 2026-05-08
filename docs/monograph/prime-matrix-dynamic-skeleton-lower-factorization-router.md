# Prime Matrix 动态粗骨架下界因子化路由器

**状态：** `dynamic_skeleton_lower_factorized_finite_closed_tail_linear_sieve_open`

本步把动态粗骨架下界压成有限桥接与尾段线性筛。有限段 3001<=P<100000 已由现有动态提升轮审计关闭，最小骨架数为 456，出现在 P=3023 plus 侧。因此当前唯一剩余是 P>=100000 的一维 lower-bound sieve 显式尾段账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
dynamic_skeleton_lower_factorized=true
finite_dynamic_skeleton_certificate_closed=true
tail_linear_lower_sieve_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 因子化律

```text
DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
  =>
LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger
  + FiniteDynamicRoughSkeletonAlpha043P3001To99991Certificate(closed)
```

## 2. 两段账本

| segment | records | primes | min S | worst record | target | status |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| 3001<=P<100000 | 18324 | 9162 | 456 | P=3023, plus, cutoff=31 | 401 | closed finite certificate |
| P>=100000 | - | - | - | lower-bound sieve with s=2.325581 | 401 | open analytic ledger |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DynamicSkeletonLowerGateActive | `true` | `false` | 最新最窄点是动态粗骨架 S_Y(P)>=401。 | DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍处理假设早期零行链条中的模型余量账本，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FiniteDynamicRoughSkeletonAlpha043P3001To99991Certificate | `true` | `true` | 3001<=P<100000 的动态粗骨架已由现有审计逐点核查，最小值仍大于 401。 | 有限桥接段关闭。 |
| TailLinearSieveReduction | `true` | `false` | P>=100000 的骨架下界被压成标准一维 lower-bound sieve 尾段账本。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger | `false` | `false` | 需要把线性筛下界常数、端点误差和 floor(P^0.43) 取整统一写成显式可审稿不等式。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger | `true` | `false` | 原骨架下界已分解为有限桥接证书与尾段 lower-sieve 输入；尚未整体证明。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

直接攻 `LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger`：把一维 lower-bound sieve 在 `z=P^0.43`、`D≈P`、`s=1/0.43` 的显式常数、端点误差和取整误差全部写成一个可验算不等式，目标只需证明尾段骨架数至少 `401`。
