# Prime Matrix square-phase low-alpha z=61 fixed-core cycle nonpersistence comparator

**状态：** `z61_fixed_core_cycle_requires_named_persistent_phase_exclusion_open`

已有通用无循环输入可以排除免费无名回流，但不能排除当前 z=61 固定核心闭环，因为该闭环已经登记为命名持久相位 `b≡0 mod 28842`，且样本中负侧一次、正侧两次。因此当前最窄剩余不是继续重跑局部闭环，而是证明 PrefixGate signed phase balance 全局成立，或排斥 PersistentPhase-PDEC；直接短复现矛盾仍缺 `StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` 输入。

```text
fixed_core_cycle_named_persistent_phase_materialized=true
generic_no_free_cycle_does_not_exclude_named_persistent_phase=true
prefix_gate_signed_phase_balance_proved=false
persistent_phase_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 匹配结论

| check | value |
| --- | --- |
| target | `unbalanced<=8, omega=4, shell=(8D,16D]` |
| core/M | `4807 / 57684` |
| phase | `b ≡ 0 (mod 28842)` |
| phase hits by sign | `{'negative': 1, 'positive': 2, 'zero': 0}` |
| positive/negative phase actual | `2.000000` |
| generic no-free cycle imported | true |
| generic no-cycle sufficient here | false |
| direct short-return input available | false |

## 2. 剩余义务

| obligation | closed | why needed |
| --- | --- | --- |
| `PrefixGateSignedPhaseBalance` | false | 固定相位 `b≡0 mod 28842` 已持久出现；必须证明正侧 quotient 2,4 全局伴随并吸收负侧 quotient 1。 |
| `PersistentPhasePDECExclusion` | false | 若 signed balance 不能全局证明，就要排斥这个命名持久相位 PDEC。 |
| `StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` | false | 若要直接从早期零行反例链撞出矛盾，还必须证明短稳定同标签复现或相位缺陷登记。 |

## 3. 证明边界

- 已闭合：旧无循环输入与当前固定核心闭环的适用边界已明确。
- 未闭合：PrefixGate signed phase balance 或 PersistentPhase-PDEC 排斥。
- 下一目标：`PrefixGateSignedPhaseBalanceOrPersistentPhasePDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-clean-core-source-loop-cut-router.json` | `6ef150041b8fc9a4b8f18d79dae9d3f88de6a23b84f2e9d1c0a631316243971f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-ledger-router.json` | `97de4961d3eb4ce5b77cd7d8c2527cae71c8aa3fbef572487f863d6a8c43631d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json` | `7470bdf7651a2cdc84f388e336e7c4273cbb2aa2836bb149c17330950fe3365f` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json` | `960a954eca848fa45c0ebb0c0086357477c058bbaf7dc4a3f966117c8c03ce21` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_nonpersistence_comparator.py` | `67a086f0c9f4dd41edde3b31e8198311eb1dc936a6cbda2025553eeb37f98b5c` |
