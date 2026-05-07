# Triad-A1 删除势剖面：Q=30030 -> Q=510510

**状态：** `promoted_prime_essentiality_profile_materialized`

本审计把 fiber 删除势解释为 promoted prime residue choice 的必要性比例。当前层 killed residue choices 很多，因此仍在 FiberDeletion；若未来该比例趋零，则 promoted prime 近乎非必要，必须转入 NoDeletion-KL。

## 1. 结构语义

本层 promoted prime 为 `17`。对旧活跃相位 `t`，它的每个 fiber residue 只覆盖旧洞集中的一个模 `r` 残基类。

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
| `base_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `lift_multiplicity_json` | `400fadeec3a97b7cd6c22ed0bd5e1271c703ebda07ee074db7db549d43d9b4fd` |

## 3. 总表

| P | active phases | survival | deletion | D=-log(survival) | full | partial | singleton | support hist | avg removed survived | avg removed killed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 19 | 368 | 0.0792839 | 0.920716 | 2.53472 | 8 | 0 | 360 | `{'1': 360, '17': 8}` | 0.725806 | 0 |
| 23 | 936 | 0.162896 | 0.837104 | 1.81464 | 48 | 888 | 0 | `{'17': 48, '2': 888}` | 0.703704 | 0 |

## 4. 按旧洞数分桶

### P=19

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 136 | 136 | 0 | 1 | 0 |
| 1 | 6120 | 360 | 5760 | 0.0588235 | 0.941176 |

### P=23

| old holes | slots | surviving | killed | survival | deletion |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 816 | 816 | 0 | 1 | 0 |
| 2 | 15096 | 1776 | 13320 | 0.117647 | 0.882353 |

## 5. promoted prime 命中旧洞的效果

| P | zero-cover survival | zero-cover killed | positive-cover survival | positive-cover killed | zero-cover survival rate | positive-cover survival rate |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 136 | 5760 | 360 | 0 | 0.0230665 | 1 |
| 23 | 768 | 13320 | 1824 | 0 | 0.0545145 | 1 |

## 6. 读法

本审计不证明删除势无限发散；它把每层删除势拆成 promoted prime residue choice 的必要性比例。
后续若某层 `deletion_rate` 很小，不能视为失败，而是自动触发 NoDeletion-KL 门控。
