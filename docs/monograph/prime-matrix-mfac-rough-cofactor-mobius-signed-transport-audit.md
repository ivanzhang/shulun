# MFAC-1A 粗辅因子 Möbius 带符号传输状态审计

**状态：** `lpf_local_state_insufficient_for_exact_mobius_payload_audit`
**核验日期：** `2026-08-06`

本审计只检验 source state 的充分性，不构造一般 signed transport，
不提供平方根误差、零点排除或 RH 结论。

## 1. 精确 source 恒等式

```text
Lambda(n) = - sum_{d|n} mu(d) log(d)
```

每个非零 Möbius 除数以 source pair `(d,m)`（其中 `n=d*m`）单独登记。

## 2. 审计读数

```text
mobius_von_mangoldt_identity_verified=true
source_pair_partition_verified=true
source_pair_count=4975
lpf_local_state_collision_found=true
divisor_history_augmentation_removes_payload_collision=true
mfac_1a_constructed=false
downstream_recovery_used=false
row_column_unconditional_closed=false
```

## 3. 最小碰撞

LPF-local state: `(2, 3, 2)`

| source | n | d | m | mu(d) | log(d) factors |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 6 | 3 | 2 | -1 | (3,) |
| 2 | 12 | 6 | 2 | 1 | (2, 3) |

## 4. 结论边界

全局 Möbius--von Mangoldt source pair 可逐项枚举，但仅以 owner LPF、当前 rough cofactor q 与 m 组成的局部状态会把不同 divisor-history 压到同一状态，并要求不同 Möbius 符号和 log(d) 分解。因此该 LPF-local 状态不足以构造 MFAC-1A 的 exact signed transport；必须保留完整 divisor-history 或等价的可追溯状态。

下一步必须把 source state 扩展为完整 divisor-history 或等价的可追溯状态，
随后才可尝试定义推前前的 exact transport record。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py` | `8c11b60928eb4baad0a54f2d09177bf6de6ef78fd32b5a3888f17ca148217563` |
| `docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json` | `8f696d3cb025e8d98790530763d5b87717c945b57c310f6d16f4c49711c8fdcb` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json` | `96d6dadbc5add815f8623295aae5ae519c0b5e44db556d85d657259db97a9773` |
