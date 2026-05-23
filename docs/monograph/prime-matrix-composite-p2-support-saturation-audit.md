# Prime Matrix 合成 P2 支持饱和审计

**状态**：`composite_p2_residue_support_saturates_lzc_window_in_sample`
**核验日期**：`2026-05-23`

## 1. 原子结论

- 在 Li--Zhang--Cai 尺度 `X=P^1.8345` 内，样本行的合成 `P2` 对象本身已经覆盖全部非零列。
- 从 `P=499` 起，样本中每个非零列的合成 `P2` 计数都严格大于素数计数。
- 因此只使用 `P2` residue 支持或列覆盖的路线是奇偶盲的；必须加入区分 prime 与合成 `P2` 的对象敏感输入。

## 2. 样本审计

| P | X=floor(P^1.8345) | prime support | composite P2 support | min comp P2 | comp/prime ratio | comp>=prime cols | comp>prime cols | min(comp-prime) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 4752 | 100/100 | 100/100 | 8 | 2.015649 | 98/100 | 96/100 | -1 |
| 199 | 16490 | 198/198 | 198/198 | 13 | 2.196859 | 198/198 | 196/198 | 0 |
| 499 | 89056 | 498/498 | 498/498 | 27 | 2.426252 | 498/498 | 498/498 | 5 |
| 997 | 317034 | 996/996 | 996/996 | 54 | 2.562792 | 996/996 | 996/996 | 18 |
| 2003 | 1140075 | 2002/2002 | 2002/2002 | 88 | 2.684857 | 2002/2002 | 2002/2002 | 32 |
| 5003 | 6112774 | 5002/5002 | 5002/5002 | 195 | 2.826571 | 5002/5002 | 5002/5002 | 95 |

```text
all_sample_rows_composite_p2_support_saturated=true
first_strict_pointwise_composite_dominance: P=499, min(comp-prime)=5
largest_sample: P=5003, min_composite_p2_count=195, comp/prime_ratio=2.826571
```

## 3. 更新后的剩余基

```text
ObjectSensitivePrimeMinusCompositeP2SeparationInput
SmallFactorCofactorAPCompositeFiberDominanceBound
NonleastPrimeSelectorRequiresAdditionalDistributionInput
FixedPrimeModulusZeroExceptionTransferForPrimeObjects
SameObjectNonlinearActualSourceConstructorBeforeProjection
PointwiseShortIntervalPrimeTheoremThetaLeHalf
LinnikExponentLeTwoWithSquareWindowConstants
```

## 4. 边界声明

本审计删除的是 support-only 的 P2-to-prime 伪路线；它不是全 P 的定理，也没有证明素数存在命题。

```text
support_only_p2_to_prime_transfer_rejected=true
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```
