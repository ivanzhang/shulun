# Triad-A1 连续 PDEC 签名 Prime-Lift 路由器

**状态：** `continuous_pdec_signatures_routed_to_prime_lift_gate`

连续 positive-limsup PDEC 输入的 prime-lift 刚性已物化：所有 40 个签名行都满足唯一同余。其中标准下一素数晋升行可直接接删除势/NoDeletion-KL；选择性晋升行需要先证明与较小尾素数晋升交换，或按 cofactor-order 缺口回流。

## 1. Prime-Lift 刚性律

任何 payment signature b=(ell,y,c) 都强制旧相位满足 t == 1-cP^{-1}-Qy (mod ell)，并强制升层相位 t+Qy 满足 t+Qy == 1-cP^{-1} (mod ell)。因此 positive-limsup finite signature 不是自由 PDEC 尖峰；它是把 ell 晋升进低模周期的合法 prime-lift 输入。

```text
signature b=(ell,y,c)；
row=t+Qy；
(row-1)P+c=0 mod ell；
therefore t=1-cP^{-1}-Qy mod ell。
```

这说明 positive-limsup PDEC 签名等价于新增素数层上的 residue 锁定。

## 2. 汇总

- `signature_row_count=40`。
- `all_signature_rows_have_prime_lift_congruence=True`。
- `route_counts={'SelectivePrimePromotionNeedsCommutationBeforeDeletionKL': 1, 'StandardNextPrimePromotionDeletionKLReady': 39}`。
- `promoted_prime_counts={13: 39, 17: 1}`。
- `standard_next_prime_row_count=39`。
- `selective_prime_row_count=1`。

## 3. P 汇总

| P | rows | promoted primes | routes | min Fourier/total |
| ---: | ---: | --- | --- | ---: |
| 17 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 1 |
| 19 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 1 |
| 23 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 0.998745 |
| 29 | 5 | `{13: 4, 17: 1}` | `{'SelectivePrimePromotionNeedsCommutationBeforeDeletionKL': 1, 'StandardNextPrimePromotionDeletionKLReady': 4}` | 0.997989 |
| 31 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 0.992125 |
| 37 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 0.998488 |
| 43 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 0.986379 |
| 47 | 5 | `{13: 5}` | `{'StandardNextPrimePromotionDeletionKLReady': 5}` | 0.989948 |

## 4. 签名行

| P | signature | ell | next ell | old t mod ell | lift mod ell | mass | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | `13:1:7` | 13 | 13 | 0 | 9 | 1 | `StandardNextPrimePromotionDeletionKLReady` |
| 17 | `13:2:8` | 13 | 13 | 7 | 12 | 1 | `StandardNextPrimePromotionDeletionKLReady` |
| 17 | `13:5:6` | 13 | 13 | 0 | 6 | 1 | `StandardNextPrimePromotionDeletionKLReady` |
| 17 | `13:4:12` | 13 | 13 | 1 | 11 | 1 | `StandardNextPrimePromotionDeletionKLReady` |
| 17 | `13:10:3` | 13 | 13 | 11 | 10 | 1 | `StandardNextPrimePromotionDeletionKLReady` |
| 19 | `13:11:10` | 13 | 13 | 0 | 8 | 19 | `StandardNextPrimePromotionDeletionKLReady` |
| 19 | `13:1:9` | 13 | 13 | 10 | 6 | 19 | `StandardNextPrimePromotionDeletionKLReady` |
| 19 | `13:4:11` | 13 | 13 | 0 | 10 | 18 | `StandardNextPrimePromotionDeletionKLReady` |
| 19 | `13:8:8` | 13 | 13 | 10 | 4 | 18 | `StandardNextPrimePromotionDeletionKLReady` |
| 19 | `13:10:9` | 13 | 13 | 7 | 6 | 17 | `StandardNextPrimePromotionDeletionKLReady` |
| 23 | `13:0:1` | 13 | 13 | 10 | 10 | 76 | `StandardNextPrimePromotionDeletionKLReady` |
| 23 | `13:12:9` | 13 | 13 | 0 | 4 | 76 | `StandardNextPrimePromotionDeletionKLReady` |
| 23 | `13:8:12` | 13 | 13 | 11 | 5 | 72 | `StandardNextPrimePromotionDeletionKLReady` |
| 23 | `13:4:11` | 13 | 13 | 12 | 9 | 72 | `StandardNextPrimePromotionDeletionKLReady` |
| 23 | `13:10:11` | 13 | 13 | 10 | 9 | 70 | `StandardNextPrimePromotionDeletionKLReady` |
| 29 | `13:0:2` | 13 | 13 | 9 | 9 | 272 | `StandardNextPrimePromotionDeletionKLReady` |
| 29 | `13:12:1` | 13 | 13 | 1 | 5 | 272 | `StandardNextPrimePromotionDeletionKLReady` |
| 29 | `17:8:6` | 17 | 13 | 8 | 9 | 204 | `SelectivePrimePromotionNeedsCommutationBeforeDeletionKL` |
| 29 | `13:0:4` | 13 | 13 | 4 | 4 | 148 | `StandardNextPrimePromotionDeletionKLReady` |
| 29 | `13:12:12` | 13 | 13 | 6 | 10 | 148 | `StandardNextPrimePromotionDeletionKLReady` |
| 31 | `13:2:4` | 13 | 13 | 3 | 8 | 10780 | `StandardNextPrimePromotionDeletionKLReady` |
| 31 | `13:7:2` | 13 | 13 | 0 | 11 | 10732 | `StandardNextPrimePromotionDeletionKLReady` |
| 31 | `13:5:3` | 13 | 13 | 10 | 3 | 10732 | `StandardNextPrimePromotionDeletionKLReady` |
| 31 | `13:10:1` | 13 | 13 | 7 | 6 | 10708 | `StandardNextPrimePromotionDeletionKLReady` |
| 31 | `13:12:4` | 13 | 13 | 4 | 8 | 3120 | `StandardNextPrimePromotionDeletionKLReady` |
| 37 | `13:7:2` | 13 | 13 | 4 | 2 | 62508 | `StandardNextPrimePromotionDeletionKLReady` |
| 37 | `13:5:9` | 13 | 13 | 6 | 12 | 62508 | `StandardNextPrimePromotionDeletionKLReady` |
| 37 | `13:8:8` | 13 | 13 | 11 | 5 | 62388 | `StandardNextPrimePromotionDeletionKLReady` |
| 37 | `13:4:3` | 13 | 13 | 12 | 9 | 62388 | `StandardNextPrimePromotionDeletionKLReady` |
| 37 | `13:3:10` | 13 | 13 | 5 | 6 | 60132 | `StandardNextPrimePromotionDeletionKLReady` |
| 43 | `13:5:1` | 13 | 13 | 11 | 4 | 11760408 | `StandardNextPrimePromotionDeletionKLReady` |
| 43 | `13:7:3` | 13 | 13 | 12 | 10 | 11755368 | `StandardNextPrimePromotionDeletionKLReady` |
| 43 | `13:0:1` | 13 | 13 | 4 | 4 | 11450880 | `StandardNextPrimePromotionDeletionKLReady` |
| 43 | `13:12:3` | 13 | 13 | 6 | 10 | 11450160 | `StandardNextPrimePromotionDeletionKLReady` |
| 43 | `13:2:2` | 13 | 13 | 2 | 7 | 11323512 | `StandardNextPrimePromotionDeletionKLReady` |
| 47 | `13:4:4` | 13 | 13 | 10 | 7 | 682835712 | `StandardNextPrimePromotionDeletionKLReady` |
| 47 | `13:8:4` | 13 | 13 | 0 | 7 | 681090552 | `StandardNextPrimePromotionDeletionKLReady` |
| 47 | `13:0:5` | 13 | 13 | 2 | 2 | 618189720 | `StandardNextPrimePromotionDeletionKLReady` |
| 47 | `13:12:3` | 13 | 13 | 8 | 12 | 618149400 | `StandardNextPrimePromotionDeletionKLReady` |
| 47 | `13:12:12` | 13 | 13 | 2 | 6 | 406006896 | `StandardNextPrimePromotionDeletionKLReady` |

## 5. 当前硬点

这一步把 `PDEC-CAP` 的 positive-limsup 输入进一步变成 prime-lift 输入。
标准下一素数行应接已有 PromotionDeletionPotential / NoDeletion-KL / CleanKLS 账本。
选择性素数行需要补一个交换律：先晋升较小尾素数再晋升该签名素数，不改变终端路由；
若交换律失败，失败本身是 cofactor-order/PDEC 缺口。
