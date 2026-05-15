# Prime Matrix square-phase low-alpha z=61 QuotientLock fixed-core bridge

**状态：** `z61_quotient_lock_fixed_core_bridged_to_dyadic_absorber_global_open`

固定核心检查显示 QuotientLock-PDEC 不是一个新的孤立缺口：`core=4807` 与 Prefix/CommonCore 的核心相同，负锚相位为 `B=6C=28842`，而 QuotientLock 的 `M=57684` 正是 `2B`。样本内该相位有 quotient `1,2,4` 三个命中，两个正向 dyadic lift 的同权贡献恰好以 2:1 吸收负锚。因此不能用相位缺席排斥它；下一步必须把这种 dyadic signed balance 全局化，或登记 PersistentPhase-PDEC。

```text
phase_modulus_equals_6core=true
quotient_lock_modulus_equals_12core=true
quotient_lock_modulus_is_positive_lift_2B=true
common_core_bridge_closed=true
hit_lcm_bridge_closed=true
quotient_lock_fixed_core_bridge_closed_for_sample=true
quotient_lock_pdec_locally_absorbed_by_dyadic_lifts=true
row_column_unconditional_closed=false
```

## 1. 核心桥接

| quantity | value | relation |
| --- | ---: | --- |
| C | 4807 | fixed core |
| B | 28842 | `6C` |
| M | 57684 | `12C=2B` |

## 2. Quotient ladder

| source | quotients |
| --- | --- |
| phase hits | `[1, 2, 4]` |
| dyadic absorber | `[2, 4]` |
| source congruence | `[1, 2, 4]` |

## 3. q 匹配

| check | value |
| --- | --- |
| quotient 2 source q = q2 | true |
| quotient 4 source q = q4 | true |
| quotient 2 b = M | true |
| quotient 4 b = 2M | true |

## 4. Signed phase balance

| negative actual | positive actual | ratio | same unit weight | local absorption |
| ---: | ---: | ---: | --- | --- |
| 0.555427 | 1.110853 | 2.000000 | true | true |

## 5. 证明边界

- 已闭合：固定核心检查完成；QuotientLock-PDEC 与既有 dyadic 吸收链同一对象。
- 已排除的路线：不能靠相位缺席排斥，因为该相位在样本内持久出现。
- 未闭合：把 dyadic signed balance 全局化，或登记并排斥 PersistentPhase-PDEC。
- 下一目标：`FixedCoreDyadicAbsorberGlobalizationOrPersistentPhasePDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json` | `ea2150eaee0eb08d7f7a3412b3d35821bac7f1901f2fa37028335cf16c9b5d0f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json` | `65ce21708202ca8dcc7098eb114492541672abe0cb55743e74e261e81998e034` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json` | `4784443770637bbe4832130b0d33a9d72035071ad39e497e65ff67571c5d16d1` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json` | `23bc56d8d9a7bb56e2dda988ad66df5d49fa7e51e00bef1f81adc6cbae146523` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json` | `7470bdf7651a2cdc84f388e336e7c4273cbb2aa2836bb149c17330950fe3365f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json` | `de2e08cee034406c26eafaed8b009646d6310f645e4c04d8d552f77cd5df216e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_fixed_core_bridge_router.py` | `02be46961895cd5b082f65f22dd019c01f0ce4436388f0c72003b03aaf623c92` |
