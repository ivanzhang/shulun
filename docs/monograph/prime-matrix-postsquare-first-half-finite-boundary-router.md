# Prime Matrix 平方后前半窗素数输入有限边界证书

**状态：** `first_half_prime_square_finite_boundary_verified_global_input_open`

有限审计已检查 `P<= 200000` 的 `(P^2,P^2+P)` 前半窗，未发现失败。但该输入等价于长度 `sqrt(x)` 级的特殊短区间素数命题；当前通用无条件素数间隙定理不能直接给出这个长度，有限验证也不能升级为全局证明。因此 final-tail 线仍不能声明自足闭合，主攻应回到非 final-tail 的 PDEC/SAE/预算放大路线。

```text
max_p=200000
prime_count=17984
failure_count=0
first_half_prime_square_input_current_corpus_proved=false
row_column_unconditional_closed=false
```

## 1. 最坏偏移样本

| P | least_offset | least_prime | offset/P |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 29 | 0.800000 |
| 3 | 2 | 11 | 0.666667 |
| 7 | 4 | 53 | 0.571429 |
| 11 | 6 | 127 | 0.545455 |
| 23 | 12 | 541 | 0.521739 |
| 2 | 1 | 5 | 0.500000 |
| 29 | 12 | 853 | 0.413793 |
| 19 | 6 | 367 | 0.315789 |
| 13 | 4 | 173 | 0.307692 |
| 41 | 12 | 1693 | 0.292683 |
| 43 | 12 | 1861 | 0.279070 |
| 17 | 4 | 293 | 0.235294 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteFirstHalfPrimeSquareScanCompleted` | `true` | `false` | 已有限检查素数 P<= 200000 的 (P^2,P^2+P) 前半窗。 | finite evidence only |
| `FiniteFailureFound` | `true` | `false` | 本次有限范围没有发现反例；若出现 failure，则 final-tail 路线立即失败。 | none in scanned range |
| `ExternalPrimeGapTheoremDirectlyMatchesLengthP` | `false` | `false` | 现有通用短区间素数定理仍给 x^theta 型长度，theta>1/2；代入 x=P^2 不能推出长度 P。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| `FirstHalfPrimeSquareInputProved` | `false` | `false` | 有限证书和现有通用素数间隙输入都不能升级为每个素数 P 的全局证明。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 3. 审稿边界

- `PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP` 是 final-tail 线的真实输入边界，不是已证引理。
- 现有有限验证只说明低范围无反例；不能替代全局短区间素数证明。
- 已登记外部短区间素数结果的指数仍大于 `1/2`，代入 `x=P^2` 只能给长于 `P` 的区间。
- 若不新增该强输入，下一步必须沿 `NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction` 继续寻找反例链与真实结构链的终端矛盾。

## 4. 外部短区间边界

| source | exponent | directly sufficient | url |
| --- | ---: | ---: | --- |
| Baker-Harman-Pintz 2001 | `0.525` | `false` | https://doi.org/10.1112/plms/83.3.532 |
| Runbo Li arXiv:2308.04458 v8 | `0.52` | `false` | https://arxiv.org/abs/2308.04458 |

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/postsquare-first-half-prime-finite-boundary-ledger.json` | `6bc0c8abe9244dfe135fbfe20b57cc4dce061f3abf93295c04ae4f4c550be67a` |
| `experiments/prime_matrix_postsquare_first_half_finite_boundary_router.py` | `e624025f475a2d1ee5c82102594503718c2f5427d4b3a31e4bdc228381d64bd2` |
