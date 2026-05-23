# Prime Matrix P2 到素数转移原子审计

**状态**：`p2_wrong_object_split_to_small_factor_cofactor_ap_fibers_open`
**核验日期**：`2026-05-23`

## 1. 原子结论

- `P2` almost-prime 进入方阵只关闭位置门，不关闭素数对象门。
- 合成 `P2` 见证在非零列中必有小素因子 `r<P`，并精确落到 cofactor AP `m=a*r^{-1} mod P`。
- 对 Li--Zhang--Cai 指数 `1.8345`，小因子门进一步为 `r<=P^0.91725`。
- 因此从 `P2` 升级到 prime 的真剩余不是筛恒等式，而是半素数 cofactor AP 纤维不能耗尽固定列。

## 2. 精确转移原子

```text
If P is prime, 1<=a<P, n≡a mod P, Ω(n)=2 and n<P^2, then n=r*m with prime r<P and m≡a*r^{-1} mod P. If n<=P^sigma with sigma<2, then r<=P^(sigma/2).
cofactor_ap_identity_closed=true
small_factor_bound_sample_closed=true
lzc_small_factor_bound_sample_closed=true
```

## 3. 有限样本读数

| P | primes <=P^2 | composite P2 <=P^2 | P2/prime ratio | least P2 composite share | LZC bound | LZC P2 residues |
|---:|---:|---:|---:|---:|---:|---:|
| 101 | 1251 | 2650 | 2.118305 | 0.550000 | 4752 | 100 |
| 199 | 4163 | 9651 | 2.318280 | 0.580808 | 16490 | 198 |
| 499 | 21963 | 55623 | 2.532578 | 0.632530 | 89056 | 498 |
| 997 | 78059 | 208680 | 2.673362 | 0.621486 | 317034 | 996 |

样本极值：

```text
max_semiprime_to_prime_ratio_square: P=997, ratio=2.673362
max_least_p2_composite_share_square: P=929, share=0.641164
```

## 4. 最新剩余基

```text
SmallFactorCofactorAPCompositeFiberDominanceBound
PrimeBeforeCompositeP2SelectorInEveryFixedClass
FixedPrimeModulusZeroExceptionTransferForPrimeObjects
SameObjectNonlinearActualSourceConstructorBeforeProjection
PointwiseShortIntervalPrimeTheoremThetaLeHalf
LinnikExponentLeTwoWithSquareWindowConstants
```

## 5. 边界声明

本审计闭合的是 `P2` 合成见证的纤维定位，不是 P2 到素数的无条件转移。

```text
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```
