# Prime Matrix AffineTwin actual packet critical-load contract

**状态：** `current_sweep_actual_packet_contract_closed_global_open`

本合同把 AffineTwin 平方根门从形式包络 `M_q^{form}=A_g A_f` 改写为实际非 PDEC packet 数 `N_q`。
当前 sweep 中 actual packets 全部注入 primitive 支撑，并满足 actual 平方根门；全局仍需证明 primitive 支撑耗尽、收紧形式乘积账本并排斥支撑逃逸。

```text
candidate_q_values=[31, 43, 103]
actual_q_values_current=[31]
total_formal_product_upper=40
total_actual_packet_count_current=1
total_formal_to_actual_gap=39
all_actual_packets_pass_sqrt_gate_current=true
projection_collision_pdec_count_current=0
row_column_unconditional_closed=false
```

## 1. actual packet 表

| q | M_form | N_q current | support W | capacity | formal load ratio | actual load ratio | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 12 | 1 | 20 | 899 | 0.160178 | 0.001112 | `ActualPrimitiveSupportAbsorbed+ProductAccountingTightening` |
| 43 | 16 | 0 | 26 | 1763 | 0.145207 | 0.000000 | `NoActualPacketCurrentSweep+ProductAccountingTightening` |
| 103 | 12 | 0 | 56 | 10403 | 0.013842 | 0.000000 | `NoActualPacketCurrentSweep+ProductAccountingTightening` |

## 2. 结论

- 当前 sweep 的 actual load 为 `N_q^2`，不是形式上界 `(A_g A_f)^2`。
- 当前 actual packets 全部满足 `N_q <= W_q <= sqrt(q(q-2))`。
- 形式包络和 actual load 的差额被登记为 `ProductAccountingTightening`，不能作为真实矛盾使用。
- 若未来出现 `N_q>W_q`，它必须进入 `ProjectionCollision-PDEC/ColumnCRT`。
- 若 actual packet 不落入 primitive 支撑，它必须进入 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 3. 仍未闭合

- 全局 `PrimitiveTwinSlotSupportExhaustion` 尚未证明。
- 全局 `ProductAccountingTightening` 尚未完成。
- `PrimitiveTwinSlotSupportEscape-PDEC/SAE` 尚未排斥。
- 因此行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json` | `44e048bbb9be8b3e2fa427090bf3bfa613575035385807986c0b7a3c664ff50a` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
