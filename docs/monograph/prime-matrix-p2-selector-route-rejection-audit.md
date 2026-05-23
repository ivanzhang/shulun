# Prime Matrix P2 最早见证选择器路线反证审计

**状态**：`least_p2_prime_selector_route_rejected_by_finite_counterexamples`
**核验日期**：`2026-05-23`

## 1. 原子结论

- “最早 P2 见证就是素数”不是可用破奇偶路线；它已有有限反例。
- 该反例在排除平凡 `n<=P` 见证后仍存在。
- 因此上一层剩余基中的 `PrimeBeforeCompositeP2SelectorInEveryFixedClass` 必须删除或改名为需要新分布输入的非最早选择器问题。

## 2. 首个反例

```text
P=3
X=floor(P^1.8345)=7
a=1
least_P2_after_P=4
factors=[2, 2]
```

## 3. 大样本审计

| P | X=floor(P^1.8345) | first P2 prime | first P2 composite | missing | composite share |
|---:|---:|---:|---:|---:|---:|
| 101 | 4752 | 43 | 57 | 0 | 0.570000 |
| 199 | 16490 | 76 | 122 | 0 | 0.616162 |
| 499 | 89056 | 179 | 319 | 0 | 0.640562 |
| 997 | 317034 | 355 | 641 | 0 | 0.643574 |

```text
large_sample_all_have_counterexamples=true
max_composite_first_share: P=19, share=0.666667
```

## 4. 更新后的剩余基

```text
SmallFactorCofactorAPCompositeFiberDominanceBound
NonleastPrimeSelectorRequiresAdditionalDistributionInput
FixedPrimeModulusZeroExceptionTransferForPrimeObjects
SameObjectNonlinearActualSourceConstructorBeforeProjection
PointwiseShortIntervalPrimeTheoremThetaLeHalf
LinnikExponentLeTwoWithSquareWindowConstants
```

## 5. 边界声明

本审计只排除一个错误选择器路线；它没有证明 P2 到素数的无条件转移。

```text
selector_route_rejected=true
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```
