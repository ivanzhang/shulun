# Triad-A1 删除势剖面：Q=2310 -> Q=30030

**状态：** `promoted_prime_essentiality_profile_materialized`

本审计把 fiber 删除势解释为 promoted prime residue choice 的必要性比例。当前层 killed residue choices 很多，因此仍在 FiberDeletion；若未来该比例趋零，则 promoted prime 近乎非必要，必须转入 NoDeletion-KL。

## 1. 结构语义

本层 promoted prime 为 `13`。对旧活跃相位 `t`，它的每个 fiber residue 只覆盖旧洞集中的一个模 `r` 残基类。

```text
survival_rate = surviving residue choices / all residue choices；
deletion_rate = killed residue choices / all residue choices；
deletion_potential = -log(survival_rate)。
```

若删除率长期不小，则删除势发散；若删除率趋零，则 promoted prime 在多数相位上近乎非必要，进入 NoDeletion-KL。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `deletion_profile_script` | `bf4210d5f98ad0fb245ba3782c19e7a6c8f0d7ef882a2676b255491c91bc3f60` |
| `base_multiplicity_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |
| `lift_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |

## 3. 总表

| P | active phases | survival | deletion | D=-log(survival) | full | partial | singleton | support hist | avg removed survived | avg removed killed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 17 | 28 | 0.0769231 | 0.923077 | 2.56495 | 0 | 0 | 28 | `{'1': 28}` | 1 | 0 |
| 19 | 140 | 0.202198 | 0.797802 | 1.59851 | 8 | 132 | 0 | `{'13': 8, '2': 132}` | 0.73913 | 0 |
| 23 | 232 | 0.310345 | 0.689655 | 1.17007 | 24 | 208 | 0 | `{'13': 24, '3': 208}` | 0.717949 | 0 |
| 29 | 150 | 0.312821 | 0.687179 | 1.16213 | 8 | 122 | 20 | `{'1': 20, '13': 8, '3': 2, '4': 120}` | 0.904918 | 0.0447761 |

## 4. 按旧洞数分桶

### P=17

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 364 | 28 | 336 | 0.0769231 | 0.923077 |

### P=19

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 104 | 104 | 0 | 1 | 0 |
| 2 | 1716 | 264 | 1452 | 0.153846 | 0.846154 |

### P=23

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 312 | 312 | 0 | 1 | 0 |
| 3 | 2704 | 624 | 2080 | 0.230769 | 0.769231 |

### P=29

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 104 | 104 | 0 | 1 | 0 |
| 4 | 1586 | 486 | 1100 | 0.306431 | 0.693569 |
| 5 | 260 | 20 | 240 | 0.0769231 | 0.923077 |

## 5. promoted prime 命中旧洞的效果

| P | zero-cover survival | zero-cover killed | positive-cover survival | positive-cover killed | zero-cover survival rate | positive-cover survival rate |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 0 | 336 | 28 | 0 | 0 | 1 |
| 19 | 96 | 1452 | 272 | 0 | 0.0620155 | 1 |
| 23 | 264 | 2080 | 672 | 0 | 0.112628 | 1 |
| 29 | 80 | 1280 | 530 | 60 | 0.0588235 | 0.898305 |

## 6. 读法

本审计不证明删除势无限发散；它把每层删除势拆成 promoted prime residue choice 的必要性比例。
后续若某层 `deletion_rate` 很小，不能视为失败，而是自动触发 NoDeletion-KL 门控。
