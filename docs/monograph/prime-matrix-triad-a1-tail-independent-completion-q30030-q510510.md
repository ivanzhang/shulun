# Triad-A1 Tail 独立完成审计：Q=30030 -> Q=510510

**状态：** `tail_independent_zero_cover_completion_audited`

本审计只统计非空旧洞集上的 zero-cover 幸存。当前这些幸存很少；说明 Tail_{>r} 独立完成不是当前删除势的主导机制。

## 1. 审计对象

只统计：

```text
old H_Q(t) nonempty；
promoted prime r 在 residue b 下覆盖 0 个旧洞；
Tail_{>r} 仍能完成 H_Q(t)。
```

这正是 DeletionPotential 失败时会出现的 TailIndependentCompletion。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `tail_independent_script` | `cbad37ce16854696c6d9b583691d2b87c3a1eaf9000c3618656acef5fc78cf1e` |
| `base_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `lift_multiplicity_json` | `400fadeec3a97b7cd6c22ed0bd5e1271c703ebda07ee074db7db549d43d9b4fd` |

## 3. 总表

| P | tail primes | nonempty zero-cover slots | tail-independent survivors | killed | survival rate | trivial empty-H survivors | completion mass | completion hist |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 19 | `[]` | 5760 | 0 | 5760 | 0 | 136 | 0 | `{}` |
| 23 | `[19]` | 14088 | 768 | 13320 | 0.0545145 | 0 | 768 | `{'1': 768}` |

## 4. 按旧洞数分桶

### P=19

| old holes | zero-cover slots | tail-independent survivors | killed | survival rate | completion mass |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 5760 | 0 | 5760 | 0 | 0 |

### P=23

| old holes | zero-cover slots | tail-independent survivors | killed | survival rate | completion mass |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 768 | 768 | 0 | 1 | 768 |
| 2 | 13320 | 0 | 13320 | 0 | 0 |

## 5. 读法

若 `tail_independent_survival_rate` 长期高，promoted prime 近乎非必要，进入 NoDeletion-KL。
若该比例长期低，zero-cover death 直接支付 DeletionPotential。
