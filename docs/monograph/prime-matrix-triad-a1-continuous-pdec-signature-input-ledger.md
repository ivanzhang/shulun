# Triad-A1 连续 actual-payment PDEC 签名输入账本

**状态：** `continuous_positive_limsup_pdec_inputs_materialized_capacity_open`

连续 actual-payment 的 positive-limsup 分支已被物化为具体 finite-signature PDEC 输入账本。这关闭了“正 limsup 签名是否合法”的子问题；仍未关闭 PDEC-CAP 容量比较。

## 1. 输入律

若 canonical actual payment 的有限签名沿反例塔有正 limsup 质量，则该签名的 phase profile g_b(t) 是合法同集 PDEC 输入：它由真实完成态、真实低洞、真实 column-tail 支付桶共同定义。非零 Fourier 信号给出 PDEC 测试方向；剩余未闭合的是该方向上的容量不等式 U_CRT<L_PDEC。

```text
positive-limsup finite signature b=(prime,residue,column-residue)
=> g_b(t)=# canonical actual payments at phase t using b
=> finite column-tail formal row
=> PDEC capacity comparison U_CRT<L_PDEC still required。
```

## 2. 汇总

- `cap_count=8`。
- `signature_row_count=40`。
- `route_counts={'FiniteSignaturePDECInputMaterialized': 40}`。
- `all_signature_rows_have_prime_lift_congruence=True`。
- `promoted_prime_counts={13: 39, 17: 1}`。
- `global_min_signature_fourier_abs_over_total=0.986379`。
- `global_max_signature_fourier_abs_over_total=1`。

## 3. Cap 汇总

| P | top signatures | routes |
| ---: | ---: | --- |
| 17 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 19 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 23 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 29 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 31 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 37 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 43 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |
| 47 | 5 | `{'FiniteSignaturePDECInputMaterialized': 5}` |

## 4. 签名行

| P | signature | ell | t mod ell | lift mod ell | mass | phases | best h | Fourier/total | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | `13:1:7` | 13 | 0 | 9 | 1 | 1 | 1 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 17 | `13:2:8` | 13 | 7 | 12 | 1 | 1 | 1 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 17 | `13:5:6` | 13 | 0 | 6 | 1 | 1 | 1 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 17 | `13:4:12` | 13 | 1 | 11 | 1 | 1 | 1 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 17 | `13:10:3` | 13 | 11 | 10 | 1 | 1 | 1 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 19 | `13:11:10` | 13 | 0 | 8 | 19 | 3 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 19 | `13:1:9` | 13 | 10 | 6 | 19 | 3 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 19 | `13:4:11` | 13 | 0 | 10 | 18 | 2 | 616 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 19 | `13:8:8` | 13 | 10 | 4 | 18 | 2 | 77 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 19 | `13:10:9` | 13 | 7 | 6 | 17 | 1 | 5 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 23 | `13:0:1` | 13 | 10 | 10 | 76 | 5 | 533 | 0.998745 | `FiniteSignaturePDECInputMaterialized` |
| 23 | `13:12:9` | 13 | 0 | 4 | 76 | 5 | 533 | 0.998745 | `FiniteSignaturePDECInputMaterialized` |
| 23 | `13:8:12` | 13 | 11 | 5 | 72 | 3 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 23 | `13:4:11` | 13 | 12 | 9 | 72 | 3 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 23 | `13:10:11` | 13 | 10 | 9 | 70 | 2 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 29 | `13:0:2` | 13 | 9 | 9 | 272 | 7 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 29 | `13:12:1` | 13 | 1 | 5 | 272 | 7 | 1155 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 29 | `17:8:6` | 17 | 8 | 9 | 204 | 2 | 770 | 1 | `FiniteSignaturePDECInputMaterialized` |
| 29 | `13:0:4` | 13 | 4 | 4 | 148 | 7 | 533 | 0.997989 | `FiniteSignaturePDECInputMaterialized` |
| 29 | `13:12:12` | 13 | 6 | 10 | 148 | 7 | 533 | 0.997989 | `FiniteSignaturePDECInputMaterialized` |
| 31 | `13:2:4` | 13 | 3 | 8 | 10780 | 13 | 533 | 0.999216 | `FiniteSignaturePDECInputMaterialized` |
| 31 | `13:7:2` | 13 | 0 | 11 | 10732 | 11 | 533 | 0.998868 | `FiniteSignaturePDECInputMaterialized` |
| 31 | `13:5:3` | 13 | 10 | 3 | 10732 | 11 | 533 | 0.998868 | `FiniteSignaturePDECInputMaterialized` |
| 31 | `13:10:1` | 13 | 7 | 6 | 10708 | 11 | 533 | 0.999307 | `FiniteSignaturePDECInputMaterialized` |
| 31 | `13:12:4` | 13 | 4 | 8 | 3120 | 10 | 533 | 0.992125 | `FiniteSignaturePDECInputMaterialized` |
| 37 | `13:7:2` | 13 | 4 | 2 | 62508 | 8 | 241 | 0.998607 | `FiniteSignaturePDECInputMaterialized` |
| 37 | `13:5:9` | 13 | 6 | 12 | 62508 | 8 | 241 | 0.998607 | `FiniteSignaturePDECInputMaterialized` |
| 37 | `13:8:8` | 13 | 11 | 5 | 62388 | 8 | 241 | 0.998488 | `FiniteSignaturePDECInputMaterialized` |
| 37 | `13:4:3` | 13 | 12 | 9 | 62388 | 8 | 241 | 0.998488 | `FiniteSignaturePDECInputMaterialized` |
| 37 | `13:3:10` | 13 | 5 | 6 | 60132 | 10 | 533 | 0.999552 | `FiniteSignaturePDECInputMaterialized` |
| 43 | `13:5:1` | 13 | 11 | 4 | 11760408 | 42 | 533 | 0.986379 | `FiniteSignaturePDECInputMaterialized` |
| 43 | `13:7:3` | 13 | 12 | 10 | 11755368 | 41 | 533 | 0.986382 | `FiniteSignaturePDECInputMaterialized` |
| 43 | `13:0:1` | 13 | 4 | 4 | 11450880 | 48 | 1777 | 0.986633 | `FiniteSignaturePDECInputMaterialized` |
| 43 | `13:12:3` | 13 | 6 | 10 | 11450160 | 47 | 1777 | 0.986633 | `FiniteSignaturePDECInputMaterialized` |
| 43 | `13:2:2` | 13 | 2 | 7 | 11323512 | 42 | 533 | 0.990446 | `FiniteSignaturePDECInputMaterialized` |
| 47 | `13:4:4` | 13 | 10 | 7 | 682835712 | 50 | 533 | 0.99489 | `FiniteSignaturePDECInputMaterialized` |
| 47 | `13:8:4` | 13 | 0 | 7 | 681090552 | 52 | 533 | 0.994881 | `FiniteSignaturePDECInputMaterialized` |
| 47 | `13:0:5` | 13 | 2 | 2 | 618189720 | 53 | 1777 | 0.996031 | `FiniteSignaturePDECInputMaterialized` |
| 47 | `13:12:3` | 13 | 8 | 12 | 618149400 | 52 | 533 | 0.996034 | `FiniteSignaturePDECInputMaterialized` |
| 47 | `13:12:12` | 13 | 2 | 6 | 406006896 | 40 | 533 | 0.989948 | `FiniteSignaturePDECInputMaterialized` |

## 5. 当前硬点

本账本完成的是 PDEC 输入合法性与方向物化；它没有证明容量上界。
下一步必须对这些 `g_b(t)` 加入同集容量行并证明：

```text
U_CRT(g_b; h,zeta) < L_PDEC(g_b)。
```

若该比较失败，失败对象应输出更窄 DualCap、缺失 column-tail/cofactor 行，或回到 diffuse CleanKLS。
