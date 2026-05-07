# Triad-A1 晋升删除势账本

**状态：** `promotion_deletion_potential_materialized`

当前 Q=2310 的 top-prime 晋升层全部具有正删除势。这不是全局常数证明；它把当前层纳入可累加删除势账本，并给出未来层的严格门控。

## 1. 删除势律

每次 top-prime 晋升产生本地删除势 D_n=-log(a_n)。若沿无限晋升塔 sum D_n 发散，则支撑密度趋零；若 sum D_n 可求和，则 a_n->1，必须进入 NoDeletion-KL / CleanKLS / PDEC 回流。

形式上，对每层晋升：

```text
a_n = lift_survival_rate；
D_n = -log(a_n)。
```

于是：

```text
sum D_n = infinity  => 支撑密度趋零，进入 Sparse/LocalSurvivor/PDEC；
sum D_n < infinity  => a_n -> 1，进入 NoDeletion-KL / CleanKLS；
某固定 residue/cap 持久 => PDEC 回流。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `promotion_deletion_potential_script` | `34c22dc9d641b79a6a20670586506b204f9c89f7037ac3d224eb3c1caed01450` |
| `topprime_promotion_json` | `7d35be2091b3007ef596ea4fccfe21b4ec60b9b8ffe2bf280b0919747edc5df2` |

## 3. 汇总

- `cap_count=68`。
- `all_positive_deletion_potential=True`。
- `global_min_deletion_potential_current_layer=0.880079`。
- `global_max_survival_current_layer=0.41475`。

| P | caps | min survival | max survival | min D | max D | positive D |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | 8 | 0.0769231 | 0.0769231 | 2.56495 | 2.56495 | `True` |
| 19 | 12 | 0.204743 | 0.238462 | 1.43355 | 1.586 | `True` |
| 23 | 12 | 0.327427 | 0.384615 | 0.955511 | 1.11649 | `True` |
| 29 | 12 | 0.302294 | 0.356838 | 1.03047 | 1.19635 | `True` |
| 31 | 12 | 0.292721 | 0.41475 | 0.880079 | 1.22854 | `True` |
| 37 | 12 | 0.239126 | 0.351648 | 1.04512 | 1.43076 | `True` |

## 4. Cap 删除势明细

| P | alpha | h | dir | survival | deletion | D=-log(a) | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | 0 | 374 | 0 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0 | 1936 | 0 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0 | 374 | 0 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0 | 1936 | 0 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0.5 | 1001 | 0.25 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0.5 | 1309 | 0.75 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0.5 | 1001 | 0.25 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 17 | 0.5 | 1309 | 0.75 | 0.0769231 | 0.923077 | 2.56495 | `PositiveDeletionPotential` |
| 19 | 0 | 847 | 0.25 | 0.204743 | 0.795257 | 1.586 | `PositiveDeletionPotential` |
| 19 | 0 | 1463 | 0.75 | 0.204743 | 0.795257 | 1.586 | `PositiveDeletionPotential` |
| 19 | 0 | 847 | 0.25 | 0.204743 | 0.795257 | 1.586 | `PositiveDeletionPotential` |
| 19 | 0 | 1463 | 0.75 | 0.204743 | 0.795257 | 1.586 | `PositiveDeletionPotential` |
| 19 | 0.5 | 847 | 0.25 | 0.213751 | 0.786249 | 1.54294 | `PositiveDeletionPotential` |
| 19 | 0.5 | 1463 | 0.75 | 0.213751 | 0.786249 | 1.54294 | `PositiveDeletionPotential` |
| 19 | 0.5 | 847 | 0.25 | 0.213751 | 0.786249 | 1.54294 | `PositiveDeletionPotential` |
| 19 | 0.5 | 1463 | 0.75 | 0.213751 | 0.786249 | 1.54294 | `PositiveDeletionPotential` |
| 19 | 0.9 | 1265 | 0.25 | 0.238462 | 0.761538 | 1.43355 | `PositiveDeletionPotential` |
| 19 | 0.9 | 1045 | 0.75 | 0.238462 | 0.761538 | 1.43355 | `PositiveDeletionPotential` |
| 19 | 0.9 | 1265 | 0.25 | 0.238462 | 0.761538 | 1.43355 | `PositiveDeletionPotential` |
| 19 | 0.9 | 1045 | 0.75 | 0.238462 | 0.761538 | 1.43355 | `PositiveDeletionPotential` |
| 23 | 0 | 1045 | 0.25 | 0.327427 | 0.672573 | 1.11649 | `PositiveDeletionPotential` |
| 23 | 0 | 1045 | 0.25 | 0.327427 | 0.672573 | 1.11649 | `PositiveDeletionPotential` |
| 23 | 0 | 1265 | 0.75 | 0.328969 | 0.671031 | 1.11179 | `PositiveDeletionPotential` |
| 23 | 0 | 1265 | 0.75 | 0.328969 | 0.671031 | 1.11179 | `PositiveDeletionPotential` |
| 23 | 0.5 | 1045 | 0.25 | 0.335664 | 0.664336 | 1.09164 | `PositiveDeletionPotential` |
| 23 | 0.5 | 1265 | 0.75 | 0.335664 | 0.664336 | 1.09164 | `PositiveDeletionPotential` |
| 23 | 0.5 | 1045 | 0.25 | 0.335664 | 0.664336 | 1.09164 | `PositiveDeletionPotential` |
| 23 | 0.5 | 1265 | 0.75 | 0.335664 | 0.664336 | 1.09164 | `PositiveDeletionPotential` |
| 23 | 0.9 | 1045 | 0.25 | 0.384615 | 0.615385 | 0.955511 | `PositiveDeletionPotential` |
| 23 | 0.9 | 1265 | 0.75 | 0.384615 | 0.615385 | 0.955511 | `PositiveDeletionPotential` |
| 23 | 0.9 | 1045 | 0.25 | 0.384615 | 0.615385 | 0.955511 | `PositiveDeletionPotential` |
| 23 | 0.9 | 1265 | 0.75 | 0.384615 | 0.615385 | 0.955511 | `PositiveDeletionPotential` |
| 29 | 0 | 715 | 0.25 | 0.313148 | 0.686852 | 1.16108 | `PositiveDeletionPotential` |
| 29 | 0 | 715 | 0.25 | 0.313148 | 0.686852 | 1.16108 | `PositiveDeletionPotential` |
| 29 | 0 | 1595 | 0.75 | 0.313226 | 0.686774 | 1.16083 | `PositiveDeletionPotential` |
| 29 | 0 | 1595 | 0.75 | 0.313226 | 0.686774 | 1.16083 | `PositiveDeletionPotential` |
| 29 | 0.5 | 1295 | 0.25 | 0.323964 | 0.676036 | 1.12712 | `PositiveDeletionPotential` |
| 29 | 0.5 | 1015 | 0.75 | 0.323964 | 0.676036 | 1.12712 | `PositiveDeletionPotential` |
| 29 | 0.5 | 715 | 0.25 | 0.302294 | 0.697706 | 1.19635 | `PositiveDeletionPotential` |
| 29 | 0.5 | 1595 | 0.75 | 0.302294 | 0.697706 | 1.19635 | `PositiveDeletionPotential` |
| 29 | 0.9 | 1295 | 0.25 | 0.356838 | 0.643162 | 1.03047 | `PositiveDeletionPotential` |
| 29 | 0.9 | 1015 | 0.75 | 0.356838 | 0.643162 | 1.03047 | `PositiveDeletionPotential` |
| 29 | 0.9 | 1155 | 0 | 0.312821 | 0.687179 | 1.16213 | `PositiveDeletionPotential` |
| 29 | 0.9 | 1155 | 0.5 | 0.312821 | 0.687179 | 1.16213 | `PositiveDeletionPotential` |
| 31 | 0 | 1085 | 0.75 | 0.321111 | 0.678889 | 1.13597 | `PositiveDeletionPotential` |
| 31 | 0 | 1225 | 0.25 | 0.324914 | 0.675086 | 1.1242 | `PositiveDeletionPotential` |
| 31 | 0.5 | 1225 | 0.25 | 0.357287 | 0.642713 | 1.02921 | `PositiveDeletionPotential` |
| 31 | 0.5 | 1085 | 0.75 | 0.357287 | 0.642713 | 1.02921 | `PositiveDeletionPotential` |
| 31 | 0 | 1287 | 0.25 | 0.295399 | 0.704601 | 1.21943 | `PositiveDeletionPotential` |
| 31 | 0 | 1023 | 0.75 | 0.29449 | 0.70551 | 1.22251 | `PositiveDeletionPotential` |
| 31 | 0.9 | 1225 | 0.25 | 0.41475 | 0.58525 | 0.880079 | `PositiveDeletionPotential` |
| 31 | 0.9 | 1085 | 0.75 | 0.41475 | 0.58525 | 0.880079 | `PositiveDeletionPotential` |
| 31 | 0.5 | 1287 | 0.25 | 0.312217 | 0.687783 | 1.16406 | `PositiveDeletionPotential` |
| 31 | 0.5 | 1023 | 0.75 | 0.312217 | 0.687783 | 1.16406 | `PositiveDeletionPotential` |
| 31 | 0.9 | 1155 | 0 | 0.292721 | 0.707279 | 1.22854 | `PositiveDeletionPotential` |
| 31 | 0.9 | 1155 | 0.5 | 0.292721 | 0.707279 | 1.22854 | `PositiveDeletionPotential` |
| 37 | 0 | 1015 | 0.25 | 0.264758 | 0.735242 | 1.32894 | `PositiveDeletionPotential` |
| 37 | 0 | 1015 | 0.25 | 0.264758 | 0.735242 | 1.32894 | `PositiveDeletionPotential` |
| 37 | 0 | 1295 | 0.75 | 0.266667 | 0.733333 | 1.32176 | `PositiveDeletionPotential` |
| 37 | 0 | 1295 | 0.75 | 0.266667 | 0.733333 | 1.32176 | `PositiveDeletionPotential` |
| 37 | 0.5 | 1015 | 0.25 | 0.305053 | 0.694947 | 1.18727 | `PositiveDeletionPotential` |
| 37 | 0.5 | 1295 | 0.75 | 0.305053 | 0.694947 | 1.18727 | `PositiveDeletionPotential` |
| 37 | 0.5 | 1015 | 0.25 | 0.305053 | 0.694947 | 1.18727 | `PositiveDeletionPotential` |
| 37 | 0.5 | 1295 | 0.75 | 0.305053 | 0.694947 | 1.18727 | `PositiveDeletionPotential` |
| 37 | 0.9 | 1015 | 0.25 | 0.351648 | 0.648352 | 1.04512 | `PositiveDeletionPotential` |
| 37 | 0.9 | 1295 | 0.75 | 0.351648 | 0.648352 | 1.04512 | `PositiveDeletionPotential` |
| 37 | 0.9 | 1155 | 0 | 0.239126 | 0.760874 | 1.43076 | `PositiveDeletionPotential` |
| 37 | 0.9 | 1155 | 0.5 | 0.239126 | 0.760874 | 1.43076 | `PositiveDeletionPotential` |

## 5. 结构读数

当前层最小删除势为正，说明 `top-prime 持久支付` 在本层已经被实质删除吸收。
后续证明不应把 `0.880078...` 当作全局常数；正确链条是逐层登记 `D_n`。
若未来层 `D_n` 不可累加到无穷，则自动给出 `a_n->1` 的 NoDeletion 条件，接入 KL/PDEC 或 CleanKLS。
