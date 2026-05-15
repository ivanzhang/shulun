# Prime Matrix square-phase low-alpha z=61 fixed-core dyadic balance lemma

**状态：** `z61_fixed_core_dyadic_balance_reduced_to_positive_lift_existence_open`

固定核心的局部吸收可抽象为同权 dyadic balance 引理：同一 hit-moduli 组内单位权重相同，负 quotient `1` 若有正 quotient `2,4` 两个 lift，则 signed count 和 signed weight 自动为正。样本内该引理闭合；剩余不再是权重比较，而是全局证明正向 dyadic lift 必存在，或登记 MissingLift-PDEC。

```text
same_unit_weight_on_phase_hits=true
negative_quotients=[1]
dyadic_positive_quotients=[2, 4]
positive_count_at_least_twice_negative=true
signed_phase_count=1
signed_phase_weight=0.555427
fixed_core_dyadic_balance_lemma_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. Quotient rows

| quotient | sign | p | q | a | b | mult | contribution | signed | singleton | short delta |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | `negative` | 36739 | 53 | 883 | 28842 | 1 | 0.555427 | -0.555427 | true | true |
| 2 | `positive` | 200003 | 71 | 9767 | 57684 | 1 | 0.555427 | 0.555427 | true | true |
| 4 | `positive` | 200003 | 37 | 9371 | 115368 | 1 | 0.555427 | 0.555427 | true | true |

## 2. 自足引理

在固定 hit-moduli 组中，单位权重只由目标模数组决定；若负侧只有 quotient `1` 一次命中，而正侧存在 quotient `2,4` 两个同组命中，则

```text
signed_count = 2 - 1 = 1 > 0,
signed_weight = 2w - w = w > 0.
```

因此该固定核心的局部剩余已经从权重估计降为正向 lift 存在性。

## 3. 证明边界

- 已闭合：样本内同权 dyadic balance 引理。
- 未闭合：全局证明 quotient `2,4` 正向 lift 必伴随 quotient `1` 负锚，或登记 MissingLift-PDEC。
- 下一目标：`PositiveDyadicLiftExistenceForFixedCoreOrMissingLiftPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json` | `ea2150eaee0eb08d7f7a3412b3d35821bac7f1901f2fa37028335cf16c9b5d0f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json` | `7470bdf7651a2cdc84f388e336e7c4273cbb2aa2836bb149c17330950fe3365f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json` | `b35e0485419f8a462a1dfc40b2bbdcf1aff19d97415544ef995dd00fb057e7fc` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_dyadic_balance_lemma_router.py` | `472d86c23320980e8f20dcb04358657e2adbc4e211d145d2aa5071d1d527444d` |
